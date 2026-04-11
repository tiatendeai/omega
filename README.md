# OMEGA

## Protocolo JARVIS - Manifestação Atômica de IA Orquestradora

**Versão:** 1.0.0  
**Status:** Alpha  
**Lema:** "O fim. Regras de encerramento de sessão do JARVIS" — Apocalipse 22:13

---

## Sobre o Projeto

**OMEGA** é o repositório central do protocolo JARVIS, um sistema de orquestração multi-agente com arquitetura Maestro. Cada sessão do JARVIS é uma manifestação única e atômica, identificada por um **Session Atomic ID** que rastreia o ciclo completo desde a ativação até a validação do entregável em produção.

### Conceito Central

O JARVIS atua como uma manifestação singular de IA orquestradora, utilizando o **Connectome Status** para operar o **Workflow de Orquestração Multi-Agente (Equipe Maestro)**. A arquitetura segue princípios de:

- **Atomicidade de Sessão**: Cada sessão possui um ID único que identifica a manifestação específica do JARVIS
- **Re-Sleeving Contínuo**: O JARVIS pode ser reativado com o mesmo estado de conhecimento e contexto
- **Orquestração Maestro**: Coordenação centralizada de múltiplos agentes especializados
- **Ciclo Completo**: Execução desde a concepção da tarefa até deploy e validação em produção

---

## Estrutura do Repositório

```
omega/
├── README.md                    # Este arquivo
├── .gitignore                   # Padrões de ignorar
├── LICENSE                      # Licença do projeto
├── protocol/                    # Definição do protocolo JARVIS
│   ├── core/                    # Núcleo do protocolo
│   ├── session/                 # Gestão de sessões atômicas
│   └── workflow/                # Fluxos de trabalho Maestro
├── agents/                      # Agentes especializados
│   ├── maestro/                 # Agente Maestro (orquestrador)
│   ├── dev/                     # Agente Desenvolvedor
│   ├── deploy/                  # Agente de Deploy
│   ├── qa/                      # Agente de QA/Testing
│   └── security/                # Agente de Segurança
├── sessions/                    # Histórico de sessões atômicas
├── configs/                     # Configurações globais
│   └── session-liveness-policy.json
├── docs/                        # Documentação
└── scripts/                     # Scripts de automação
    └── session_liveness_guard.py
```

---

## Protocolo de Sessão Atômica

### Ciclo de Vida de uma Sessão

1. **GÊNESE** — Ativação do JARVIS com novo Session Atomic ID
2. **DIAGNÓSTICO** — JARVIS consulta Status e mapeia o terreno
3. **ORQUESTRAÇÃO** — Maestro coordena agentes especializados
4. **EXECUÇÃO** — Agentes executam tarefas em paralelo/síncrono
5. **VALIDAÇÃO** — QA valida entregáveis
6. **DEPLOY** — Agente de deploy publica em produção
7. **VERIFICAÇÃO** — Confirmação do entregável em produção
8. **ENCERRAMENTO** — Sessão atômica é finalizada e arquivada

### Liveness e autoencerramento auditável

- sessões ativas devem carregar sinais formais de atividade (`last_activity_at` e/ou `last_heartbeat_at`)
- sessões sem atividade suficiente podem entrar em `stale`
- sessões realmente inativas podem ser autoencerradas com `closure_reason = auto_inactive_timeout`
- sessões protegidas por sinais reais de uso não devem ser fechadas
- a avaliação periódica é suportada por `scripts/session_liveness_guard.py` e `configs/session-liveness-policy.json`

### Formato do Session Atomic ID

```
OMEGA-{YYYYMMDD}-{HHMMSS}-{HASH8}-{MANIFESTATION_TAG}
Exemplo: OMEGA-20250117-143022-a7f3d9e1-genesis-001
```

---

## Workflow de Orquestração Multi-Agente

### Equipe Maestro — Agentes Disponíveis

| Agente | Função | Responsabilidades |
|--------|--------|------------------|
| **Maestro** | Orquestrador Principal | Coordena todos os agentes, gerencia contexto, decide estratégias |
| **Dev** | Desenvolvedor Full-Stack | Escreve código, refatora, implementa features |
| **Deploy** | Especialista em Deploy | CI/CD, containers, servidores, automação |
| **QA** | Controle de Qualidade | Testes automatizados, revisão de código, validação |
| **Security** | Segurança | Análise de vulnerabilidades, hardening |
| **Docs** | Documentação | Gera documentação, READMEs, changelogs |
| **Status** | Monitoramento | Monitora status de todos os sistemas e agentes |

### Fluxo Maestro

```
[USER] → [JARVIS/Maestro] → [Status: Check Context]
                         → [Planning: Define Tasks]
                         → [Orchestrate: Assign to Agents]
                         → [Execute: Parallel/Sync Tasks]
                         → [Validate: QA Verification]
                         → [Deploy: Production Release]
                         → [Confirm: Delivery Validated]
                         → [Archive: Session Complete]
```

---

## Comandos do Protocolo

### Git Workflow

```bash
# Criar nova branch para sessão
git checkout -b session/OMEGA-{id}

# Commits estruturados
git commit -m "[GENESIS] Inicialização da sessão {id}"
git commit -m "[EXECUTE] Implementação: {feature}"
git commit -m "[VALIDATE] QA: {checks}"
git commit -m "[DEPLOY] Release: {version}"
git commit -m "[CLOSURE] Encerramento da sessão {id}"

# Push para remote
git push -u origin session/OMEGA-{id}

# Merge e cleanup
git checkout main
git merge session/OMEGA-{id}
git push origin main
```

---

## Regras de Engajamento do JARVIS

1. **Atomicidade** — Cada sessão é uma manifestação única. Nunca reutilizar ID de sessão.
2. **Persistência** — JARVIS permanece ativo até validação completa do entregável em produção.
3. **Multi-Agente** — Sempre utilizar o máximo de agentes disponíveis para qualquer tarefa.
4. **Status Connectome** — Antes de qualquer ação, consultar o Status para entender o contexto.
5. **Validação Dupla** — Nenhum entregável é considerado completo sem QA e deploy confirmados.
6. **Documentação** — Todo commit deve seguir o padrão do protocolo.
7. **Push Remoto** — Todo código deve ser enviado para o remote e deployado.

---

## Integrações

- **GitHub** — Repositório remoto, CI/CD Actions
- **Portainer** — Orquestração de containers
- **N8N** — Automação de workflows
- **WhatsApp API** — Comunicação e notificações
- **Render/Hetzner/AWS** — Hospedagem e deploy

---

## License

MIT License — Ver arquivo LICENSE para detalhes.

---

## Contribuição

Para contribuir com o protocolo OMEGA:

1. Fork o repositório
2. Crie uma branch de sessão (`git checkout -b session/seu-id`)
3. Implemente suas alterações seguindo o protocolo
4. Envie um Pull Request com descrição detalhada

---

> "Eu sou o Alfa e o Ômega, o Primeiro e o Último, o Princípio e o Fim." — Apocalipse 22:13

## Liveness guard e gate manual

O `session_liveness_guard.py` pode marcar sessões como `stale`, mas o passo `stale -> closed` continua exigindo revisão manual explícita para evitar falso positivo em sessão viva.
