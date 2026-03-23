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
