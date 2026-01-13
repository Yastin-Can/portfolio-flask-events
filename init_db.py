#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para inicializar la base de datos con datos de prueba
Ejecutar con: python init_db.py
"""

from datetime import date, datetime
from app import create_app, db
from app.models import Service, MaintenancePlan, Project, Testimonial

def init_database():
    """Inicializa la base de datos con datos de prueba"""
    
    app = create_app()
    
    with app.app_context():
        # Crear tablas
        print("📦 Creando tablas de base de datos...")
        db.create_all()
        print("✅ Tablas creadas exitosamente")
        
        # Verificar si ya existen datos
        if Service.query.first():
            print("⚠️  La base de datos ya contiene datos. Saltando inicialización.")
            return
        
        # Agregar Servicios
        print("\n📝 Agregando servicios...")
        services = [
            Service(
                name="Diseño Web Responsivo",
                slug="diseno-web-responsivo",
                description="Creamos sitios modernos que se ven perfectos en móviles, tablets y desktop.",
                icon="fa-mobile-alt",
                order=1
            ),
            Service(
                name="Optimización SEO",
                slug="optimizacion-seo",
                description="Posicionamos tu sitio en los primeros resultados de Google para tus palabras clave.",
                icon="fa-search",
                order=2
            ),
            Service(
                name="Mantenimiento Mensual",
                slug="mantenimiento-mensual",
                description="Actualizaciones, copias de seguridad y soporte técnico continuo.",
                icon="fa-wrench",
                order=3
            ),
            Service(
                name="Hosting & Dominio",
                slug="hosting-dominio",
                description="Alojamiento rápido y seguro con dominio personalizado incluido.",
                icon="fa-server",
                order=4
            ),
            Service(
                name="Formularios & Contacto",
                slug="formularios-contacto",
                description="Formularios de contacto que funcionan y capturan clientes potenciales.",
                icon="fa-envelope",
                order=5
            ),
            Service(
                name="Galería & Portfolio",
                slug="galeria-portfolio",
                description="Exhibe tus trabajos con galerías hermosas y profesionales.",
                icon="fa-images",
                order=6
            ),
        ]
        
        for service in services:
            db.session.add(service)
        
        db.session.commit()
        print(f"✅ {len(services)} servicios agregados")
        
        # Agregar Planes de Mantenimiento
        print("\n💰 Agregando planes de mantenimiento...")
        plans = [
            MaintenancePlan(
                name="Plan Básico",
                slug="plan-basico",
                description="Para sitios pequeños con pocas actualizaciones",
                price=50.00,
                currency="USD",
                features="Actualizaciones mensuales, Monitoreo, 1 backup",
                recommended=False,
                order=1
            ),
            MaintenancePlan(
                name="Plan Profesional",
                slug="plan-profesional",
                description="Para restaurantes, eventos y pequeños negocios",
                price=100.00,
                currency="USD",
                features="Actualizaciones, Monitoreo, Backups diarios, Soporte email",
                recommended=True,
                order=2
            ),
            MaintenancePlan(
                name="Plan Premium",
                slug="plan-premium",
                description="Soporte completo y atención prioritaria",
                price=200.00,
                currency="USD",
                features="Todo del profesional + Soporte WhatsApp 24/7, Mejoras ilimitadas",
                recommended=False,
                order=3
            ),
        ]
        
        for plan in plans:
            db.session.add(plan)
        
        db.session.commit()
        print(f"✅ {len(plans)} planes de mantenimiento agregados")
        
        # Agregar Proyectos de ejemplo
        print("\n🎨 Agregando proyectos de ejemplo...")
        projects = [
            Project(
                title="Restaurante La Cascada",
                slug="restaurante-la-cascada",
                description="Rediseño completo de sitio para restaurante de comida gourmet",
                short_description="Nuevo sitio responsive y atractivo",
                client_name="Restaurante La Cascada",
                client_type="restaurante",
                challenge="Sitio muy antiguo, sin responsive, bajo impacto visual",
                solution="Diseño moderno con Flask, Bootstrap 5 y optimizaciones SEO",
                results="40% más visitas, 25% más reservas en el primer mes",
                technologies="Flask, HTML5, CSS3, JavaScript, Bootstrap 5",
                date_completed=date(2023, 11, 15),
                is_featured=True
            ),
            Project(
                title="Wedding Planning - Andrea & Carlos",
                slug="wedding-planning-andrea-carlos",
                description="Sitio dedicado para boda con RSVP y galerías de fotos",
                short_description="Portal de boda interactivo y elegante",
                client_name="Andrea & Carlos",
                client_type="eventos",
                challenge="Necesitaban un sitio elegante para su boda con confirmación de asistentes",
                solution="Sitio responsive con formulario de RSVP integrado y galería de fotos",
                results="100% de confirmaciones digitales, reducción de contactos telefónicos",
                technologies="Flask, SQLAlchemy, Bootstrap, jQuery",
                date_completed=date(2023, 10, 20),
                is_featured=True
            ),
            Project(
                title="Productora Audiovisual MX Films",
                slug="productora-audiovisual-mx-films",
                description="Portfolio profesional para productora audiovisual",
                short_description="Sitio de portfolio con videos y proyectos",
                client_name="MX Films",
                client_type="eventos",
                challenge="Mostrar trabajos audiovisuales de forma profesional",
                solution="Sitio con galería de videos, trabajos y sistema de contacto",
                results="Aumento de inquiries de clientes en 60%",
                technologies="Flask, HTML5, CSS3, Responsive, Video embeds",
                date_completed=date(2023, 9, 10),
                is_featured=True
            ),
            Project(
                title="KS - Sistema de Gestión",
                slug="ks-sistema-gestion",
                description="Sistema de gestión desarrollado en Python. Proyecto open source disponible en GitHub.",
                short_description="Sistema de gestión con interfaz intuitiva",
                client_name="Proyecto Personal",
                client_type="software",
                challenge="Crear una solución flexible para gestión de datos",
                solution="Desarrollo de sistema robusto con Python, arquitectura escalable",
                results="Herramienta utilizada por múltiples usuarios, código disponible en GitHub",
                technologies="Python, GitHub, Open Source",
                date_completed=date(2026, 1, 10),
                is_featured=True
            ),
        ]
        
        for project in projects:
            db.session.add(project)
        
        db.session.commit()
        print(f"✅ {len(projects)} proyectos agregados")
        
        # Agregar Testimonios
        print("\n⭐ Agregando testimonios...")
        testimonials = [
            Testimonial(
                client_name="María García",
                client_company="Restaurante La Cascada",
                client_role="Dueña",
                text="Yastin transformó completamente nuestro sitio web. Ahora recibimos muchas más reservas online. Altamente recomendado.",
                rating=5,
                is_published=True
            ),
            Testimonial(
                client_name="Carlos Pérez",
                client_company="MX Films",
                client_role="Director Ejecutivo",
                text="El sitio es profesional, rápido y se ve increíble en móviles. Nuestros clientes quedaron impresionados.",
                rating=5,
                is_published=True
            ),
            Testimonial(
                client_name="Andrea López",
                client_company="Wedding Planning",
                client_role="Novia",
                text="El sitio de nuestra boda fue perfecto. Todos nuestros invitados pudieron confirmar fácilmente. ¡Gracias Yastin!",
                rating=5,
                is_published=True
            ),
        ]
        
        for testimonial in testimonials:
            db.session.add(testimonial)
        
        db.session.commit()
        print(f"✅ {len(testimonials)} testimonios agregados")
        
        print("\n" + "="*50)
        print("✅ ¡BASE DE DATOS INICIALIZADA EXITOSAMENTE!")
        print("="*50)
        print("\n📊 Resumen:")
        print(f"  • {Service.query.count()} Servicios")
        print(f"  • {MaintenancePlan.query.count()} Planes de mantenimiento")
        print(f"  • {Project.query.count()} Proyectos")
        print(f"  • {Testimonial.query.count()} Testimonios")
        print("\n🚀 Ahora puedes ejecutar: python run.py")
        print("📱 La aplicación estará en: http://localhost:5000")


if __name__ == '__main__':
    init_database()
