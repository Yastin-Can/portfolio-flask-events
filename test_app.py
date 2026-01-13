#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para verificar que la aplicación Flask funciona correctamente
Ejecutar con: python test_app.py
"""

from app import create_app, db
from app.models import Service, Project

def test_app():
    """Prueba básicas de la aplicación"""
    
    app = create_app()
    client = app.test_client()
    
    print("="*60)
    print("PRUEBAS DE LA APLICACION FLASK")
    print("="*60)
    
    # Test 1: Verificar que la app se crea
    print("\n[TEST 1] Crear aplicacion Flask")
    try:
        assert app is not None
        assert app.config['DEBUG'] == True
        print("  PASS - Aplicacion creada exitosamente")
    except AssertionError as e:
        print("  FAIL - " + str(e))
        return False
    
    # Test 2: Verificar que la base de datos se crea
    print("\n[TEST 2] Base de datos")
    try:
        with app.app_context():
            db.create_all()
            services_count = Service.query.count()
            projects_count = Project.query.count()
            print("  PASS - Base de datos OK")
            print("    Servicios: " + str(services_count))
            print("    Proyectos: " + str(projects_count))
    except Exception as e:
        print("  FAIL - " + str(e))
        return False
    
    # Test 3: Verificar ruta inicio
    print("\n[TEST 3] Ruta GET /")
    try:
        response = client.get('/')
        assert response.status_code == 200
        print("  PASS - Status code: " + str(response.status_code))
    except AssertionError:
        print("  FAIL - Status code: " + str(response.status_code))
        return False
    
    # Test 4: Verificar ruta servicios
    print("\n[TEST 4] Ruta GET /services")
    try:
        response = client.get('/services')
        assert response.status_code == 200
        print("  PASS - Status code: " + str(response.status_code))
    except AssertionError:
        print("  FAIL - Status code: " + str(response.status_code))
        return False
    
    # Test 5: Verificar ruta portafolio
    print("\n[TEST 5] Ruta GET /portfolio")
    try:
        response = client.get('/portfolio')
        assert response.status_code == 200
        print("  PASS - Status code: " + str(response.status_code))
    except AssertionError:
        print("  FAIL - Status code: " + str(response.status_code))
        return False
    
    # Test 6: Verificar ruta contacto
    print("\n[TEST 6] Ruta GET /contact")
    try:
        response = client.get('/contact')
        assert response.status_code == 200
        print("  PASS - Status code: " + str(response.status_code))
    except AssertionError:
        print("  FAIL - Status code: " + str(response.status_code))
        return False
    
    # Test 7: Verificar error 404
    print("\n[TEST 7] Ruta inexistente /no-existe")
    try:
        response = client.get('/no-existe')
        assert response.status_code == 404
        print("  PASS - Status code 404 retornado correctamente")
    except AssertionError:
        print("  FAIL - Status code: " + str(response.status_code))
        return False
    
    # Test 8: Verificar configuracion
    print("\n[TEST 8] Configuracion de la aplicacion")
    try:
        assert app.config['SITE_NAME'] == 'Yastin Villarroel - Desarrollo Web'
        assert app.config['DEVELOPER_NAME'] == 'Yastin Villarroel Cancino'
        assert app.config['DEVELOPER_EMAIL'] == 'yastin.freelance@gmail.com'
        print("  PASS - Configuracion correcta")
        print("    Nombre: " + app.config['SITE_NAME'])
        print("    Desarrollador: " + app.config['DEVELOPER_NAME'])
    except AssertionError as e:
        print("  FAIL - Configuracion incorrecta")
        return False
    
    print("\n" + "="*60)
    print("TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
    print("="*60)
    print("\nPuedes ejecutar la aplicacion con:")
    print("  python run.py")
    print("\nY acceder a:")
    print("  http://localhost:5000")
    
    return True

if __name__ == '__main__':
    import sys
    success = test_app()
    sys.exit(0 if success else 1)
