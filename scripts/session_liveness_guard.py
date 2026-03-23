#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        return None


def to_utc(dt: datetime) -> datetime:
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def latest_signal(session: dict[str, Any], policy: dict[str, Any]) -> tuple[str | None, datetime | None]:
    candidates: list[tuple[str, datetime]] = []
    for field in [policy.get('heartbeat_field'), policy.get('activity_field'), 'closed_at', 'created_at']:
        if not field:
            continue
        dt = parse_dt(session.get(field))
        if dt:
            candidates.append((field, to_utc(dt)))
    meta = session.get('metadata') or {}
    liveness = meta.get('liveness') or {}
    for field in ['last_checked_at', 'last_connectome_sync_at']:
        dt = parse_dt(liveness.get(field))
        if dt:
            candidates.append((f'metadata.liveness.{field}', to_utc(dt)))
    if not candidates:
        return None, None
    return max(candidates, key=lambda item: item[1])


def protection_signals(session: dict[str, Any]) -> dict[str, bool]:
    meta = session.get('metadata') or {}
    liveness = meta.get('liveness') or {}
    signals = liveness.get('protection_signals') or {}
    normalized = {str(k): bool(v) for k, v in signals.items()}
    if any((task or {}).get('status') == 'in_progress' for task in session.get('tasks') or []):
        normalized.setdefault('task_in_progress', True)
    return normalized


def classify(session: dict[str, Any], policy: dict[str, Any], now: datetime) -> dict[str, Any]:
    status = session.get('status')
    signal_field, signal_dt = latest_signal(session, policy)
    protections = protection_signals(session)
    active_protections = sorted([name for name, value in protections.items() if value])
    result = {
        'session_id': session.get('session_id'),
        'status': status,
        'latest_signal_field': signal_field,
        'latest_signal_at': signal_dt.isoformat() if signal_dt else None,
        'active_protections': active_protections,
        'decision': 'noop',
        'reason': None,
        'minutes_since_signal': None,
    }
    if status not in {'active', 'stale'}:
        result['reason'] = 'status_not_managed'
        return result
    if signal_dt is None:
        result['decision'] = 'manual_review'
        result['reason'] = 'insufficient_liveness_data'
        return result
    age_minutes = int((now - signal_dt).total_seconds() // 60)
    result['minutes_since_signal'] = age_minutes
    if active_protections:
        result['decision'] = 'keep_active'
        result['reason'] = 'protected_by_liveness_signals'
        return result
    stale_after = int(policy.get('stale_after_minutes', 180))
    close_after = int(policy.get('auto_close_after_minutes', 1440))
    if age_minutes >= close_after:
        result['decision'] = 'auto_close_candidate'
        result['reason'] = 'inactive_timeout_reached'
    elif age_minutes >= stale_after:
        result['decision'] = 'mark_stale_candidate'
        result['reason'] = 'stale_window_reached'
    else:
        result['decision'] = 'keep_active'
        result['reason'] = 'within_activity_window'
    return result


def apply_decision(session: dict[str, Any], decision: dict[str, Any], policy: dict[str, Any], now: datetime) -> bool:
    changed = False
    meta = session.setdefault('metadata', {})
    liveness = meta.setdefault('liveness', {})
    liveness['last_checked_at'] = now.isoformat()
    liveness['last_decision'] = decision['decision']
    liveness['last_decision_reason'] = decision['reason']
    liveness['last_decision_minutes_since_signal'] = decision['minutes_since_signal']
    if decision['decision'] == 'mark_stale_candidate' and session.get('status') == 'active':
        session['status'] = policy.get('stale_status', 'stale')
        session['stale_at'] = now.isoformat()
        changed = True
    elif decision['decision'] == 'auto_close_candidate':
        session['status'] = policy.get('close_status', 'closed')
        session['lifecycle_stage'] = 'CLOSURE'
        session['closed_at'] = now.isoformat()
        session['closure_reason'] = policy.get('closure_reason', 'auto_inactive_timeout')
        changed = True
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description='Avalia liveness e autoencerramento auditável de sessões OMEGA.')
    parser.add_argument('--sessions-dir', default='sessions')
    parser.add_argument('--policy', default='configs/session-liveness-policy.json')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--report-path', default='reports/liveness-report.json')
    args = parser.parse_args()

    sessions_dir = Path(args.sessions_dir)
    policy_path = Path(args.policy)
    policy = json.loads(policy_path.read_text())['policy']
    now = datetime.now(timezone.utc)
    report: list[dict[str, Any]] = []
    changed_files: list[str] = []

    for path in sorted(sessions_dir.glob('*.json')):
        session = json.loads(path.read_text())
        decision = classify(session, policy, now)
        if args.apply:
            changed = apply_decision(session, decision, policy, now)
            if changed:
                path.write_text(json.dumps(session, ensure_ascii=False, indent=2) + '\n')
                changed_files.append(str(path))
        report.append(decision)

    output = {
        'checked_at': now.isoformat(),
        'apply_mode': bool(args.apply),
        'policy_path': str(policy_path),
        'sessions_dir': str(sessions_dir),
        'changed_files': changed_files,
        'report': report,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
