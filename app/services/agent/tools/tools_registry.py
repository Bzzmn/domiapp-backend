"""
Registro central de herramientas disponibles para el agente.
Este módulo importa y expone todas las herramientas que pueden ser utilizadas en el grafo del agente.
"""

from app.services.agent.tools.date_time import get_current_datetime
from app.services.agent.tools.check_plan import check_plan
from app.services.agent.tools.check_om import check_om

agent_tools = [
    get_current_datetime,
    check_plan,
    check_om,
]