#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para probar la configuración de email de Flask-Mail
Útil para diagnosticar problemas con el envío de emails
"""

import os
from dotenv import load_dotenv
from flask_mail import Message
from app import create_app, mail

# Cargar variables de entorno
load_dotenv()

def test_email_configuration():
    """Prueba la configuración de email"""
    
    app = create_app()
    
    print("\n" + "="*60)
    print("🔧 PRUEBA DE CONFIGURACIÓN DE EMAIL")
    print("="*60 + "\n")
    
    with app.app_context():
        # Mostrar configuración
        print("📋 CONFIGURACIÓN ACTUAL:")
        print(f"  MAIL_SERVER: {app.config['MAIL_SERVER']}")
        print(f"  MAIL_PORT: {app.config['MAIL_PORT']}")
        print(f"  MAIL_USE_TLS: {app.config['MAIL_USE_TLS']}")
        print(f"  MAIL_USERNAME: {app.config['MAIL_USERNAME']}")
        print(f"  MAIL_PASSWORD: {'[CONFIGURADO]' if app.config['MAIL_PASSWORD'] else '[VACÍO - ERROR]'}")
        
        # Validar configuración
        print("\n🔍 VALIDANDO CONFIGURACIÓN:")
        
        errors = []
        
        if not app.config['MAIL_SERVER']:
            errors.append("❌ MAIL_SERVER no está configurado")
        else:
            print(f"✅ MAIL_SERVER: OK ({app.config['MAIL_SERVER']})")
        
        if not app.config['MAIL_USERNAME']:
            errors.append("❌ MAIL_USERNAME no está configurado")
        else:
            print(f"✅ MAIL_USERNAME: OK ({app.config['MAIL_USERNAME']})")
        
        if not app.config['MAIL_PASSWORD']:
            errors.append("❌ MAIL_PASSWORD no está configurado o está vacío")
        else:
            password_masked = app.config['MAIL_PASSWORD'][:4] + '*' * (len(app.config['MAIL_PASSWORD']) - 8) + app.config['MAIL_PASSWORD'][-4:]
            print(f"✅ MAIL_PASSWORD: OK ({password_masked})")
        
        if app.config['MAIL_PORT'] != 587:
            errors.append(f"⚠️  MAIL_PORT es {app.config['MAIL_PORT']} (debería ser 587)")
        else:
            print(f"✅ MAIL_PORT: OK (587)")
        
        if not app.config['MAIL_USE_TLS']:
            errors.append("❌ MAIL_USE_TLS debería ser True para Gmail")
        else:
            print(f"✅ MAIL_USE_TLS: OK (True)")
        
        # Mostrar errores si hay
        if errors:
            print("\n" + "="*60)
            print("⚠️  PROBLEMAS ENCONTRADOS:")
            print("="*60)
            for error in errors:
                print(f"\n{error}")
            
            print("\n" + "="*60)
            print("💡 SOLUCIÓN:")
            print("="*60)
            print("""
1. Verifica el archivo .env en la raíz del proyecto
2. Debe tener:
   MAIL_USERNAME=yastin.freelance@gmail.com
   MAIL_PASSWORD=[app-password de 16 caracteres]
   
3. Si estás en Render, verifica las variables de entorno:
   - Dashboard → portfolio-yastin → Settings → Environment
   
4. Para obtener app-password:
   - Ve a: https://myaccount.google.com/apppasswords
   - Selecciona: App=Mail, Device=Otros
   - Copia los 16 caracteres
            """)
            return False
        
        # Si llegamos aquí, todo está bien - intentar enviar email de prueba
        print("\n" + "="*60)
        print("✅ CONFIGURACIÓN CORRECTA")
        print("="*60)
        
        print("\n📧 INTENTANDO ENVIAR EMAIL DE PRUEBA...\n")
        
        try:
            msg = Message(
                subject='Test de Email - Portfolio Yastin',
                recipients=[app.config['MAIL_USERNAME']],
                body='Este es un email de prueba para verificar que la configuración funciona correctamente.',
                html='<h2>Email de Prueba</h2><p>Si recibes este email, todo está configurado correctamente.</p>'
            )
            
            mail.send(msg)
            
            print("✅ EMAIL ENVIADO EXITOSAMENTE!")
            print(f"   Verificar en: {app.config['MAIL_USERNAME']}")
            print("\n💡 El email debería llegar en 1-2 minutos")
            print("   Revisa tu carpeta de Spam si no lo ves en Inbox")
            
            return True
            
        except Exception as e:
            print("❌ ERROR AL ENVIAR EMAIL:")
            print(f"   {str(e)}\n")
            print("Posibles causas:")
            print("  1. App Password incorrecta")
            print("  2. Gmail rechazando la conexión")
            print("  3. 2FA no habilitado en la cuenta")
            print("  4. Configuración SMTP incorrecta")
            return False


if __name__ == "__main__":
    success = test_email_configuration()
    
    print("\n" + "="*60)
    if success:
        print("🎉 LA CONFIGURACIÓN DE EMAIL FUNCIONA CORRECTAMENTE")
    else:
        print("⚠️  HAY PROBLEMAS CON LA CONFIGURACIÓN DE EMAIL")
    print("="*60 + "\n")
    
    exit(0 if success else 1)
