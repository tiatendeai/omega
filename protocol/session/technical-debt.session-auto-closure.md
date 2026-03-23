# Débito técnico — autoencerramento de sessões inativas

**Status:** débito técnico documentado  
**Data:** 2026-03-23  
**Escopo:** `omega` / lifecycle de sessão

---

## Problema

Hoje, o encerramento de uma sessão do Jarvis pode depender demais de ação manual ou decisão explícita do operador.

Isso cria um risco estrutural:

- sessões antigas podem permanecer marcadas como ativas sem estarem realmente em uso
- o histórico operacional pode ficar poluído por sessões zumbis
- o lifecycle deixa de refletir o estado real de atividade
- a retomada futura pode ler uma sessão falsamente ativa como se ainda fosse a sessão vigente

---

## Princípio desejado

O encerramento usual de sessões **não deve depender exclusivamente da iniciativa manual do usuário**.

O `omega` deve evoluir para possuir uma política explícita de:

- detecção periódica de sessões inativas
- validação de liveness real
- encerramento automático de sessões que não estejam mais verdadeiramente em uso

Ao mesmo tempo, o sistema **não pode encerrar automaticamente uma sessão que ainda esteja ativa de verdade**.

---

## Regra alvo

A regra desejada para o `omega` é:

1. toda sessão ativa deve possuir sinais verificáveis de atividade recente
2. sessões sem sinal confiável de atividade por um intervalo definido devem entrar em avaliação
3. se a sessão não estiver realmente em uso, ela deve ser encerrada automaticamente
4. se a sessão ainda estiver em uso, ela deve permanecer aberta
5. todo autoencerramento deve deixar trilha auditável do motivo, horário e critério aplicado

---

## Requisitos funcionais futuros

O `omega` deve passar a suportar, no mínimo:

### 1. Sinal de liveness

Cada sessão ativa deve ter algum mecanismo confiável de atividade, por exemplo:

- `last_heartbeat_at`
- `last_activity_at`
- atualização coerente de `last_updated`
- confirmação de uso pela trilha operacional viva
- lock/lease de sessão vigente

### 2. Janela de inatividade

Deve existir uma política configurável de timeout, por exemplo:

- sessão candidata a stale após X minutos/horas sem atividade
- sessão candidata a encerramento após Y minutos/horas adicionais sem retomada

### 3. Estado intermediário

Antes do fechamento automático, a sessão pode passar por um estado intermediário como:

- `stale`
- `suspeita_de_inatividade`
- `aguardando_encerramento_automatico`

### 4. Proteção contra falso positivo

O sistema não deve encerrar uma sessão se houver evidência de uso real, como:

- heartbeat recente
- tarefa em progresso atualizada
- operador/agent lock ativo
- artefato operacional mudando dentro da janela válida

### 5. Encerramento auditável

Ao autoencerrar, registrar:

- `closed_at`
- `closure_reason: auto_inactive_timeout`
- última evidência de atividade conhecida
- regra/threshold aplicada
- origem da decisão de fechamento

---

## Requisitos não funcionais

- a política deve ser determinística e auditável
- o mecanismo deve evitar encerrar sessões legítimas em uso
- o critério de fechamento deve ser configurável, não hardcoded sem governança
- a regra deve ser compatível com handoff, suspensão e recovery
- o comportamento deve poder ser inspecionado por outro agente ou operador sem ambiguidade

---

## Risco que este débito evita

Sem esse mecanismo, o ecossistema corre risco de:

- acumular sessões formalmente abertas, mas operacionalmente mortas
- gerar confusão sobre qual sessão está realmente viva
- degradar replay, recovery e handoff
- depender demais de disciplina manual para manter a verdade do lifecycle

---

## Critério de aceite futuro

Este débito só pode ser considerado resolvido quando o `omega` possuir:

1. campo(s) formais de liveness no contrato de sessão
2. política explícita de timeout/inatividade
3. processo periódico de avaliação de sessões ativas
4. autoencerramento auditável de sessões realmente inativas
5. proteção explícita para não fechar sessões ainda em uso
6. documentação canônica do fluxo de stale -> encerramento

---

## Observação de governança

Esta política deve ser tratada como evolução do lifecycle do `omega`.

Ela **não autoriza** fechar automaticamente sessões só por conveniência.  
Ela existe para garantir que o estado formal do sistema continue aderente ao uso real.

Em resumo:

- sessão inativa de verdade -> deve poder ser encerrada automaticamente
- sessão ainda em uso -> não deve ser encerrada

