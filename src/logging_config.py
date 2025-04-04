"""
Configuração de logging da aplicação

Este módulo configura o sistema de logging da aplicação,
utilizando o Logfire para logging estruturado e tracing distribuído.
"""

import logging
import sys
from logfire import LogfireHandler
from .settings import settings

def setup_logging():
    """
    Configura o sistema de logging da aplicação.
    """
    # Criar logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Configurar handler do Logfire
    logfire_handler = LogfireHandler(
        level=logging.INFO,
        service_name="marketing_ai_platform",
        environment=settings.environment
    )
    
    # Configurar formato do log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logfire_handler.setFormatter(formatter)
    
    # Adicionar handler ao logger raiz
    root_logger.addHandler(logfire_handler)
    
    # Configurar handler para console em modo debug
    if settings.debug:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
    
    # Configurar loggers específicos
    logging.getLogger("langchain").setLevel(logging.WARNING)
    logging.getLogger("langgraph").setLevel(logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    
    return root_logger

# Configurar logging ao importar o módulo
logger = setup_logging() 