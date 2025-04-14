import uuid
import os
from langchain_core.messages import HumanMessage
from datetime import datetime
from app.services.agent.builder import create_agent
from app.utils.session_manager import SessionManager
from langgraph.checkpoint.memory import MemorySaver

class ChatSession:
    # Class-level variables for agent and memory
    _agent = None
    _memory = None
    
    @classmethod
    def get_or_create_agent(cls, persistence_type: str = "memory"):

        if cls._memory is None:
            if persistence_type == "memory":
                cls._memory = MemorySaver()
            else:
                raise ValueError(f"Invalid persistence type: {persistence_type}")

        if cls._agent is None:
            # TODO: Add memory instance to the agent
            # cls._agent = create_agent(memory_instance=cls._memory)
            cls._agent = create_agent()

        return cls._agent
    
    def __init__(self, session_id: str, persistence_type: str = "memory"):
        """
        Inicializa una nueva sesión de chat.
        
        Args:
            session_id: ID de sesión proporcionado al iniciar el chat
            persistence_type: Tipo de persistencia a usar ("summarizing_memory" por defecto)
            debug_mode: Habilitar modo de depuración (False por defecto)
        """
        # Get or create session first
        self.session_manager = SessionManager()
        self.session = self.session_manager.get_session(session_id) or self.session_manager.create_session(session_id)

        self.session_id = self.session.session_id

        # Get or create shared agent
        self.agent = self.get_or_create_agent(persistence_type)

        self.config = {
            "configurable": {
                "thread_id": self.session.session_id
            }
        }
        
    def process_query(self, query: str):
        """
        Process a user query and return the agent's response.
        """
        inputs = {
            "messages": [HumanMessage(content=query)]
        }

        response = self.agent.invoke(inputs)
        return response


if __name__ == "__main__":
    chat_session = ChatSession(session_id="test")
    response = chat_session.process_query("Uso de suelo")
    print(response)