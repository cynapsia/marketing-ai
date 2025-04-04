# Plataforma de Marketing com Agentes de IA

Uma plataforma SaaS inovadora que utiliza agentes de IA para automatizar e otimizar processos de marketing, implementada como um monólito modular com arquitetura de 9 agentes.

## Visão Geral

A plataforma combina tecnologias avançadas de IA (Gemini Fine-tuning + DSPy + ReAct) com uma arquitetura robusta de agentes para fornecer:

- Ingestão e processamento de dados de marketing
- Descoberta e catalogação automática
- Validação de qualidade e governança
- Modelagem de atribuição e predição
- Otimização cross-channel
- Visualização e análise
- Observabilidade e monitoramento
- Segurança e conformidade

## Arquitetura

A plataforma é composta por 9 agentes principais:

1. **Odin**: Supervisor e orquestrador principal
2. **Artemis**: Descoberta e inferência de esquemas
3. **Bifrost**: Integração com APIs externas
4. **Forseti**: Governança e contratos de dados
5. **Celebrimbor**: Processamento ETL/ELT
6. **Hygieia**: Qualidade e validação
7. **Seidr**: Otimização e modelagem
8. **Heimdallr**: Observabilidade e monitoramento
9. **Cerberus**: Segurança e guardrails

## Tecnologias Principais

- **IA & Agentes**: LangChain, LangGraph, DSPy, Gemini
- **Armazenamento**: MinIO, Iceberg, Nessie, Qdrant
- **MLOps**: MLflow
- **Observabilidade**: Logfire
- **Segurança**: Nemo Guardrails
- **Visualização**: Graphviz, NetworkX, Plotly

## Requisitos

- Python 3.9+
- Docker
- Kubernetes (GKE)
- Terraform

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/marketing-ai-platform.git
cd marketing-ai-platform
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Para desenvolvimento
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Inicialize a infraestrutura com Terraform:
```bash
cd infra/terraform
terraform init
terraform apply
```

## Uso

Para executar a aplicação:

```bash
python -m src.main
```

Para desenvolvimento:

```bash
# Formatação e linting
black src tests
ruff check src tests
mypy src

# Testes
pytest
```

## Estrutura do Projeto

```
plataforma_marketing_ia/
├── config/               # Configurações
├── fine_tuning/         # Pipeline de fine-tuning
├── infra/               # Infraestrutura (Terraform)
├── scripts/             # Scripts utilitários
├── src/                 # Código fonte
│   ├── agents/          # Agentes de IA
│   ├── core/            # Componentes core
│   ├── processing/      # Processamento
│   ├── storage/         # Armazenamento
│   ├── streaming/       # Streaming
│   ├── validation/      # Validação
│   ├── utils/           # Utilitários
│   └── viz/             # Visualização
├── notebooks/           # Notebooks de análise
├── output/              # Saídas (git-ignored)
└── tests/               # Testes
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Equipe de Desenvolvimento - dev@example.com

Link do Projeto: [https://github.com/seu-usuario/marketing-ai-platform](https://github.com/seu-usuario/marketing-ai-platform)
