#!/usr/bin/env python
"""
Launcher script for the Domi Agent API server.
"""

import uvicorn
import os
from dotenv import load_dotenv
import logging
from app.config import settings

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.getLevelName(settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(f"Starting Domi Agent API in {settings.ENV} mode")
    logger.info(f"Server will run on {settings.HOST}:{settings.PORT}")
    
    # Run the FastAPI app with uvicorn
    uvicorn.run(
        "app.api:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG
    ) 