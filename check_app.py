#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para verificar que la aplicación Flask está correctamente configurada
Ejecutar con: python check_app.py
"""

import sys
import os

def check_environment():
    """Verifica el entorno Python"""
    print("🔍 Verificando entorno Python...")
    print(f"  ✓ Python {sys.version.split()[0]}")
    print(f"  ✓ Ubicación: {sys.executable}")
    print(f"  ✓ Plataforma: {sys.platform}")

def check_dependencies():
    """Verifica que todas las dependencias están instaladas"""
    print("\n🔍 Verificando dependencias...")
    
    required_packages = [
        'flask',
        'flask_wtf',
        'flask_mail',
        'flask_sqlalchemy',
        'dotenv',
        'slugify',
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('_', '-'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} (FALTA INSTALAR)")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Faltan {len(missing)} paquetes. Instalalos con:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    return True

def check_app():
    """Verifica que la aplicación Flask se puede crear"""
    print("\n🔍 Verificando aplicación Flask...")
    
    try:
        from app import create_app
        app = create_app()
        print(f"  ✓ Aplicación creada exitosamente")
        print(f"  ✓ Modo Debug: {app.config['DEBUG']}")
        print(f"  ✓ Nombre de la app: {app.config['SITE_NAME']}")
        return True
    except Exception as e:
        print(f"  ✗ Error al crear la aplicación: {e}")
        return False

def check_templates():
    """Verifica que existen los templates necesarios"""
    print("\n🔍 Verificando templates...")
    
    templates_required = [
        'base.html',
        'index.html',
        'about.html',
        'services.html',
        'portfolio.html',
        'case_study.html',
        'contact.html',
        '404.html',
        '500.html',
    ]
    
    templates_dir = 'app/templates'
    missing = []
    
    for template in templates_required:
        path = os.path.join(templates_dir, template)
        if os.path.exists(path):
            print(f"  ✓ {template}")
        else:
            print(f"  ✗ {template} (FALTA)")
            missing.append(template)
    
    return len(missing) == 0

def check_static_files():
    """Verifica que existen los archivos estáticos"""
    print("\n🔍 Verificando archivos estáticos...")
    
    static_files = [
        'css/main.css',
        'js/main.js',
    ]
    
    static_dir = 'app/static'
    missing = []
    
    for file in static_files:
        path = os.path.join(static_dir, file)
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  ✓ {file} ({size} bytes)")
        else:
            print(f"  ✗ {file} (FALTA)")
            missing.append(file)
    
    return len(missing) == 0

def check_database():
    """Verifica configuración de base de datos"""
    print("\n🔍 Verificando base de datos...")
    
    try:
        from app import create_app, db
        from app.models import Project, Service, Contact
        
        app = create_app()
        
        with app.app_context():
            # Intentar acceder a la base de datos
            db.session.query(Project).first()
            print(f"  ✓ Conexión a base de datos OK")
            
            # Contar registros
            projects = db.session.query(Project).count()
            services = db.session.query(Service).count()
            contacts = db.session.query(Contact).count()
            
            print(f"  ✓ Proyectos en BD: {projects}")
            print(f"  ✓ Servicios en BD: {services}")
            print(f"  ✓ Contactos en BD: {contacts}")
            
            if projects == 0:
                print("\n⚠️  No hay proyectos. Ejecuta: python init_db.py")
            
            return True
            
    except Exception as e:
        print(f"  ✗ Error en base de datos: {e}")
        print("  ℹ️  Ejecuta: python init_db.py")
        return False

def main():
    """Ejecuta todas las verificaciones"""
    print("=" * 60)
    print("🚀 VERIFICADOR DE APLICACIÓN FLASK - PORTAFOLIO YASTIN")
    print("=" * 60)
    
    all_ok = True
    
    check_environment()
    all_ok &= check_dependencies()
    all_ok &= check_app()
    all_ok &= check_templates()
    all_ok &= check_static_files()
    all_ok &= check_database()
    
    print("\n" + "=" * 60)
    
    if all_ok:
        print("✅ ¡TODO ESTÁ CONFIGURADO CORRECTAMENTE!")
        print("\n🚀 Para iniciar la aplicación:")
        print("  python run.py")
        print("\n📱 Accede a: http://localhost:5000")
    else:
        print("⚠️  HAY PROBLEMAS QUE NECESITAN SER RESUELTOS")
        print("\nRevisa los mensajes arriba para más detalles.")
        return 1
    
    print("=" * 60)
    return 0

if __name__ == '__main__':
    sys.exit(main())
