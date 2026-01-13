#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Punto de entrada WSGI para producción
Usar con: gunicorn wsgi:app
"""

import os
from dotenv import load_dotenv
from app import create_app

# Cargar variables de entorno
load_dotenv()

# Crear aplicación con configuración según el entorno
app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == "__main__":
    app.run()