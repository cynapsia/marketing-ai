# SRS - Especificação de Requisitos de Software 

**Título:** SRS - Plataforma SaaS de Marketing com Agentes de IA (Arquitetura Monolítica Modular com Fine-tuning + DSPy + ReAct) FTDRA

**Versão:** 2.2 *(Reflete estratégia Híbrida FT+DSPy+ReAct)*
**Data:** 03/04/2025

## 1. Introdução

### 1.1. Propósito
Este documento especifica os requisitos funcionais e não funcionais para a Plataforma SaaS de Marketing baseada em Agentes de IA, implementada como um **Monólito Modular**. A plataforma automatiza o ciclo de vida dos dados de marketing, utilizando uma **estratégia de IA avançada e híbrida**, combinando **modelos Gemini fine-tuned** (especialização), **DSPy** (otimização da interação) e o paradigma **ReAct** (raciocínio dinâmico e ação adaptativa) para máxima inteligência e autonomia dos agentes.

### 1.2. Escopo
O sistema integrará dados (GMP completo, Meta, CRMs), fornecerá lakehouse versionado (Nessie/Iceberg/MinIO), catálogo (ODD), MLOps (MLflow para features, modelos ML, LLMs FT, configs/métricas DSPy), motor de otimização cross-channel (**Seidr**), observabilidade (Heimdallr/logfire), visualização (Viz), governança (Forseti) e segurança (Cerberus/Nemo). Inclui pipelines para **fine-tuning contínuo** e **otimização via DSPy**, com agentes chave empregando **ReAct** para tarefas complexas. Será uma solução SaaS multi-tenant.

### 1.3. Definições, Acrônimos e Abreviações
* **GMP:** Google Marketing Platform
* **SA360:** Search Ads 360
* **GTM:** Google Tag Manager
* **GA4:** Google Analytics 4
* **CM360:** Campaign Manager 360
* **DV360:** Display & Video 360
* **ODD:** OpenDataDiscovery
* **Nessie:** Project Nessie (Versionamento para Lakehouse)
* **MLflow:** Plataforma MLOps (usada para Feature/Model Tracking)
* **Odin, Artemis, Bifrost, Forseti, Celebrimbor, Hygieia, Seidr, Heimdallr, Cerberus:** Nomes dos agentes de IA internos.
* **HITL:** Human-in-the-Loop (Processo de aprovação humana)
* **Monólito Modular:** Arquitetura de aplicação única com forte separação lógica interna por módulos/agentes.
* **LangChain, LangGraph, DSPy:** Frameworks de IA/LLM.
* **Iceberg:** Formato de tabela Apache Iceberg.
* **MinIO:** Armazenamento de objetos S3-compatível.
* **OpenSPG:** Padrão/conceito para Knowledge Graphs semânticos.
* **Qdrant:** Banco de dados vetorial.
* **Logfire:** Ferramenta de Observabilidade para aplicações LLM.
* **OTel:** OpenTelemetry (Padrão de telemetria).
* **Nemo Guardrails:** Framework NVIDIA para guardrails de IA.
* **Colang:** Linguagem de configuração do Nemo Guardrails.
* **LGPD:** Lei Geral de Proteção de Dados (Brasil).
* **Viz:** Módulo de Visualização interno.
* **SVG:** Scalable Vector Graphics (formato de imagem para gráficos).
* **Graphviz:** Software de visualização de grafos.
* **NetworkX, Matplotlib, Plotly, UMAP, Scikit-learn:** Bibliotecas Python para grafos e visualização.
* **CLI:** Command Line Interface.
* **API:** Application Programming Interface
* **CRM:** Customer Relationship Management
* **ETL/ELT:** Extract, Transform, Load / Extract, Load, Transform
* **ML:** Machine Learning
* **OR:** Operational Research (Pesquisa Operacional)
* **DDL:** Data Definition Language
* **IaC:** Infrastructure as Code
* **Terraform:** Ferramenta de IaC para provisionamento de infraestrutura.
* **Helm:** Gerenciador de pacotes para Kubernetes.
* **CI/CD:** Continuous Integration / Continuous Deployment
* **SLO:** Service Level Objective
* **MTTR:** Mean Time To Repair
* **MTBF:** Mean Time Between Failures
* **ReAct (Reason+Act):** Paradigma onde o LLM intercala passos de raciocínio explícito ("Thought") com ações ("Action" - uso de ferramentas) e observações para resolver tarefas complexas de forma dinâmica.
* **Agent Executor (LangChain):** Componente LangChain que implementa loops de agente como ReAct para orquestrar LLM e Tools.
* **(Atualizar LangGraph):** Framework para orquestrar agentes/módulos; nós individuais podem encapsular lógica complexa, incluindo Agent Executors rodando ReAct.

