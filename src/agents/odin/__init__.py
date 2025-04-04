"""
Módulo do agente Odin - Supervisor e Orquestrador Principal

Este módulo implementa o agente Odin, responsável por:
- Consumir eventos (Pub/Sub, Agendador) de forma assíncrona
- Iniciar e orquestrar fluxos LangGraph internos
- Passar parâmetros para os fluxos
- Monitorar estado básico e logging
- Suportar modos dry-run/staging
- Orquestrar pipelines de fine-tuning e otimização DSPy
"""

from .nodes import (
    consume_events,
    orchestrate_flow,
    monitor_state,
    handle_dry_run,
    orchestrate_fine_tuning,
    orchestrate_dspy_optimization
)

__all__ = [
    'consume_events',
    'orchestrate_flow',
    'monitor_state',
    'handle_dry_run',
    'orchestrate_fine_tuning',
    'orchestrate_dspy_optimization'
] 