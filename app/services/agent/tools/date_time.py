"""
Este módulo contiene herramientas relacionadas con fecha y hora para el agente.
"""
from datetime import datetime
from typing import Annotated
from zoneinfo import ZoneInfo
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState

# Mapeo de días de la semana en español
WEEKDAYS_ES = {
    0: "lunes",
    1: "martes",
    2: "miércoles",
    3: "jueves",
    4: "viernes",
    5: "sábado",
    6: "domingo"
}

# Mapeo de días de la semana en inglés
WEEKDAYS_EN = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

@tool
def get_current_datetime(
    state: Annotated[dict, InjectedState()]
) -> str:
    """
    Devuelve la fecha y hora actuales en el timezone del usuario o Santiago por defecto.
    La hora se formatea según las preferencias del usuario e incluye el día de la semana.
    """    
    print("In tool: get_current_datetime")

    user_timezone = state.get("user_info", {}).get("timezone") if state.get("user_info", {}).get("timezone") else "America/Santiago"
    print(f"user_timezone: {user_timezone}")
    language = state.get("user_info", {}).get("language") if state.get("user_info", {}).get("language") else "es"
    print(f"language: {language}")

    now = datetime.now(ZoneInfo(user_timezone))
    weekday = now.weekday()
    
    if language == "es":
        # Formato en español
        day_name = WEEKDAYS_ES[weekday]
        return f"{day_name}, {now.strftime('%d/%m/%Y %H:%M:%S %Z')}"
    else:
        # Formato en inglés
        day_name = WEEKDAYS_EN[weekday]
        return f"{day_name}, {now.strftime('%Y-%m-%d %H:%M:%S %Z')}"