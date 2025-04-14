from langgraph.prebuilt import InjectedState
from typing_extensions import Annotated


def should_end(state: Annotated[dict, InjectedState()]) -> str:
    """
    Nodo de condicional que verifica si debe llamar a tools para obtener la respuesta.
    """
    print("In condition: conditional_edge_1")
    messages = state["messages"]
    last_message = messages[-1]
    print(f"last_message: {last_message}")
    
    # Check if tool_calls attribute exists and is not empty
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        print("Calling tools")
        tool_calls = last_message.tool_calls
        if (isinstance(tool_calls[0], dict) and tool_calls[0].get("name")) or \
           (hasattr(tool_calls[0], "function") and tool_calls[0].function.name):
            print("returning tools")
            return "tools"
    
    print("--- Ending the tool calling flow ---")
    return "end"