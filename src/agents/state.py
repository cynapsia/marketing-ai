"""
Definição do estado compartilhado entre os agentes

Este módulo define a estrutura de estado compartilhada entre todos os agentes
do sistema, usando Pydantic para validação e serialização.
"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class AgentState(BaseModel):
    """
    Estado compartilhado entre os agentes do sistema.
    
    Este estado é passado entre os nós do LangGraph e contém informações
    relevantes para a execução do fluxo de trabalho.
    """
    
    # Identificação
    tenant_id: str = Field(..., description="ID do tenant atual")
    flow_id: str = Field(..., description="ID do fluxo atual")
    timestamp: datetime = Field(default_factory=datetime.now)
    
    # Configuração
    is_dry_run: bool = Field(default=False, description="Indica se está em modo dry-run")
    nessie_ref: Optional[str] = Field(None, description="Referência do Nessie para o fluxo")
    
    # Dados do fluxo
    event_data: Dict[str, Any] = Field(default_factory=dict)
    intermediate_results: Dict[str, Any] = Field(default_factory=dict)
    errors: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Metadados
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True 