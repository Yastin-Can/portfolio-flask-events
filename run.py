#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from app import create_app

# Cargar variables de entorno
load_dotenv()

# Crear aplicación con configuración según el entorno
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Ejecutar servidor de desarrollo
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=app.config['DEBUG']
    )