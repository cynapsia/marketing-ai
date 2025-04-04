"""
Ponto de entrada da aplicação

Este módulo serve como ponto de entrada principal da aplicação,
configurando e iniciando o sistema de agentes de marketing com IA.
"""

import asyncio
import logging
import os
import sys
from typing import Optional, Dict, Any

from logfire import setup_logging
from logfire.context import context

from .agents import workflow_graph, AgentState
from .settings import get_settings
from .agents.cerberus import initialize_cerberus, validate_environment

# Configurar logging
setup_logging()
logger = logging.getLogger(__name__)

async def initialize_application() -> bool:
    """
    Inicializa componentes críticos da aplicação.
    
    Returns:
        bool: True se a inicialização foi bem-sucedida, False caso contrário
    """
    try:
        # Carregar configurações
        settings = get_settings()
        
        # Validar ambiente
        if not validate_environment():
            logger.error("Falha na validação do ambiente")
            return False
            
        # Inicializar Cerberus (Nemo Guardrails)
        if not initialize_cerberus():
            logger.error("Falha na inicialização do Cerberus")
            return False
            
        logger.info("Aplicação inicializada com sucesso")
        return True
        
    except Exception as e:
        logger.error(f"Erro na inicialização da aplicação: {str(e)}")
        return False

async def main(tenant_id: Optional[str] = None, flow_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Função principal que inicia a aplicação.
    
    Args:
        tenant_id: ID do tenant (opcional, usa valor padrão se não fornecido)
        flow_id: ID do fluxo (opcional, usa valor padrão se não fornecido)
        
    Returns:
        Dict[str, Any]: Resultado da execução do workflow
        
    Raises:
        RuntimeError: Se a inicialização falhar
        Exception: Para outros erros durante a execução
    """
    # Configurar contexto de logging
    with context(tenant_id=tenant_id or "default"):
        try:
            logger.info("Iniciando aplicação de marketing com IA")
            
            # Inicializar componentes críticos
            if not await initialize_application():
                raise RuntimeError("Falha na inicialização da aplicação")
            
            # Criar estado inicial
            initial_state = AgentState(
                tenant_id=tenant_id or "default",
                flow_id=flow_id or "initial_flow"
            )
            
            # Executar o grafo de workflow
            result = await workflow_graph.arun(initial_state)
            
            logger.info("Aplicação finalizada com sucesso")
            return result
            
        except Exception as e:
            logger.error(f"Erro na execução da aplicação: {str(e)}", exc_info=True)
            raise

def run_cli():
    """
    Função para execução via linha de comando.
    """
    try:
        # Verificar argumentos da linha de comando
        tenant_id = None
        flow_id = None
        
        if len(sys.argv) > 1:
            tenant_id = sys.argv[1]
        if len(sys.argv) > 2:
            flow_id = sys.argv[2]
            
        # Executar aplicação
        result = asyncio.run(main(tenant_id, flow_id))
        print(f"Resultado: {result}")
        
    except Exception as e:
        print(f"Erro: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 
    run_cli() 