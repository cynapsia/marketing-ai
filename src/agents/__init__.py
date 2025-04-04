"""
Pacote principal dos agentes

Este pacote contém todos os agentes e componentes relacionados à orquestração
do sistema de marketing com IA.
"""

from .state import AgentState
from .graph import workflow_graph

# Importar e exportar os agentes
from .odin import (
    consume_events,
    orchestrate_flow,
    monitor_state,
    handle_dry_run,
    orchestrate_fine_tuning,
    orchestrate_dspy_optimization
)

__all__ = [
    'AgentState',
    'workflow_graph',
    'consume_events',
    'orchestrate_flow',
    'monitor_state',
    'handle_dry_run',
    'orchestrate_fine_tuning',
    'orchestrate_dspy_optimization'
] 