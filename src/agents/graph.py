"""
Definição do grafo principal do LangGraph

Este módulo define o grafo principal de orquestração dos agentes,
utilizando o LangGraph para gerenciar o fluxo de trabalho.
"""

from typing import Dict, Any, Type
from langgraph.graph import Graph, StateGraph
from langgraph.prebuilt import ToolExecutor
from .state import AgentState
from .odin.nodes import (
    consume_events,
    orchestrate_flow,
    monitor_state,
    handle_dry_run,
    orchestrate_fine_tuning,
    orchestrate_dspy_optimization
)

def create_workflow_graph() -> Graph:
    """
    Cria o grafo principal de workflow do sistema.
    
    Returns:
        Graph: Grafo LangGraph configurado
    """
    # Criar o grafo de estado
    workflow = StateGraph(AgentState)
    
    # Adicionar nós ao grafo
    workflow.add_node("consume_events", consume_events)
    workflow.add_node("orchestrate_flow", orchestrate_flow)
    workflow.add_node("monitor_state", monitor_state)
    workflow.add_node("handle_dry_run", handle_dry_run)
    workflow.add_node("orchestrate_fine_tuning", orchestrate_fine_tuning)
    workflow.add_node("orchestrate_dspy_optimization", orchestrate_dspy_optimization)
    
    # Definir as arestas do grafo
    workflow.add_edge("consume_events", "orchestrate_flow")
    workflow.add_edge("orchestrate_flow", "monitor_state")
    workflow.add_conditional_edges(
        "monitor_state",
        lambda x: "handle_dry_run" if x.get("is_dry_run", False) else "orchestrate_flow"
    )
    workflow.add_edge("handle_dry_run", "orchestrate_flow")
    
    # Adicionar nós opcionais para fine-tuning e DSPy
    workflow.add_conditional_edges(
        "orchestrate_flow",
        lambda x: "orchestrate_fine_tuning" if x.get("needs_fine_tuning", False) else "orchestrate_dspy_optimization"
    )
    
    # Definir o ponto de entrada
    workflow.set_entry_point("consume_events")
    
    # Compilar o grafo
    return workflow.compile()

# Instância global do grafo
workflow_graph = create_workflow_graph() 