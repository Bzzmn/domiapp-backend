FROM python:3.11-slim AS builder

WORKDIR /app

# Instalar herramientas de compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero para aprovechar la caché
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Etapa final - imagen más ligera
FROM python:3.11-slim

# Argumentos de construcción para metadatos
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION=latest

# Etiquetas para metadatos de imagen según las mejores prácticas
LABEL org.opencontainers.image.created="${BUILD_DATE}" \
    org.opencontainers.image.title="DomiApp Backend" \
    org.opencontainers.image.description="Backend API para DomiApp" \
    org.opencontainers.image.revision="${VCS_REF}" \
    org.opencontainers.image.version="${VERSION}" \
    maintainer="DomiApp Team <contact@domiapp.com>"

WORKDIR /app

# Instalar curl para el healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configurar variables de entorno
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Copiar dependencias instaladas desde la etapa builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar el código de la aplicación
COPY . .

# Usuario no privilegiado para seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser \
    && chown -R appuser:appuser /app
USER appuser

# Exponer el puerto
EXPOSE ${PORT}

# Usar ENTRYPOINT con CMD para mejor control
ENTRYPOINT ["uvicorn"]
CMD ["app.api:app", "--host", "0.0.0.0", "--port", "8000"]

# Verificación de salud
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1 