### 1.4. Tecnologias de Referência e Websites Principais

Esta seção lista as principais tecnologias e ferramentas utilizadas no projeto e seus respectivos sites de referência ou documentação primária:

* **Linguagem & Core:**
    * Python: [https://www.python.org/](https://www.python.org/)
    * Docker: [https://www.docker.com/](https://www.docker.com/)
    * Kubernetes: [https://kubernetes.io/](https://kubernetes.io/) (Implantação via GKE: [https://cloud.google.com/kubernetes-engine](https://cloud.google.com/kubernetes-engine))
    * Git: [https://git-scm.com/](https://git-scm.com/)
* **IA & Agentes:**
    * Gemini (Google AI): [https://ai.google.dev/](https://ai.google.dev/) ou [https://developers.google.com/gemini](https://developers.google.com/gemini)
    * DSPy: [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
    * LangChain: [https://python.langchain.com/](https://python.langchain.com/)
    * LangGraph: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
* **Lakehouse & Dados:**
    * MinIO: [https://min.io/](https://min.io/)
    * Apache Iceberg: [https://iceberg.apache.org/](https://iceberg.apache.org/)
    * Project Nessie: [https://projectnessie.org/](https://projectnessie.org/)
    * Apache Spark: [https://spark.apache.org/](https://spark.apache.org/)
    * DBT (Data Build Tool): [https://www.getdbt.com/](https://www.getdbt.com/)
* **Metadados, Grafos & Vetores:**
    * OpenSPG (Standard/Concept): [https://github.com/OpenSPG/openspg](https://github.com/OpenSPG/openspg) ou [https://spg.openkg.cn/](https://spg.openkg.cn/)
    * Qdrant: [https://qdrant.tech/](https://qdrant.tech/)
    * OpenDataDiscovery (ODD): [https://opendatadiscovery.org/](https://opendatadiscovery.org/)
* **MLOps & Otimização:**
    * MLflow: [https://mlflow.org/](https://mlflow.org/)
    * SciPy: [https://scipy.org/](https://scipy.org/)
    * Google OR-Tools: [https://developers.google.com/optimization](https://developers.google.com/optimization)
* **Observabilidade & Qualidade:**
    * Logfire: [https://logfire.pydantic.dev/](https://logfire.pydantic.dev/)
    * OpenTelemetry (OTel): [https://opentelemetry.io/](https://opentelemetry.io/)
    * Great Expectations: [https://greatexpectations.io/](https://greatexpectations.io/)
* **Guardrails & Segurança:**
    * NVIDIA Nemo Guardrails: [https://github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
* **Visualização:**
    * Graphviz: [https://graphviz.org/](https://graphviz.org/)
    * NetworkX: [https://networkx.org/](https://networkx.org/)
    * Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
    * Plotly: [https://plotly.com/python/](https://plotly.com/python/)
    * UMAP: [https://umap-learn.readthedocs.io/](https://umap-learn.readthedocs.io/)
    * Scikit-learn (para t-SNE): [https://scikit-learn.org/](https://scikit-learn.org/)
* **Infraestrutura & Deploy:**
    * Terraform: [https://www.terraform.io/](https://www.terraform.io/)
    * Helm: [https://helm.sh/](https://helm.sh/)
* **APIs Externas Principais (Exemplos):**
    * Google Ads API: [https://developers.google.com/google-ads/api/](https://developers.google.com/google-ads/api/)
    * Google Analytics Data API (GA4): [https://developers.google.com/analytics/devguides/reporting/data/v1](https://developers.google.com/analytics/devguides/reporting/data/v1)
    * Search Ads 360 API: [https://developers.google.com/search-ads/v2/reference/rpc](https://developers.google.com/search-ads/v2/reference/rpc)
    * Google Tag Manager API: [https://developers.google.com/tag-platform/tag-manager/api/v2](https://developers.google.com/tag-platform/tag-manager/api/v2)
    * Display & Video 360 API: [https://developers.google.com/display-video/api/](https://developers.google.com/display-video/api/)
    * Campaign Manager 360 API: [https://developers.google.com/campaign-manager/api/](https://developers.google.com/campaign-manager/api/)
    * Meta Marketing API: [https://developers.facebook.com/docs/marketing-apis/](https://developers.facebook.com/docs/marketing-apis/)
    * Salesforce APIs: [https://developer.salesforce.com/docs/](https://developer.salesforce.com/docs/)
    * HubSpot API: [https://developers.hubspot.com/](https://developers.hubspot.com/)
* **Ferramentas de Desenvolvimento Python:**
    * Pytest: [https://docs.pytest.org/](https://docs.pytest.org/)
    * Black Formatter: [https://github.com/psf/black](https://github.com/psf/black)
    * Ruff Linter: [https://astral.sh/ruff](https://astral.sh/ruff)
    * Mypy Type Checker: [https://mypy-lang.org/](https://mypy-lang.org/)
    * Typer (CLI): [https://typer.tiangolo.com/](https://typer.tiangolo.com/)
* **ReAct (Conceito/Frameworks):**
    * Paper Original (Exemplo): [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
    * LangChain Agent Executors: [https://python.langchain.com/docs/modules/agents/agent_executors/](https://python.langchain.com/docs/modules/agents/agent_executors/)

### 1.5. Referências Adicionais
* **[DOC-ARQ-001]** Descrição Detalhada da Arquitetura da Plataforma v6 (Este Documento ou Link Interno para Wiki/Repo) 
* **[DOC-API-GMP]** Guia Interno de Integração com APIs Google Marketing Platform (Autenticação, Padrões, Erros Comuns) 
* **[DOC-API-META]** Guia Interno de Integração com Meta Marketing API 
* **[DOC-API-PLAT]** Especificação OpenAPI para APIs da Plataforma (Se Aplicável - Futuro) 
* **[DOC-DESIGN-SEIDR]** Documento de Design Detalhado: Modelo de Otimização Seidr (Modelos ML, OR, Atribuição) 
* **[DOC-DESIGN-FORSETI]** Documento de Design Detalhado: Governança e Ciclo de Vida Nessie/ODD/MLflow 
* **[DOC-MLOPS-FT]** Estratégia e Processo de Fine-tuning Contínuo de LLMs
* **[DOC-MLOPS-DSPY]** Estratégia e Processo de Otimização de Programas DSPy
* **[DOC-SEC-POL]** Políticas de Segurança da Informação e Privacidade de Dados (Incluindo diretrizes LGPD) 
* **[DOC-CODING-STD]** Guia de Estilo e Padrões de Codificação Python do Projeto 
* **[DOC-INFRA-SETUP]** Guia de Setup do Ambiente de Desenvolvimento (Detalhes sobre Terraform/Docker Compose)

### 1.6. Visão Geral
Detalhamento do produto, requisitos (incluindo FT, DSPy, ReAct), interfaces.

## 2. Descrição Geral

### 2.1. Perspectiva do Produto
Plataforma SaaS inovadora usando IA em arquitetura de agentes modulares, com performance maximizada (FT+DSPy) e **capacidade de resolução de problemas complexos através de raciocínio dinâmico (ReAct)**.

### 2.2. Funções Principais do Produto (Realizadas pelos Agentes/Módulos)
* Ingestão de dados (Bifrost).
* Descoberta e catalogação (Artemis - *FT+DSPy, ReAct opcional*).
* Processamento ETL/ELT versionado (Celebrimbor).
* Validação de qualidade e rastreamento (Hygieia - *FT/base+DSPy opcional, ReAct opcional*).
* Governança por Contratos de Dados (Forseti - *FT+DSPy, ReAct para validação/resolução complexa*).
* Gestão de Features e Modelos (ML, LLM FT) e Configs DSPy (Forseti, MLflow).
* Modelagem de Atribuição e Predição ML (Seidr - *FT+DSPy, ReAct para análise*).
* Otimização Cross-Channel (Seidr - *FT+DSPy, ReAct para análise/planejamento*).
* **Raciocínio Dinâmico e Uso Adaptativo de Ferramentas (ReAct):** Capacidade de agentes chave (Seidr, Forseti, Heimdallr) de decompor tarefas, buscar informações iterativamente usando `Tools` e adaptar seu plano com base em observações.
* Ativação Automatizada via APIs (Seidr, Bifrost).
* **Visualização** (Módulo Viz).
* **Pipeline de Fine-tuning Contínuo**.
* **Processo de Otimização DSPy**.
* Monitoramento e Observabilidade (Heimdallr - *FT+DSPy, ReAct para diagnóstico*).
* Aplicação de Políticas/Guardrails (Cerberus, Nemo Guardrails).

### 2.3. Características do Usuário
* Administradores da Plataforma 
* Engenheiros de Dados 
* Analistas de Dados 
* Cientistas de Dados 
* Analistas de Marketing 
* Gestores de Marketing 
* Desenvolvedores/Engenheiros da Plataforma (MLOps, AI Engineers)

### 2.4. Restrições Gerais
* Dependência funcional/performance APIs externas. 
* Necessidade de infraestrutura cloud escalável (GKE). 
* Obrigatoriedade de conformidade com LGPD, GDPR, etc. 
* Adesão ao stack tecnológico definido. 
* Arquitetura monolítica modular (impacta deploy/escalabilidade). 
* **Provisionamento de Ambiente via IaC (Terraform) é mandatório** para dev/teste. 
* Geração de visualizações (Viz) pode exigir dependências/recursos adicionais. 
* **Dependência de Plataforma de Fine-tuning (Google Cloud AI Platform)**. 
* **Necessidade de Dados de Treino (Fine-tuning e DSPy)** de alta qualidade. 
* **Complexidade MLOps Aumentada (Fine-tuning + DSPy)**.
* **Complexidade da IA:** A combinação de Fine-tuning, DSPy e ReAct representa o estado da arte, mas também o pico de complexidade em desenvolvimento, MLOps e debugging.

### 2.5. Suposições e Dependências
* APIs externas estáveis. 
* Acesso programático às contas de clientes. 
* Infraestrutura cloud gerenciada. 
* Recursos computacionais suficientes (ETL, ML, OR, Fine-tuning, DSPy opt). 
* Disponibilidade de ferramentas IaC e permissões. 
* Capacidade de instalar dependências de sistema (Graphviz). 
* **`Tools` LangChain bem definidas para uso em ReAct.** 
* **Latência ReAct aceitável para os casos de uso.** 
* **Processo para gerar/coletar dados de treino FT/DSPy.**

## 3. Requisitos Específicos

### 3.1. Requisitos de Interface Externa
* **UI Web:** Dashboards (dados, status agentes, modelos FT/DSPy, otimizações Seidr, qualidade Hygieia), gestão contratos (Forseti), aprovações HITL (Cerberus), config fontes. Opcional: exibir Viz, rastros ReAct. Pode incluir visualização do *rastro de pensamento* (thought process) de execuções ReAct para depuração ou auditoria.
* **APIs da Plataforma:** (Opcional/Futuro) APIs seguras/versionadas para consumo externo.
* **CLI (Módulo Viz)**: ** (Recomendado) Disparar geração de SVGs (LangGraph, OpenSPG, Qdrant)
* **Integração APIs Externas (Módulo Bifrost):** Suportar autenticação, paginação, erros, rate limits (GMP completo, Meta, CRMs). Extrair dados definidos. Executar ativações de Seidr (budget, target, audience).
* **Integração Ferramentas Internas:** ODD (registro/sync via Forseti), MLflow (ciclo vida features, modelos ML, LLMs FT, configs/métricas DSPy via Forseti/Seidr), Nessie (operações via Forseti/Celebrimbor), Nemo Guardrails (interceptação via LangGraph, execução Actions via Cerberus), Google Cloud AI Platform (submissão jobs FT).

### 3.2. Requisitos Funcionais (por Módulo/Agente - Foco nas Mudanças IA)

* **Odin (Supervisor):** 
	* RF-ODN-01: Consumir eventos (Pub/Sub, Agendador) async. 
	* RF-ODN-02: Iniciar/orquestrar fluxos LangGraph internos (`src/agents/graph.py`). 
	* RF-ODN-03: Passar parâmetros (data, cliente, ref Nessie) aos fluxos. 
	* RF-ODN-04: Monitorar estado básico (sucesso/falha) e logar (Logfire). 
	* RF-ODN-05: Suportar modos `dry-run`/`staging` (branches Nessie). 
	* RF-ODN-06: Orquestrar/disparar **pipeline de fine-tuning contínuo**. 
	* RF-ODN-07: Orquestrar/disparar **processo de otimização DSPy**.

* **Artemis (Descoberta):**
    * RF-ART-01: Ler amostras (Landing Zone/Nessie). 
    * RF-ART-02: Usar **modelo Gemini fine-tuned + programa DSPy otimizado** para inferir esquema, tipos, PIIs. 
    * RF-ART-03: Consultar OpenSPG/Qdrant para entidades similares. 
    * RF-ART-04: **Propor** metadados para validação por Forseti. 
    * RF-ART-05: **PODE** implementar loop **ReAct** interno para inferências complexas.

* **Bifrost (Integração):**
	 * RF-BIF-01: Implementar `Tools` para cada API externa do escopo. 
	 * RF-BIF-02: Extrair dados detalhados. 
	 * RF-BIF-03: Depositar dados brutos na Landing Zone (MinIO). 
	 * RF-BIF-04: Implementar `Tools` seguras para ativações GMP. 
	 * RF-BIF-05: Tratar erros API, retentativas, rate limits. 
	 * RF-BIF-06: Gerenciar autenticação segura. 
	 * RF-BIF-07: `Tools` **PODEM** usar mini-loops ReAct internos para interações API complexas.

* **Forseti (Contrato de Dados):**
	* RF-FOR-01: Gerenciar Contratos de Dados (OpenSPG). 
	* RF-FOR-02: Usar **modelo Gemini fine-tuned + programa DSPy otimizado** para validar dados contra contratos. 
	* RF-FOR-03: Interagir com Nessie (`nessie_manager.py`) para DDL, branches, tags, merges (via Cerberus/HITL). 
	* RF-FOR-04: Registrar/atualizar ativos no ODD (`odd_updater.py`) com **ref Nessie**. 
	* RF-FOR-05: Registrar/atualizar features, modelos ML e **modelos LLM FT / configs DSPy** no MLflow (`mlflow_registrar.py`) com **refs Nessie**. 
	* RF-FOR-06: Detectar schema drift e iniciar fluxo de resolução (pode usar ReAct). 
	* RF-FOR-07: Analisar métricas (Heimdallr) e propor/executar otimizações DDL (via Cerberus/HITL). 
	* RF-FOR-09: Para validação de contratos complexos ou resolução de drift multi-etapas, **DEVE** implementar **ReAct** (via AgentExecutor). 
	* RF-FOR-10: `Tools` devem ter descrições claras para ReAct.

* **Celebrimbor (ETL/ELT):** 
	* RF-CEL-01: Ler dados brutos (Landing Zone). 
	* RF-CEL-02: Executar transformações (Spark/dbt) usando catálogo Nessie. 
	* RF-CEL-03: Commitar atomicamente em branch Nessie. 
	* RF-CEL-04: Execução verificada por Cerberus. (Pode usar LLM base+DSPy para gerar jobs).

* **Hygieia (Qualidade de Dados):**
    * RF-HYG-01: Executar testes DQ (GE) sobre refs Nessie. 
    * RF-HYG-02: Auditar config GTM (via Bifrost). 
    * RF-HYG-03: Validar predições ML (pode usar LLM FT/base + DSPy). 
    * RF-HYG-04: Reportar resultados (com ref Nessie). 
    * RF-HYG-05: Propostas de correção validadas por Cerberus. 
    * RF-HYG-07: **PODE** implementar loop **ReAct** interno para diagnósticos complexos de DQ.

* **Seidr (Otimização):**
	* RF-SEI-01: Ler dados curados (Iceberg/Nessie). 
	* RF-SEI-02: Implementar/executar modelos de atribuição. 
	* RF-SEI-03: Interagir com MLflow para ciclo de vida ML (pCVR, pLTV, resposta). 
	* RF-SEI-04: Gerar previsões. 
	* RF-SEI-05: Formular/resolver problemas OR. 
	* RF-SEI-06: Gerar plano de ativação API. 
	* RF-SEI-07: Instruir Bifrost (via LangGraph), **após validação/aprovação HITL por Cerberus**. * RF-SEI-08: Escrever resultados (otimização, perf. atribuída) em Iceberg/Nessie. 
	* RF-SEI-09: Implementar ciclo de feedback/retreino. 
	* RF-SEI-10: O núcleo de análise, modelagem (exceto treino/solver), planejamento **DEVE** usar **ReAct** (via AgentExecutor) com **modelos Gemini fine-tuned e programas DSPy otimizados**. 
	* RF-SEI-11: `Tools` devem ter descrições claras para ReAct.

* **Heimdallr (Observabilidade):**
    * RF-HEI-01: Coletar/centralizar logs (Logfire) e métricas (OTel), incluindo pipelines FT/DSPy. 
    * RF-HEI-02: Monitorar saúde Nessie e Landing Zone. 
    * RF-HEI-03: Consultar OpenSPG para contexto linhagem/políticas (com refs Nessie). 
    * RF-HEI-04: Monitorar execução fluxos **Seidr**. 
    * RF-HEI-05: Monitorar performance modelos **ML e LLM FT**. 
    * RF-HEI-06: Correlacionar mudanças GTM com anomalias. 
    * RF-HEI-07: Gerar alertas configuráveis. 
    * RF-HEI-08: Fornecer dados de performance para Forseti. 
    * RF-HEI-09: Usar **modelo Gemini fine-tuned + programa DSPy otimizado** para análises proativas. 
    * RF-HEI-11: Para diagnósticos complexos, **DEVE** implementar **ReAct**.

* **Cerberus (Nemo Guardrails):** 
	* RF-CER-01: Implementado com Nemo Guardrails e regras Colang. 
	* RF-CER-02: Interceptar ações críticas (ativações **Seidr**, ops Nessie/DDL Forseti, exec código Celebrimbor). 
	* RF-CER-03: Executar Nemo Actions para buscar contexto. 
	* RF-CER-04: Aplicar políticas configuradas. 
	* RF-CER-05: Bloquear ações não conformes/arriscadas. 
	* RF-CER-06: Disparar e gerenciar fluxos HITL.

* **Módulo Viz:** 
	* RF-VIZ-01: Gerar SVG LangGraph. 
	* RF-VIZ-02: Gerar SVG subgrafo OpenSPG. 
	* RF-VIZ-03: Gerar SVG/HTML espaço vetorial Qdrant. 
	* RF-VIZ-04: Salvar SVGs em `output/visualizations/`. 
	* RF-VIZ-05: (Recomendado) Fornecer interface CLI.

* **Pipeline de Fine-tuning Contínuo:** 
	* *RF-FT-01: **Coleta de Dados:** Deve existir um mecanismo (automatizado ou via feedback HITL/UI) para coletar exemplos de alta qualidade (input/output desejado) das tarefas dos agentes que usarão fine-tuning (Forseti, Seidr, Artemis, Heimdallr). As fontes e o processo de coleta devem ser definidos. 
	* RF-FT-02: **Preparação de Dados:** Deve haver scripts (`fine_tuning/datasets/`) para limpar, formatar (ex: JSONL) e dividir os dados coletados em conjuntos de treino/validação/teste, conforme exigido pela API do Gemini. 
	* RF-FT-03: **Versionamento de Datasets:** Os datasets de treino/validação/teste DEVEM ser versionados (ex: usando MLflow Datasets ou tabelas Iceberg/Nessie dedicadas) para reprodutibilidade. 
	* RF-FT-04: **Gerenciamento de Jobs de Treino:** A plataforma deve ser capaz de submeter jobs de fine-tuning para a Google Cloud AI Platform via API/SDK, passando o dataset versionado correto e hiperparâmetros. Os runs de treino DEVEM ser rastreados no MLflow (experimentos, parâmetros, métricas). 
	* RF-FT-05: **Avaliação de Modelos:** Deve haver um processo e scripts (`fine_tuning/evaluation/`) para avaliar modelos recém-ajustados contra métricas objetivas (ex: loss, acurácia em tarefa específica, métricas de negócio simuladas) e benchmarks. 
	* RF-FT-06: **Registro e Deploy de Modelos:** Modelos aprovados na avaliação DEVEM ser registrados no MLflow. Deve haver um processo (controlado por Forseti/Odin e potencialmente HITL via Cerberus) para atualizar a configuração da aplicação (`src/settings.py`, ConfigMaps K8s) para que os agentes usem a nova versão do modelo fine-tuned. Estratégias de deploy seguro (ex: canary) devem ser consideradas. 
	* RF-FT-07: **Orquestração:** O pipeline completo (coleta a deploy) deve ser orquestrável (ex: via Odin, Airflow, Kubeflow Pipelines) e executado em cadência definida ou por gatilho.

* **Processo de Otimização DSPy:** 
	* * RF-DSPY-01: **Definição de Tarefa e Métrica:** Para cada tarefa de LLM otimizada via DSPy (nos agentes Seidr, Forseti, etc.), uma métrica de avaliação clara e computável DEVE ser definida. 
	* RF-DSPY-02: **Gerenciamento de Dados Treino/Dev:** O processo DSPy deve ter acesso a conjuntos de dados representativos (podem reusar/derivar dos datasets de fine-tuning) para o otimizador (ex: `BootstrapFewShotWithRandomSearch`) aprender exemplos few-shot ou otimizar a cadeia de raciocínio. 
	* RF-DSPY-03: **Execução de Otimizador:** Deve haver scripts ou processos (`scripts/run_dspy_optimization.sh`?) para executar os otimizadores DSPy para um dado programa (`src/processing/dspy_programs/` ou local do agente), métrica e dados. A execução pode ser computacionalmente intensiva. 
	* RF-DSPY-04: **Compilação e Versionamento:** O programa DSPy compilado/otimizado resultante (ex: estado JSON) DEVE ser versionado (ex: Git LFS, artefatos MLflow) e associado à versão do modelo LLM (base ou fine-tuned) para o qual foi otimizado. 
	* RF-DSPY-05: **Carregamento em Produção:** Os agentes relevantes DEVEM carregar e executar a versão aprovada do programa DSPy compilado (obtido do local versionado via configuração) para suas interações com o LLM. 
	* RF-DSPY-06: **Orquestração:** O ciclo de otimização DSPy (execução do otimizador, avaliação, versionamento do programa compilado, atualização da configuração) deve ser orquestrável (ex: via Odin, CI/CD, MLOps).

### 3.3. Requisitos Não Funcionais
* **Desempenho:**
    * RFN-DES-01: Latência de ingestão batch (ex: D-1) < X horas (SLO a definir). 
    * RFN-DES-02: Processamento ETL/ELT (Celebrimbor) < Y horas (SLO a definir). 
    * RFN-DES-03: Tempo de resposta p95 para consultas analíticas Iceberg < Z segundos (SLO a definir). 
    * RFN-DES-04: Ciclo de otimização **Seidr** (incluindo inferência ML/OR) < W horas/dias (SLO a definir, ex: diário). 
    * RFN-DES-05: Tempo de resposta p95 da UI e API da plataforma < V segundos (SLO a definir). 
    * RFN-DES-06: Latência introduzida pelos loops **ReAct** (múltiplas chamadas LLM) DEVE ser monitorada (Heimdallr) e mantida dentro dos SLOs aceitáveis para os fluxos impactados (Seidr, Forseti, etc.). Otimizações via **DSPy**, caching e **fine-tuning** devem ser consideradas para mitigar latência.
    * RFN-DES-07: Tempo de execução dos pipelines de **Fine-tuning** e **Otimização DSPy** deve ser monitorado e gerenciado.
* **Escalabilidade:**
	* RFN-ESC-01: Suportar aumento de X% no volume de dados/cliente sem violar SLOs de desempenho. 
	* RFN-ESC-02: Suportar adição de N fontes/cliente com configuração gerenciável. 
	* RFN-ESC-03: Suportar M clientes simultâneos (arquitetura multi-tenant). 
	* RFN-ESC-04: Aplicação monolítica deve escalar horizontalmente (ex: múltiplos pods do consumidor Odin). Recursos (CPU/Memória/GPU) para jobs intensivos (Celebrimbor, **Seidr ML/OR**, **FT Jobs**, **DSPy Optimization**) devem ser configuráveis e escaláveis (ex: node pools GKE dedicados). 
	* RFN-ESC-05: Serviços externos provisionados via IaC (Nessie, MinIO, Qdrant, etc.) devem ser configurados para escalabilidade apropriada.
	* RFN-ESC-06: Nós LangGraph que executam loops ReAct podem ser mais intensivos em LLM e exigir mais recursos ou instâncias.
* **Confiabilidade:**
    * RFN-CON-01: Disponibilidade alvo da plataforma: 99.9% (a definir). * RFN-CON-02: Implementar retentativas configuráveis com backoff exponencial para falhas transitórias em chamadas de API (Bifrost) e processamento (Celebrimbor). 
    * RFN-CON-03: **Rollback rápido e seguro para versões anteriores de dados e esquemas via Iceberg/Nessie é MANDATÓRIO** como principal mecanismo de recuperação de dados. Processo deve ser documentado e testado. 
    * RFN-CON-04: Falhas em um fluxo/agente devem ser isoladas e não corromper o estado global ou outros fluxos não relacionados (gerenciamento de estado LangGraph). 
    * RFN-CON-05: Definir e monitorar objetivos de MTTR (< A horas) e MTBF (> B dias). 
    * RFN-CON-06: Fluxos **ReAct** DEVEM implementar tratamento robusto de erros internos (falha de Tool, LLM não gera ação válida), logando o estado e potencialmente escalando para revisão manual (via Heimdallr/Odin). 
    * RFN-CON-07: Monitorar consistência entre versões de modelos **LLM fine-tuned** e os **programas DSPy** otimizados para eles. Ter estratégia de rollback para ambos. * RFN-CON-08: Pipelines de **Fine-tuning** e **Otimização DSPy** devem ser resilientes a falhas e permitir retomada ou re-execução segura.
    * RFN-CON-08: Pipelines de **Fine-tuning** e **Otimização DSPy** devem ser resilientes a falhas e permitir retomada ou re-execução segura.
* **Segurança:** 
	* RFN-SEG-01: Implementar Autenticação (ex: OAuth2/OIDC) e Autorização (RBAC) fortes para UI e APIs. 
	* RFN-SEG-02: Gestão de segredos (chaves API externas, senhas DB) via K8s Secrets / Google Secret Manager com acesso via Workload Identity. **NÃO** armazenar segredos em código ou config files. 
	* RFN-SEG-03: Criptografia de dados em repouso (MinIO, DBs, etc.) e em trânsito (TLS 1.2+). 
	* RFN-SEG-04: Garantir isolamento de dados lógico (e opcionalmente físico) entre tenants. * RFN-SEG-05: Implementar funcionalidades e seguir práticas para auxiliar na conformidade com **LGPD** (gestão de consentimento, direitos do titular, anonimização/pseudonimização onde aplicável, relatório de impacto). Políticas definidas no OpenSPG. 
	* RFN-SEG-06: Auditoria completa de acessos e ações críticas (login, alteração de contrato, DDL, ativação de budget, acesso a dados sensíveis), logs gerenciados por Heimdallr. 
	* RFN-SEG-07: Aplicação **MANDATÓRIA** de políticas via **Cerberus (Nemo Guardrails)** para ações críticas, incluindo checagens de segurança, conformidade e limites operacionais. 
	* RFN-SEG-08: Módulo Viz (se exposto via API) deve ter controle de acesso. Dados sensíveis (PII) não devem ser expostos em visualizações gerais. 
	* RFN-SEG-09: Proteger o pipeline de **Fine-tuning** e os **datasets de treino** contra acesso não autorizado e garantir conformidade com LGPD.
	* RFN-SEG-10: Ações (`Action`) dentro de loops ReAct ainda devem passar por Cerberus se forem críticas.
* **Manutenibilidade:**
    * RFN-MAN-01: Aderência estrita aos padrões de código (Black, Ruff, Mypy) definidos em `pyproject.toml`. 
    * RFN-MAN-02: Código **altamente modular** dentro da estrutura `src/` (agentes, storage, processing, etc.). Baixo acoplamento, alta coesão. 
    * RFN-MAN-03: Cobertura de testes (unitários e integração com `pytest-asyncio`) > X% (a definir, ex: 80%). Testes específicos para lógica ReAct, FT e DSPy. 
    * RFN-MAN-04: **Infraestrutura gerenciada via IaC (Terraform)** em `infra/terraform/` para garantir ambientes reprodutíveis. 
    * RFN-MAN-05: Pipeline CI/CD automatizado (build, test, scan de segurança, deploy em K8s). 
    * RFN-MAN-06: Documentação abrangente (README principal, READMEs por módulo/agente, docstrings Google Style, documentos de arquitetura/design referenciados). 
    * RFN-MAN-07: **Logging estruturado e tracing distribuído (Logfire)** são essenciais para depuração, especialmente dos fluxos complexos de ReAct e inter-agentes. 
    * RFN-MAN-08: Ambientes dev/teste **facilmente reprodutíveis** via IaC. 
    * RFN-MAN-09: Gerenciar a **complexidade dos pipelines FT/DSPy e dos fluxos ReAct** com clareza, documentação e MLOps robusto. Versionamento claro de código, dados (Nessie), modelos (MLflow) e configurações (Git, ConfigMaps).
* **Custo:**
    * RFN-CST-01: Monitorar e otimizar custos de infraestrutura cloud (GKE, MinIO, DBs, etc.) e APIs externas (se aplicável). 
    * RFN-CST-02: Monitorar e otimizar custos de inferência LLM (Gemini base e fine-tuned). Avaliar impacto de **ReAct** (mais chamadas) vs **FT/DSPy** (potencialmente menos tokens/chamada). Implementar caching onde aplicável. 
    * RFN-CST-03: Monitorar e otimizar custos dos **jobs de fine-tuning** na Google Cloud AI Platform. 
    * RFN-CST-04: Monitorar e otimizar custos de computação para **otimização DSPy** (se intensivo). 
    * RFN-CST-05: Monitorar custos de ferramentas de terceiros (ODD, Qdrant, etc., se não forem self-hosted ou usarem serviços cloud).
    * RFN-CST-06: O número aumentado de chamadas LLM devido aos loops ReAct deve ser monitorado e otimizado para controlar custos (uso de modelos fine-tuned menores, otimização DSPy, caching).
* **Usabilidade:** 
	* RFN-USA-01: UI deve ser intuitiva para tarefas chave de cada perfil de usuário. 
	* RFN-USA-02: Mensagens de erro claras e acionáveis. 
	* RFN-USA-03: Processo de **aprovação HITL via Cerberus** deve ser eficiente, claro e fornecer contexto suficiente para a tomada de decisão do gestor. 
	* RFN-USA-04: CLI do Módulo Viz deve ser clara e fácil de usar para desenvolvedores.

## 4. Outros Requisitos
	** Licenciamento:** Garantir conformidade das licenças de todas as bibliotecas (Python, JS), ferramentas (Nessie, ODD, etc.) e software base (Docker, K8s). *
	 **Conformidade Legal/Regulatória:** Aderência estrita à **LGPD** e outras regulações de privacidade e segurança de dados relevantes para os clientes e a operação da plataforma.

