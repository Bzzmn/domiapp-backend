from datetime import datetime
from typing import Dict, Optional

class Session:
    def __init__(self, session_id: str):
        """
        Initialize a new session.
        
        Args:
            session_id: ID de sesión proporcionado al iniciar el chat.
                       Este mismo ID se usará como thread_id en LangGraph.
        """
        self.session_id = session_id
        self.created_at = datetime.now()
        self.last_active = datetime.now()
        
    def get_metadata(self) -> Dict[str, any]:
        """
        Returns session metadata for debugging purposes.
        
        Returns:
            Dict[str, any]: Dictionary with session metadata
        """
        return {
            "session_id": self.session_id,
            "created_at": self.created_at,
            "last_active": self.last_active
        }
class SessionManager:
    _instance = None
    _sessions: Dict[str, Session] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def create_session(cls, session_id: str) -> Session:
        """
        Crea una nueva sesión con el ID proporcionado.
        
        Args:
            session_id: ID de sesión proporcionado al iniciar el chat.
            
        Returns:
            Session: El objeto sesión creado
        """
        session = Session(session_id)
        cls._sessions[session_id] = session
        return session
    
    @classmethod
    def get_session(cls, session_id: str) -> Optional[Session]:
        """
        Obtiene una sesión existente por su ID.
        
        Args:
            session_id: ID de sesión proporcionado al iniciar el chat.
            
        Returns:
            Optional[Session]: La sesión si existe, None si no existe
        """
        session = cls._sessions.get(session_id)
        if session:
            session.last_active = datetime.now()
        return session