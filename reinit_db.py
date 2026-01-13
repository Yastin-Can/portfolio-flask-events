#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para reinicializar la base de datos (eliminar todo y crear de nuevo)
"""

from datetime import date
from app import create_app, db
from app.models import Service, MaintenancePlan, Project, Testimonial

def reinit_database():
    """Reinicializa la base de datos eliminando todo"""
    
    app = create_app()
    
    with app.app_context():
        # Eliminar todas las tablas
        print("🗑️  Eliminando todas las tablas...")
        db.drop_all()
        print("✅ Tablas eliminadas")
        
        # Crear tablas nuevas
        print("\n📦 Creando tablas de base de datos...")
        db.create_all()
        print("✅ Tablas creadas exitosamente")
        
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
        
        # Agregar Proyectos
        print("\n🎨 Agregando proyectos...")
        projects = [
            Project(
                title="KS - E-commerce de Productos Saludables",
                slug="ks-ecommerce-saludable",
                description="Plataforma de e-commerce para productos saludables desarrollada en Python. Proyecto profesional con interfaz intuitiva y sistema de gestión completo.",
                short_description="E-commerce profesional de productos saludables",
                client_name="Proyecto Profesional",
                client_type="e-commerce",
                challenge="Crear una solución robusta de e-commerce con sistema de gestión de inventario",
                solution="Desarrollo completo en Python con arquitectura escalable, carrito de compras y panel de administración",
                results="Plataforma funcional y profesional lista para producción",
                technologies="Python, Flask, SQLAlchemy, Bootstrap, JavaScript",
                date_completed=date(2024, 1, 10),
                is_featured=True
            ),
        ]
        
        for project in projects:
            db.session.add(project)
        
        db.session.commit()
        print(f"✅ {len(projects)} proyectos agregados")
        
        print("\n" + "="*50)
        print("✅ ¡BASE DE DATOS REINICIALIZADA EXITOSAMENTE!")
        print("="*50)
        print("\n📊 Resumen:")
        print(f"  • {Service.query.count()} Servicios")
        print(f"  • {MaintenancePlan.query.count()} Planes de mantenimiento")
        print(f"  • {Project.query.count()} Proyectos (solo KS)")
        print(f"  • {Testimonial.query.count()} Testimonios")
        print("\n🚀 Ahora puedes ejecutar: python run.py")

if __name__ == "__main__":
    reinit_database()
