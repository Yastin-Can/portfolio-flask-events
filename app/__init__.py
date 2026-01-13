#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory de aplicación Flask
Crea y configura la aplicación Flask con todos sus blueprints y extensiones
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

# Inicializar extensiones
db = SQLAlchemy()
mail = Mail()


def create_app(config_name='development'):
    """
    Factory function para crear la aplicación Flask
    
    Args:
        config_name (str): Nombre de la configuración ('development', 'production', 'testing')
    
    Returns:
        Flask: Instancia configurada de la aplicación Flask
    """
    # Crear aplicación con configuración
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    mail.init_app(app)
    
    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Crear contexto de aplicación para interactuar con BD
    with app.app_context():
        # Crear tablas si no existen
        db.create_all()
    
    # Registrar manejadores de errores
    @app.errorhandler(404)
    def not_found_error(error):
        from flask import render_template
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        from flask import render_template
        db.session.rollback()
        return render_template('500.html'), 500
    
    return app