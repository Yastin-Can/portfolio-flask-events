#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modelos de base de datos para el portafolio
"""

from datetime import datetime
from app import db


class Contact(db.Model):
    """Modelo para mensajes de contacto"""
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Contact {self.name} - {self.email}>'


class Project(db.Model):
    """Modelo para proyectos/casos de estudio"""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    slug = db.Column(db.String(200), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(500), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    client_type = db.Column(db.String(50), nullable=False)  # restaurante, eventos, otro
    challenge = db.Column(db.Text, nullable=False)  # Problema que tenía el cliente
    solution = db.Column(db.Text, nullable=False)  # Solución implementada
    results = db.Column(db.Text, nullable=False)  # Resultados obtenidos
    
    # Imágenes
    image_url = db.Column(db.String(300), nullable=True)
    before_image_url = db.Column(db.String(300), nullable=True)
    after_image_url = db.Column(db.String(300), nullable=True)
    
    # Información adicional
    technologies = db.Column(db.String(500), nullable=True)  # Tecnologías usadas
    project_url = db.Column(db.String(300), nullable=True)  # URL del proyecto
    date_completed = db.Column(db.Date, nullable=False)
    is_featured = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'


class Service(db.Model):
    """Modelo para servicios ofrecidos"""
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(100), nullable=True)  # Clase de icono (ej: fa-globe)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Service {self.name}>'


class MaintenancePlan(db.Model):
    """Modelo para planes de mantenimiento mensual"""
    __tablename__ = 'maintenance_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='USD')
    features = db.Column(db.Text, nullable=False)  # JSON string de características
    recommended = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<MaintenancePlan {self.name}>'


class Testimonial(db.Model):
    """Modelo para testimonios de clientes"""
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_company = db.Column(db.String(100), nullable=False)
    client_role = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    image_url = db.Column(db.String(300), nullable=True)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Testimonial {self.client_name}>'