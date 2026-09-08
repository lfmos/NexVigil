# NexVigil Roadmap

## v1.0.0 — Core Security Validation Lab

**Status:** Concluído

- [x] FastAPI Security Lab
- [x] Telemetria estruturada em JSON Lines
- [x] Brute-force simulation
- [x] Compromise simulation
- [x] Detection Engine em Python
- [x] Event correlation
- [x] MITRE ATT&CK T1110
- [x] Alertas HIGH / CRITICAL
- [x] Event IDs
- [x] Alert IDs
- [x] Persistent state
- [x] Incremental event processing
- [x] Alert deduplication
- [x] Restart safety
- [x] Documentação de incidentes
- [x] Pytest
- [x] Bandit SAST
- [x] pip-audit
- [x] GitHub Actions
- [x] Wazuh single-node deployment
- [x] Documentação de integração Wazuh SIEM

---

## v1.0.1 — Documentation and Portfolio Polish

**Status:** Concluído

- [x] Finalização e refinamento da documentação do projeto
- [x] Ajustes de apresentação para portfólio

---

## v1.0.2 — Security Hardening

**Status:** Concluído

- [x] Remoção de artefatos de runtime do versionamento
- [x] Remoção de arquivos `__pycache__` rastreados
- [x] MIT License
- [x] Testes automatizados da API FastAPI
- [x] Validação de que senhas não são gravadas na telemetria
- [x] Tratamento seguro de eventos e timestamps inválidos
- [x] CI configurado para Python 3.11 e 3.13
- [x] Validação com `compileall`
- [x] Bandit SAST
- [x] Auditoria de dependências com pip-audit
- [x] Atualização da documentação de segurança e arquitetura

---

## Futuras evoluções

As funcionalidades abaixo **não fazem parte do escopo implementado da v1.0.0**.

### Detection Engineering

- novas técnicas MITRE ATT&CK;
- password spraying;
- credential stuffing;
- impossible travel;
- privilege escalation;
- behavioral detection;
- risk scoring.

### Cloud Security

- AWS CloudTrail;
- CloudWatch;
- GuardDuty;
- EventBridge;
- Lambda;
- infraestrutura reproduzível com Terraform.

A infraestrutura cloud deverá ser criada sob demanda e destruída após os testes para reduzir custos.

### SOAR

- playbooks de resposta;
- enriquecimento automático;
- bloqueio controlado;
- revogação de sessão;
- ações críticas com aprovação humana.

### AI Security

- SOC Copilot local;
- sumarização de incidentes;
- apoio à investigação;
- RAG com base de conhecimento de segurança;
- testes de prompt injection;
- controles contra execução arbitrária de ações.

### Observabilidade

- dashboards adicionais;
- métricas de detecção;
- acompanhamento de falsos positivos;
- Mean Time to Detect;
- Mean Time to Investigate.

---

## Princípio do projeto

O roadmap representa possibilidades de evolução e não funcionalidades já implementadas.

O NexVigil v1.0.0 permanece utilizável e demonstrável independentemente dessas futuras extensões.