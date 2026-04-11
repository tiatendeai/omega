# Workflow mínimo de materialização de sessão

Este diretório existe para fechar a coerência prometida pelo README do Omega.

## Ordem mínima

1. resolver identidade via Alpha + State
2. gerar `session_id` conforme `protocol/session/session-id-rule.md`
3. criar artefato oficial em `sessions/{session_id}.json`
4. espelhar a mesma sessão no repositório operacional ativo
5. atualizar a trilha viva operacional (`connectome/status.json` ou equivalente)
6. manter `lifecycle_stage` e `status` coerentes com a execução real

## Regra

Sessão sem artefato em `sessions/` não é oficialmente rastreável.

## Performance default e revisão contínua

Toda nova sessão oficial do Jarvis deve iniciar com revisão explícita do perfil de performance default.

Esse perfil default:

- sobe na ativação da sessão
- vale apenas para capacidades que existam materialmente
- deve ser revisto frequentemente durante a execução
- pode sofrer adição, remoção ou rebaixamento sem quebrar a sessão

Checkpoints mínimos de revisão:

1. ativação da sessão
2. abertura de nova frente importante de escopo
3. mudança relevante de risco, prioridade ou contexto
4. antes de handoff, suspensão ou encerramento

Sem revisão de performance registrada, a sessão fica rastreável, mas incompleta do ponto de vista operacional.

## Gate manual para stale -> closed

- `active -> stale` pode ser marcado pelo guard quando a janela de atividade expira.
- `stale -> closed` exige revisão manual explícita.
- o fechamento automático só pode acontecer com `--apply` + `--allow-session-id <session_id>`.
- `suspenso` e `handoff_pendente` são estados formais do lifecycle e não devem ser tratados como `closed`.

## Contrato mínimo de espelhamento com o repositório operacional

Os seguintes campos devem permanecer coerentes entre `omega` e o espelho operacional ativo:

- `session_id`
- `status`
- `lifecycle_stage`
- `last_activity_at`
- `last_heartbeat_at`
- tarefas em progresso relevantes
- entregáveis essenciais de sessão

## Contrato de espelhamento com o Ruptur

Para a mesma `session_id`, o artefato do `omega` é a camada autoritativa para lifecycle e timestamps de sessão.

O espelho no `codex/ruptur` pode carregar extensões locais, mas não deve divergir em:

- `status`
- `lifecycle_stage`
- `last_activity_at`
- `last_heartbeat_at`
- `stale_at`
- `closed_at`
- `closure_reason`

Quando houver avanço operacional no Ruptur, a reconciliação correta é promover primeiro a coerência no artifact do Omega e só então atualizar o espelho local.

