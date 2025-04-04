"""
Configurações da aplicação

Este módulo gerencia as configurações da aplicação, carregando-as
de arquivos YAML e variáveis de ambiente.
"""

import os
from typing import Dict, Any
import yaml
from pydantic import BaseModel, Field

class Settings(BaseModel):
    """
    Configurações da aplicação.
    
    Esta classe define todas as configurações necessárias para o funcionamento
    da aplicação, incluindo endpoints, chaves, e outros parâmetros.
    """
    
    # Configurações gerais
    environment: str = Field(default="development", description="Ambiente de execução")
    debug: bool = Field(default=False, description="Modo debug")
    
    # Configurações de API
    api_timeout: int = Field(default=30, description="Timeout para chamadas de API")
    api_retries: int = Field(default=3, description="Número de tentativas para chamadas de API")
    
    # Configurações de LLM
    gemini_model_id: str = Field(..., description="ID do modelo Gemini")
    gemini_api_key: str = Field(..., description="Chave da API do Gemini")
    
    # Configurações de armazenamento
    minio_endpoint: str = Field(..., description="Endpoint do MinIO")
    minio_access_key: str = Field(..., description="Chave de acesso do MinIO")
    minio_secret_key: str = Field(..., description="Chave secreta do MinIO")
    
    # Configurações de Nessie
    nessie_endpoint: str = Field(..., description="Endpoint do Nessie")
    nessie_branch: str = Field(default="main", description="Branch padrão do Nessie")
    
    # Configurações de MLflow
    mlflow_tracking_uri: str = Field(..., description="URI de tracking do MLflow")
    
    # Configurações de DSPy
    dspy_optimization_path: str = Field(..., description="Caminho para programas DSPy otimizados")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def load_settings() -> Settings:
    """
    Carrega as configurações do arquivo YAML e variáveis de ambiente.
    
    Returns:
        Settings: Objeto com as configurações carregadas
    """
    # Carregar configurações do arquivo YAML
    config_path = os.getenv("CONFIG_PATH", "config/settings.yaml")
    with open(config_path, "r") as f:
        yaml_config = yaml.safe_load(f)
    
    # Criar objeto de configurações
    settings = Settings(**yaml_config)
    
    return settings

# Instância global das configurações
settings = load_settings() 