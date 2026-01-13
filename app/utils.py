#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Funciones utilitarias para la aplicación
"""

import re
import unicodedata
from datetime import datetime
from slugify import slugify


def format_date(date, format='%d/%m/%Y'):
    """
    Formatea una fecha en un formato legible
    
    Args:
        date: objeto datetime
        format: formato de salida
    
    Returns:
        str: fecha formateada
    """
    if date:
        return date.strftime(format)
    return ""


def generate_slug(title):
    """
    Genera un slug amigable para URLs a partir de un título
    
    Args:
        title: texto a convertir
    
    Returns:
        str: slug
    """
    return slugify(title, to_lower=True)


def sanitize_input(user_input):
    """
    Sanitiza entrada del usuario para prevenir XSS
    
    Args:
        user_input: texto de usuario
    
    Returns:
        str: texto sanitizado
    """
    # Remover caracteres especiales peligrosos
    user_input = re.sub(r'<[^>]*>', '', user_input)
    user_input = re.sub(r'[<>\"\'%;()&+]', '', user_input)
    return user_input.strip()


def remove_accents(text):
    """
    Remover acentos del texto
    
    Args:
        text: texto con acentos
    
    Returns:
        str: texto sin acentos
    """
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def calculate_days_until_event(event_date):
    """
    Calcula cuántos días faltan para un evento
    
    Args:
        event_date: fecha del evento
    
    Returns:
        int: días restantes
    """
    return (event_date - datetime.now()).days


def format_phone(phone):
    """
    Formatea número telefónico
    
    Args:
        phone: número de teléfono
    
    Returns:
        str: teléfono formateado
    """
    phone = re.sub(r'\D', '', phone)
    if len(phone) == 9 and phone.startswith('9'):
        return f"+56 9 {phone[1:5]} {phone[5:]}"
    return phone


def truncate_text(text, length=100, suffix='...'):
    """
    Trunca texto a cierta longitud
    
    Args:
        text: texto a truncar
        length: longitud máxima
        suffix: sufijo
    
    Returns:
        str: texto truncado
    """
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix
    from markupsafe import escape
    return escape(user_input)