#!/usr/bin/env python3
"""
Script para generar requirements.txt desde pyproject.toml
"""

import tomli
import sys

def generate_requirements_txt():
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomli.load(f)
        
        dependencies = data.get("project", {}).get("dependencies", [])
        
        with open("requirements.txt", "w") as f:
            for dep in dependencies:
                f.write(f"{dep}\n")
        
        print("✅ Archivo requirements.txt generado exitosamente")
        return 0
    except Exception as e:
        print(f"❌ Error al generar requirements.txt: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(generate_requirements_txt()) 