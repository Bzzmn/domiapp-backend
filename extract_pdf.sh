#!/bin/bash

# Script para ejecutar el extractor de PDF desde la raíz del proyecto

# Obtener la ruta absoluta del directorio actual (raíz del proyecto)
PROJECT_ROOT=$(pwd)

# Ruta al script Python
SCRIPT_PATH="$PROJECT_ROOT/app/services/ragger/pdf_analyzer/src/main.py"

# Verificar que el script exista
if [ ! -f "$SCRIPT_PATH" ]; then
  echo "Error: No se encontró el script en $SCRIPT_PATH"
  exit 1
fi

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
  echo "Error: Python 3 no está instalado"
  exit 1
fi

# Verificar que pdfplumber esté instalado
if ! python3 -c "import pdfplumber" &> /dev/null; then
  echo "Instalando pdfplumber..."
  pip install pdfplumber
fi

# Ejecutar el script Python
echo "Ejecutando extractor de PDF..."
python3 "$SCRIPT_PATH"

echo "Extracción completada." 