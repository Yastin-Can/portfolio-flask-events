#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Servicio de envío de emails
"""

from flask_mail import Message
from app import mail
from flask import render_template


def send_email(subject, recipients, text_body=None, html_body=None):
    """
    Envía un email
    
    Args:
        subject (str): Asunto del email
        recipients (list): Lista de destinatarios
        text_body (str): Cuerpo del email en texto plano
        html_body (str): Cuerpo del email en HTML
    
    Returns:
        bool: True si se envió correctamente, False si hubo error
    """
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=text_body,
            html=html_body
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error enviando email: {str(e)}")
        return False


def send_contact_confirmation(contact_email, contact_name):
    """
    Envía email de confirmación al contacto
    
    Args:
        contact_email (str): Email del contacto
        contact_name (str): Nombre del contacto
    
    Returns:
        bool: True si se envió correctamente
    """
    return send_email(
        subject='Hemos recibido tu mensaje',
        recipients=[contact_email],
        html_body=render_template('email/contact_confirmation.html',
                                  name=contact_name)
    )


def send_newsletter_notification(email_list, subject, html_content):
    """
    Envía newsletter a múltiples suscriptores
    
    Args:
        email_list (list): Lista de emails
        subject (str): Asunto
        html_content (str): Contenido HTML
    
    Returns:
        bool: True si se envió correctamente
    """
    return send_email(
        subject=subject,
        recipients=email_list,
        html_body=html_content
    )