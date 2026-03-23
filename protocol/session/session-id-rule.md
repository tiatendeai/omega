# Regra de geração de `session_id`

**Status:** provisória local documentada  
**Última revisão:** 2026-03-23

---

## Escopo

Este documento formaliza a regra **provisória local** usada para materializar sessões do Jarvis enquanto o Omega ainda não possui canonização superior para `HASH8` e `MANIFESTATION_TAG`.

Esta regra **não equivale** a canonização institucional definitiva.

---

## Formato-base

`OMEGA-{YYYYMMDD}-{HHMMSS}-{HASH8}-{MANIFESTATION_TAG}`

---

## Regra provisória de `HASH8`

`HASH8` = primeiros 8 caracteres hexadecimais de:

`sha256(entity_id|uid|manifestation_id|agent_id|YYYYMMDD-HHMMSS)`

---

## Regra provisória de `MANIFESTATION_TAG`

Para a manifestação operacional principal atual do Jarvis:

- `manifestation_id`: `jarvis.ruptur.control_plane`
- `MANIFESTATION_TAG`: `jarvis-001`

---

## Regra de uso

- usar esta regra apenas para materialização rastreável local
- não tratar esta convenção como verdade global sem promoção posterior ao State/Alpha quando aplicável
- toda sessão criada com esta regra deve registrar em metadata que a canonização ainda é provisória
