#!/bin/bash

# Script para ejecutar phase2.py desde la raíz del proyecto

# Obtener la ruta absoluta del directorio actual (raíz del proyecto)
PROJECT_ROOT=$(pwd)

# Ruta al script Python
SCRIPT_PATH="$PROJECT_ROOT/app/services/ragger/pdf_analyzer/src/phase2.py"

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

# Verificar que Tesseract OCR esté instalado
if ! command -v tesseract &> /dev/null; then
  echo "Error: Tesseract OCR no está instalado"
  echo "Por favor, instálalo con: sudo apt install tesseract-ocr tesseract-ocr-spa"
  exit 1
fi

# Verificar las dependencias de Python
echo "Verificando dependencias..."
DEPENDENCIES=("pdf2image" "layoutparser" "pytesseract" "PIL" "numpy")
for dep in "${DEPENDENCIES[@]}"; do
  if ! python3 -c "import $dep" &> /dev/null; then
    echo "Instalando $dep..."
    if [ "$dep" = "PIL" ]; then
      pip install Pillow
    elif [ "$dep" = "layoutparser" ]; then
      pip install layoutparser
      # Instalar también detectron2 para layoutparser
      pip install 'git+https://github.com/facebookresearch/detectron2.git'
      pip install layoutparser[layoutmodels]
    else
      pip install $dep
    fi
  fi
done

# Crear directorio de salida si no existe
mkdir -p "$PROJECT_ROOT/output"

# Ejecutar el script Python
echo "Ejecutando extractor de layout y OCR..."
python3 "$SCRIPT_PATH"

echo "Proceso completado."