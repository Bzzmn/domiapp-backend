"""
Este módulo contiene la herramienta para extraer información desde archivos PDF de planos.
"""
import json
import os
from typing import Annotated, Dict, Any, Optional
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState

@tool
def check_plan(
    state: Annotated[dict, InjectedState()],
) -> str:
    """
    Extrae información desde un plano en formato PDF predefinido y la devuelve en formato JSON.
    
    Args:
        state: Estado inyectado que contiene información del usuario.
    
    Returns:
        Información del plan en formato JSON como string.
    """
    print(f"Ejecutando check_plan")
    
    # En una implementación real, aquí se haría una llamada a la API 
    # que procesa el PDF y extrae la información
    
    # Simulamos la respuesta con datos ficticios
    plan_data = {
        "uso de suelo": {
            "destino": "taller de costura"
        },
        "agrupamiento": {
            "sistema de agrupamiento": "contínuo",
            "zonas": [
            {
                "nombre": "elevación norte",
                "altura máxima": "6.83 [m]"
            },
            {
                "nombre": "elevación sur",
                "altura máxima": "6.83 [m]"
            },
            {
                "nombre": "corte a1",
                "altura máxima": "4.15 [m]"
            },
            {
                "nombre": "corte a2",
                "altura máxima": "6.83 [m]"
            }
            ]
        },
        "estacionamientos": {
            "destino": "taller de costura",
            "zonas": []
        },
        "coeficiente de constructibilidad": {
            "superficie terreno": "174.72 [m^2]",
            "constructibilidad": "200.51 [m^2]"
        },
        "coeficiente de ocupación de suelo": {
            "sistema de agrupamiento": "contínuo",
            "ocupación de suelo": "143.66 [m^2]"
        },
        "coeficiente de ocupación de pisos superiores": {
            "sistema de agrupamiento": "contínuo",
            "ocupación pisos superiores": "56.85 [m^2]"
        }
        }
    
    # En una implementación real, aquí procesaríamos la respuesta de la API
    
    return json.dumps(plan_data, ensure_ascii=False, indent=2)
