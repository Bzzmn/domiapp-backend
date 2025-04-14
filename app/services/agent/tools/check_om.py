"""
Este módulo contiene la herramienta para consultar información de la Ordenanza Municipal.
"""
import os
import uuid
from typing import List, Dict, Any, Optional
import pickle

# Importaciones para Pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

# Importaciones para Redis
from redis import Redis
from langchain_community.storage import RedisStore

# Importaciones de LangChain
from langchain_core.documents import Document
from langchain.retrievers.multi_vector import MultiVectorRetriever

from typing_extensions import Annotated
from langgraph.prebuilt import InjectedState
from langchain_core.tools import tool

from dotenv import load_dotenv

load_dotenv()

# Variables de entorno
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENVIRONMENT", "gcp-starter") 
PINECONE_INDEX = os.environ.get("PINECONE_INDEX", "pdf-analyzer")
REDIS_URL = os.environ.get("REDIS_URL")
REDIS_NAMESPACE = os.environ.get("REDIS_NAMESPACE", "docs")

class PickleMultiVectorRetriever(MultiVectorRetriever):
    """MultiVectorRetriever con soporte para deserialización automática."""
    
    def invoke(self, query, config=None, **kwargs):
        # Obtener los IDs de documentos del vectorstore
        ids = self.vectorstore.similarity_search(query, **kwargs.get("search_kwargs", {}))
        # Obtener los documentos del docstore por IDs
        docs = self.docstore.mget([d.metadata[self.id_key] for d in ids])
        # Deserializar los documentos
        return [pickle.loads(doc) if doc else None for doc in docs]

def get_om_retriever():
    """
    Inicializa y devuelve el retriever para consultar la Ordenanza Municipal.
    """
    vectorstore = PineconeVectorStore(
        pinecone_api_key=PINECONE_API_KEY,
        index_name=PINECONE_INDEX,
        embedding=OpenAIEmbeddings(),
    )

    doc_store = RedisStore(
        redis_url=REDIS_URL,
        namespace=REDIS_NAMESPACE,
    )
        
    # Crear y devolver el retriever
    retriever = PickleMultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=doc_store,
        id_key="doc_id"
    )
    
    return retriever

# Inicializar el retriever (sólo una vez al cargar el módulo)
_retriever = get_om_retriever()

def extract_text_from_results(results):
    """
    Extrae el texto y metadata relevante de los resultados del retriever.
    
    Args:
        results: Lista de resultados del retriever (CompositeElements deserializados)
        
    Returns:
        Lista de diccionarios con texto y metadata contextual
    """
    extracted_data = []
    
    for doc in results:
        if doc is not None:
            try:
                # Obtener texto del documento
                text = doc.text
                
                # Extraer metadata relevante
                metadata = {}
                if hasattr(doc, "metadata"):
                    # Extraer número de página
                    if hasattr(doc.metadata, "page_number"):
                        metadata["página"] = doc.metadata.page_number
                    
                    # Extraer tipo de documento
                    if hasattr(doc.metadata, "previous_element_type"):
                        metadata["tipo_anterior"] = doc.metadata.previous_element_type
                    
                    # Extraer nombre de archivo si está disponible
                    if hasattr(doc.metadata, "filename"):
                        metadata["archivo"] = doc.metadata.filename
                    
                    # Extraer elementos originales si están disponibles
                    if hasattr(doc.metadata, "orig_elements") and doc.metadata.orig_elements:
                        elementos = []
                        for elem in doc.metadata.orig_elements:
                            elem_type = type(elem).__name__
                            elementos.append(elem_type)
                        metadata["elementos"] = elementos
                
                # Crear diccionario con texto y metadata
                extracted_data.append({
                    "text": text,
                    "metadata": metadata
                })
            except AttributeError as e:
                # Si hay un error al extraer, guardar como string con metadata mínima
                extracted_data.append({
                    "text": str(doc),
                    "metadata": {"nota": "No se pudo extraer metadata completa"}
                })
    
    return extracted_data

@tool
def check_om(
    state: Annotated[dict, InjectedState()],
    query: str
) -> str:
    """
    Consulta información de la Ordenanza Municipal basada en una pregunta o consulta.
    
    Args:
        state: Estado inyectado que contiene información del usuario.
        query: Pregunta o consulta sobre la Ordenanza Municipal.
    
    Returns:
        Información relevante de la Ordenanza Municipal como respuesta a la consulta.
    """
    print(f"Ejecutando check_om con query: {query}")
    
    try:
        # Buscar documentos relevantes
        results = _retriever.invoke(query, search_kwargs={"k": 4})
        
        # Extraer textos y metadata de los resultados
        extracted_data = extract_text_from_results(results)
        
        if not extracted_data:
            return "No se encontró información relevante en la Ordenanza Municipal para esta consulta."
        
        # Formatear los resultados con metadata contextual
        formatted_fragments = []
        for i, data in enumerate(extracted_data):
            # Formatear la metadata como string
            metadata_str = ""
            if data["metadata"]:
                metadata_items = []
                
                if "página" in data["metadata"]:
                    metadata_items.append(f"Página: {data['metadata']['página']}")
                
                if "archivo" in data["metadata"]:
                    metadata_items.append(f"Archivo: {data['metadata']['archivo']}")
                
                if "tipo_anterior" in data["metadata"]:
                    metadata_items.append(f"Tipo de documento precedente: {data['metadata']['tipo_anterior']}")
                
                if "elementos" in data["metadata"]:
                    elementos_str = ", ".join(data["metadata"]["elementos"])
                    metadata_items.append(f"Elementos: {elementos_str}")
                
                metadata_str = " | ".join(metadata_items)
            
            # Formatear el fragmento con número, metadata y texto
            fragment = f"Fragmento {i+1}:" + (f" [{metadata_str}]" if metadata_str else "") + f"\n{data['text']}"
            formatted_fragments.append(fragment)
        
        context = "\n\n" + "\n\n".join(formatted_fragments)
        
        return f"""
Información encontrada en la Ordenanza Municipal:
{context}
"""
    except Exception as e:
        print(f"Error al consultar la Ordenanza Municipal: {str(e)}")
        return f"Error al consultar la Ordenanza Municipal: {str(e)}"
