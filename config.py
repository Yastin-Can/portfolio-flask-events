import os
from datetime import timedelta

class Config:
    """Configuración base de la aplicación Flask"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Seguridad
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Email
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'yastin.freelance@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    
    # Información del administrador
    ADMINS = ['yastin.freelance@gmail.com']
    
    # Información del sitio
    SITE_NAME = 'Yastin Villarroel - Desarrollo Web'
    SITE_DESCRIPTION = 'Creamos webs modernas, elegantes y responsive para eventos y restaurantes'
    DEVELOPER_NAME = 'Yastin Villarroel Cancino'
    DEVELOPER_EMAIL = 'yastin.freelance@gmail.com'
    DEVELOPER_WHATSAPP = '+56 9 2232 6630'
    
    # Redes sociales
    SOCIAL_LINKS = {
        'github': 'https://github.com/Yastin-Can',
        'linkedin': 'https://www.linkedin.com/in/yastin-villarroel',
        'whatsapp': 'https://wa.me/56922326630',
        'email': 'mailto:yastin.freelance@gmail.com'
    }


class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Configuración para testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}