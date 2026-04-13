# Sessões oficiais do Omega

Este diretório é a trilha oficial de lifecycle das sessões do Jarvis.

## Regra mínima

- cada sessão deve ter um único arquivo JSON com `session_id` único
- o arquivo deve ser compatível com `protocol/session/session-schema.json`
- o repositório operacional ativo deve manter espelho auditável da mesma sessão
- o encerramento da sessão deve atualizar `status` e `lifecycle_stage`

## Regra de stale e fechamento

- `stale` indica sessão sem atividade recente e sem proteção suficiente.
- `closed` exige `closed_at` + `closure_reason`.
- o fechamento por inatividade deve passar por gate manual quando a policy exigir revisão humana.
