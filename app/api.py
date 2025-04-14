"""
FastAPI server for the Domi agent.
Provides endpoints to interact with the agent.
"""

import uuid
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
import asyncio
import os
import logging
from app.config import settings, get_settings
from app.main import ChatSession
from fastapi import UploadFile, File, HTTPException
from groq import Groq
import tempfile
import os



# Configure logging
logging.basicConfig(
    level=logging.getLevelName(settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Models for the API
class MessageRequest(BaseModel):
    """Request model for sending a message to the agent."""
    content: str
    
class AgentResponse(BaseModel):
    """Response model from the agent."""
    response: str
    resolucion: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

class TranscriptionResponse(BaseModel):
    """Response model for audio transcription."""
    transcription: str

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/")
async def root():
    """Root endpoint to check if the API is running."""
    logger.info("Root endpoint accessed")
    return {"status": "ok", "message": f"Domi Agent API is running in {settings.ENV} mode"}

@app.post("/agent/query", response_model=AgentResponse)
def query_agent(message_request: MessageRequest, settings=Depends(get_settings)):
    """
    Send a query to the agent and get a response.
    """
    logger.info(f"Query received: {message_request.content}")

    session_id = str(uuid.uuid4())
    chat_session = ChatSession(session_id=session_id)

    try:
        # Call the agent with the user's message
        result = chat_session.process_query(message_request.content)
        print("--------------------------------")
        print(f"Result: {result}")
        print("--------------------------------")
        
        # Extract the response from the agent's result
        if "messages" in result and len(result["messages"]) > 0:
            # Buscar el último mensaje de tipo AIMessage
            ai_messages = [msg for msg in result["messages"] if hasattr(msg, 'type') and msg.type == 'ai' or 
                          (hasattr(msg, '__class__') and msg.__class__.__name__ == 'AIMessage')]
            
            if ai_messages:
                last_ai_message = ai_messages[-1]
                response_content = last_ai_message.content if hasattr(last_ai_message, 'content') else ""
                
                # Obtener la resolución del resultado
                resolucion = result.get("resolucion_item", "No aplica")
                
                logger.info(f"Response generated successfully")
                return AgentResponse(
                    response=response_content,
                    resolucion=resolucion
                )
            
        logger.warning("No response generated from agent")
        return AgentResponse(
            response="No response from agent",
            resolucion="No aplica"
        )
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
    

@app.post("/api/transcription", response_model=TranscriptionResponse)
async def transcribe_audio(audio: UploadFile = File(...)):
    """
    Receives an audio file and transcribes it to text using Groq's Whisper model.
    """
    # Check if audio file
    if not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio.filename)[1]) as temp_file:
        temp_file_path = temp_file.name
        content = await audio.read()
        temp_file.write(content)
    
    try:
        # Initialize Groq client
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        # Open the audio file and send to Whisper for transcription
        with open(temp_file_path, "rb") as audio_file:
            # Create a transcription using the Whisper model through Groq
            response = client.audio.transcriptions.create(
                model="whisper-large-v3-turbo",
                file=audio_file, 
                language="es"
            )
        
        # Return the transcription
        return {"transcription": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription error: {str(e)}")
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)








if __name__ == "__main__":
    # Run the FastAPI app with uvicorn
    uvicorn.run(
        "app.api:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG
    ) 