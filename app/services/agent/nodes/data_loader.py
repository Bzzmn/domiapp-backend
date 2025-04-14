from typing_extensions import Annotated
from langgraph.prebuilt import InjectedState
from langgraph.types import Command

def data_loader(state: Annotated[dict, InjectedState]) -> Command:
    """
    This function loads the project data from the database to the state.
    """

    project_name = "EINSTEIN 264"
    project_description = "Solicitud de permiso de edificacion para ampliacion taller de costura en direccion Einstein 264, Recoleta"
    project_status = "active"
    project_owner = "Juan Perez"
    project_created_at = "2021-01-01"
    project_updated_at = "2025-04-02"

    state_update = {
        "project_name": project_name,
        "project_description": project_description,
        "project_status": project_status,
        "project_owner": project_owner,
        "project_created_at": project_created_at,
        "project_updated_at": project_updated_at,
    }

    return Command(
        update=state_update
    )