# Loop de revisão de performance por sessão

**Status:** ativo
**Última revisão:** 2026-03-23

---

## Objetivo

Garantir que novas sessões do Jarvis iniciem com baseline de performance e revisem esse baseline ao longo da execução real.

---

## Regra-base

Toda sessão oficial deve:

1. subir com um perfil de performance default documentado
2. registrar capacidades ativas e pendentes
3. revisar continuamente a utilidade dessas capacidades
4. adicionar, remover ou rebaixar capacidades quando o contexto pedir

---

## Checkpoints mínimos

- na ativação
- em troca importante de escopo
- em mudanças de risco, prioridade ou contexto
- antes de handoff
- antes de suspensão
- antes de encerramento

---

## Regra de prudência

Capacidade inexistente, incompleta ou só desejada não entra como ativa por default.

Ela deve ficar como:

- pendente
- débito
- automação incompleta

---

## Resultado esperado

A sessão não depende mais de memória manual para ativar performance, e também não fica presa a um baseline rígido que nunca é reavaliado.
