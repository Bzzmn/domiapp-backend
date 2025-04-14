"""This file was generated using `langgraph-gen` version 0.0.3.

This file provides a placeholder implementation for the corresponding stub.

Replace the placeholder implementation with your own logic.
"""

from typing_extensions import TypedDict, Annotated

from app.services.agent import tools
from app.services.agent.schemas.state import ProjectState
from app.services.agent.tools.tools_registry import agent_tools
from app.services.agent.stub import CustomAgent
from app.services.agent.nodes import (
    data_loader,
    cip_loader,
    should_end
)
from app.services.agent.prompts import get_formatted_prompt

from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver


llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0)
llm = llm.bind_tools(agent_tools)
llm = llm.bind(tool_choice="auto")

tools_node = ToolNode(tools=agent_tools)

# Define stand-alone functions
def investigador(state) -> dict:
    """
    Nodo de agente que usa un LLM para realizar la investigacion para la solicitud de permiso de edificacion.
    """ 
    print("In node: investigador")
    
    # Obtener la consulta del usuario del último mensaje HumanMessage
    user_query = ""
    if "messages" in state and len(state["messages"]) > 0:
        for message in reversed(state["messages"]):
            if hasattr(message, "type") and message.type == "human" or \
               (hasattr(message, "__class__") and message.__class__.__name__ == "HumanMessage"):
                user_query = message.content
                print(f"User query: {user_query}")
                break

    # Determinar el tipo de consulta y el ítem de acta correspondiente
    query_type = "Uso de Suelo"  # Valor por defecto
    
    if user_query:
        query_lower = user_query.lower()
        if "coeficiente" in query_lower or "constructibilidad" in query_lower:
            query_type = "Coeficiente de Constructibilidad"
        elif "estacionamiento" in query_lower:
            query_type = "Estacionamientos"
    
    print(f"Tipo de consulta detectado: {query_type}")

    # Obtener el prompt formateado según el tipo de consulta
    # Pasamos el CIP completo y dejamos que el módulo de prompts seleccione los campos relevantes
    formatted_prompt = get_formatted_prompt(query_type, state.get("cip_data", {}))
    system_message = SystemMessage(content=formatted_prompt)
    messages = [system_message] + state["messages"]

    print(f'Enviando mensajes al LLM...')

    response = llm.invoke(messages)

    print(f'Respuesta recibida del LLM')

    if not isinstance(response, AIMessage):
        # Si no es un AIMessage, convertirlo
        if hasattr(response, "content"):
            response = AIMessage(content=response.content)
        else:
            response = AIMessage(content=str(response))
    
    # Extraer la resolución del contenido de la respuesta
    resolucion = "No aplica"  # Valor por defecto
    
    if response.content:
        content = response.content.lower()
        if "resolución: cumple" in content:
            resolucion = "Cumple"
        elif "resolución: no cumple" in content:
            resolucion = "No Cumple"
    
    print(f"Resolución extraída: {resolucion}")
    
    # Devolver la respuesta, resolución y tipo de consulta
    return {
        "messages": [response],
        "resolucion_item": resolucion,
        "item_acta_observaciones": query_type
    }


    
agent = CustomAgent(
    state_schema=ProjectState,
    impl=[
        ("investigador", investigador),
        ("tools", tools_node),
        ("cip_loader", cip_loader),
        ("should_end", should_end),
        ("data_loader", data_loader),
    ],
)

domiapp = agent.compile()


    
