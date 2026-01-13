#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rutas principales de la aplicación Flask
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from app import db
from app.models import Contact, Project, Service, MaintenancePlan, Testimonial
from app.forms import ContactForm
from app.email import send_email

# Crear blueprint principal
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/index')
def index():
    """Página principal / Home"""
    # Obtener proyectos destacados
    featured_projects = Project.query.filter_by(is_featured=True).limit(3).all()
    
    # Obtener testimonios publicados
    testimonials = Testimonial.query.filter_by(is_published=True).limit(5).all()
    
    # Obtener servicios
    services = Service.query.order_by(Service.order).all()
    
    return render_template('index.html', 
                         featured_projects=featured_projects,
                         testimonials=testimonials,
                         services=services)


@main_bp.route('/about')
def about():
    """Página Sobre mí"""
    # Contar proyectos completados
    project_count = Project.query.count()
    
    # Obtener servicios
    services = Service.query.order_by(Service.order).all()
    
    return render_template('about.html', 
                         project_count=project_count,
                         services=services)


@main_bp.route('/services')
def services():
    """Página de servicios"""
    # Obtener todos los servicios
    services_list = Service.query.order_by(Service.order).all()
    
    # Obtener planes de mantenimiento
    plans = MaintenancePlan.query.order_by(MaintenancePlan.order).all()
    
    return render_template('services.html', 
                         services=services_list,
                         plans=plans)


@main_bp.route('/maintenance-plans')
def maintenance_plans():
    """Página de planes de mantenimiento"""
    plans = MaintenancePlan.query.order_by(MaintenancePlan.order).all()
    return render_template('maintenance_plans.html', plans=plans)


@main_bp.route('/portfolio')
def portfolio():
    """Página de portafolio / Casos de estudio"""
    # Obtener todos los proyectos
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.date_completed.desc()).paginate(
        page=page, per_page=12, error_out=False
    )
    
    return render_template('portfolio.html', projects=projects)


@main_bp.route('/portfolio/<string:slug>')
def case_study(slug):
    """Página de caso de estudio individual"""
    project = Project.query.filter_by(slug=slug).first_or_404()
    
    # Obtener proyectos relacionados
    related_projects = Project.query.filter(
        Project.id != project.id,
        Project.client_type == project.client_type
    ).limit(3).all()
    
    return render_template('case_study.html', 
                         project=project,
                         related_projects=related_projects)


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Página de contacto con formulario"""
    form = ContactForm()
    
    if form.validate_on_submit():
        try:
            # Crear nuevo contacto en BD
            contact = Contact(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data if form.phone.data else None,
                subject=form.subject.data,
                message=form.message.data
            )
            
            db.session.add(contact)
            db.session.commit()
            
            # Enviar email al administrador
            send_email(
                subject=f"Nuevo mensaje de contacto: {form.subject.data}",
                recipients=['yastin.freelance@gmail.com'],
                text_body=f"""
                Nuevo contacto desde el portafolio:
                
                Nombre: {form.name.data}
                Email: {form.email.data}
                Teléfono: {form.phone.data or 'No proporcionado'}
                
                Asunto: {form.subject.data}
                
                Mensaje:
                {form.message.data}
                """,
                html_body=render_template('email/contact_notification.html',
                                         contact=contact)
            )
            
            flash('¡Mensaje enviado exitosamente! Me pondré en contacto pronto.', 'success')
            return redirect(url_for('main.contact'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al enviar el mensaje: {str(e)}', 'error')
    
    return render_template('contact.html', form=form)


@main_bp.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint para envío de contactos (JSON)"""
    data = request.get_json()
    
    # Validar datos mínimos
    if not all([data.get('name'), data.get('email'), data.get('message')]):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    try:
        contact = Contact(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            subject=data.get('subject', 'Contacto desde portafolio'),
            message=data['message']
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Mensaje enviado correctamente'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_bp.route('/problems')
def common_problems():
    """Página con problemas comunes que resolvemos"""
    return render_template('problems.html')


@main_bp.route('/technologies')
def technologies():
    """Página de tecnologías utilizadas"""
    tech_stack = {
        'frontend': ['HTML5', 'CSS3', 'JavaScript', 'Responsive Design'],
        'backend': ['Flask', 'Python', 'PostgreSQL', 'SQLite'],
        'tools': ['Git', 'Docker', 'Nginx', 'Gunicorn'],
        'services': ['Gmail API', 'WhatsApp Business', 'Google Analytics']
    }
    return render_template('technologies.html', tech_stack=tech_stack)


# Manejadores de errores
@main_bp.app_errorhandler(404)
def page_not_found(error):
    """Error 404 - Página no encontrada"""
    return render_template('404.html'), 404


@main_bp.app_errorhandler(500)
def internal_error(error):
    """Error 500 - Error interno del servidor"""
    db.session.rollback()
    return render_template('500.html'), 500