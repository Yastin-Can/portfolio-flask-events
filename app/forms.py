#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Formularios de la aplicación usando Flask-WTF
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class ContactForm(FlaskForm):
    """Formulario de contacto"""
    name = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es requerido'),
            Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')
        ],
        render_kw={"placeholder": "Tu nombre", "class": "form-control"}
    )
    
    email = StringField(
        'Correo Electrónico',
        validators=[
            DataRequired(message='El email es requerido'),
            Email(message='Email inválido')
        ],
        render_kw={"placeholder": "tu@email.com", "class": "form-control"}
    )
    
    phone = StringField(
        'Teléfono',
        validators=[
            Optional(),
            Length(min=8, max=20, message='Teléfono inválido')
        ],
        render_kw={"placeholder": "+56 9 XXXX XXXX", "class": "form-control"}
    )
    
    subject = SelectField(
        'Tipo de Consulta',
        choices=[
            ('general', 'Consulta General'),
            ('nuevo-sitio', 'Quiero un nuevo sitio web'),
            ('rediseño', 'Necesito rediseñar mi sitio'),
            ('mantenimiento', 'Estoy interesado en mantenimiento mensual'),
            ('otro', 'Otro')
        ],
        validators=[DataRequired(message='Selecciona un tipo de consulta')],
        render_kw={"class": "form-control"}
    )
    
    message = TextAreaField(
        'Mensaje',
        validators=[
            DataRequired(message='El mensaje es requerido'),
            Length(min=10, max=2000, message='El mensaje debe tener entre 10 y 2000 caracteres')
        ],
        render_kw={
            "placeholder": "Cuéntame sobre tu proyecto...",
            "rows": 6,
            "class": "form-control"
        }
    )
    
    submit = SubmitField('Enviar Mensaje', render_kw={"class": "btn btn-primary btn-lg"})
    
    class Meta:
        csrf = True