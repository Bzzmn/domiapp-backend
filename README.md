# DomiApp Backend

Backend para la aplicación DomiApp, desarrollado con FastAPI y LangGraph.

## Requisitos

- Python 3.9+
- [UV](https://github.com/astral-sh/uv) (gestor de paquetes)
- Docker y Docker Compose (opcional, para desarrollo con contenedores)

## Instalación

### Usando UV (Recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/domiapp-backend.git
cd domiapp-backend

# Crear un entorno virtual e instalar dependencias con UV
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
uv pip install .
```

### Usando Docker

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/domiapp-backend.git
cd domiapp-backend

# Crear archivo .env con las variables de entorno
echo "GROQ_API_KEY=tu_api_key_aqui" > .env

# Construir y ejecutar con Docker Compose
docker-compose up --build
```

## Desarrollo

Para ejecutar el servidor en modo desarrollo:

```bash
# Sin Docker
uvicorn app.api:app --reload

# Con Docker
docker-compose up
```

La API estará disponible en [http://localhost:8000](http://localhost:8000).

## Documentación de la API

La documentación interactiva de la API estará disponible en:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Estructura del Proyecto

```
domiapp-backend/
├── app/                  # Código principal
│   ├── api.py            # Endpoints de FastAPI
│   ├── config.py         # Configuración de la aplicación
│   ├── main.py           # Lógica de inicialización
│   └── services/         # Servicios y lógica de negocio
│       └── agent/        # Agente LangGraph
├── Dockerfile            # Configuración para Docker
├── docker-compose.yml    # Configuración para Docker Compose
├── pyproject.toml        # Configuración del proyecto y dependencias
└── README.md             # Este archivo
```

## Variables de Entorno

- `ENV`: Entorno de ejecución (`dev`, `test`, `prod`)
- `DEBUG`: Modo de depuración (`True`, `False`)
- `LOG_LEVEL`: Nivel de logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`)
- `GROQ_API_KEY`: API Key para servicios de Groq 