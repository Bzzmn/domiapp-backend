"""
Configuration module for the Domi Agent API.
Manages different environments: development, test, and production.
"""

import os
from pydantic import BaseModel
from enum import Enum
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"
    
class Settings(BaseModel):
    """Settings for the Domi Agent API."""
    # Environment configuration
    ENV: EnvironmentType = os.getenv("ENV", EnvironmentType.DEVELOPMENT)
    DEBUG: bool = ENV != EnvironmentType.PRODUCTION
    
    # API configuration
    API_TITLE: str = "Domi Agent API"
    API_DESCRIPTION: str = "API for interacting with the Domi building permit agent"
    API_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    
    # Server configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # CORS configuration
    CORS_ORIGINS: list = ["*"] if ENV != EnvironmentType.PRODUCTION else [
        "https://your-production-frontend-domain.com", "http://localhost:3001", "http://localhost:3000"
    ]
    
    # Logging configuration
    LOG_LEVEL: str = "DEBUG" if ENV != EnvironmentType.PRODUCTION else "INFO"
    
    # LLM configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # Project paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Groq configuration
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    
    class Config:
        env_file = ".env"

# Create a settings instance
settings = Settings()

def get_settings():
    """Return the settings instance."""
    return settings 