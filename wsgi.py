#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Punto de entrada WSGI para producción
Usar con: gunicorn wsgi:app

En Render.com:
- Procfile: web: gunicorn wsgi:app
- FLASK_ENV: production
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from app import create_app

# Crear aplicación con configuración según el entorno
# Por defecto usa 'production' si no está definido
app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == "__main__":
    # Nota: No ejecutar con app.run() en producción
    # Usar siempre: gunicorn wsgi:app
    app.run(debug=False)