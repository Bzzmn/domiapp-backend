# Domi Agent API

Esta API proporciona endpoints para interactuar con el agente de evaluación de permisos de edificación.

## Requisitos

- Python 3.10+
- Dependencias listadas en pyproject.toml

## Configuración

1. Asegúrate de tener todas las dependencias instaladas:
   ```
   pip install -e .
   ```

2. Configura las variables de entorno necesarias en el archivo `.env` (asegúrate de que exista este archivo)

## Ejecución del servidor

Para iniciar el servidor FastAPI:

```bash
python run_api.py
```

Por defecto, el servidor se ejecutará en `http://localhost:8000`

## Endpoints disponibles

### GET /

Endpoint de prueba para verificar que la API está funcionando.

**Respuesta**:
```json
{
  "status": "ok",
  "message": "Domi Agent API is running"
}
```

### POST /agent/query

Envía una consulta al agente y recibe una respuesta.

**Request**:
```json
{
  "content": "¿Este proyecto cumple con la normativa?"
}
```

**Respuesta**:
```json
{
  "response": "Según mi análisis, el proyecto...",
  "details": {
    "full_result": { ... }
  }
}
```

### POST /agent/investigate

Inicia una investigación en segundo plano sobre un proyecto de edificación.

**Respuesta**:
```json
{
  "status": "Investigation started"
}
```

## Desarrollo

### Estructura de archivos

- `app/api.py`: Implementación del servidor FastAPI
- `app/services/agent/implementation.py`: Implementación del agente
- `run_api.py`: Script de ejecución del servidor

### Entornos de ejecución

El servidor está configurado para funcionar en entornos de desarrollo, prueba y producción. La variable `ENV` en el archivo `.env` determina el entorno actual.

### Logs

Los logs del servidor se escriben en la salida estándar. Se recomienda usar redirección para capturarlos en un archivo en entornos de producción. 