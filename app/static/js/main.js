/**
 * SCRIPTS PRINCIPALES - PORTAFOLIO YASTIN VILLARROEL
 * Funcionalidad, interactividad y mejoras UX
 */

document.addEventListener('DOMContentLoaded', function() {
    initSmoothScroll();
    initAnimations();
    initFormValidation();
    initNavbarEffects();
});

/**
 * Scroll suave para enlaces internos
 */
function initSmoothScroll() {
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

/**
 * Animaciones al hacer scroll
 */
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, section h2, section h3').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Validación de formularios
 */
function initFormValidation() {
    const forms = document.querySelectorAll('form[novalidate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!this.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            this.classList.add('was-validated');
        });
    });
}

/**
 * Efectos en la navbar al scroll
 */
function initNavbarEffects() {
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow');
            } else {
                navbar.classList.remove('shadow');
            }
        });
    }
}

/**
 * Función para enviar contactos vía AJAX
 */
function sendContactForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            name: form.querySelector('[name="name"]').value,
            email: form.querySelector('[name="email"]').value,
            phone: form.querySelector('[name="phone"]').value || '',
            subject: form.querySelector('[name="subject"]').value,
            message: form.querySelector('[name="message"]').value
        };

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                showAlert('¡Mensaje enviado exitosamente!', 'success');
                form.reset();
            } else {
                showAlert('Error al enviar el mensaje. Intenta de nuevo.', 'danger');
            }
        } catch (error) {
            console.error('Error:', error);
            showAlert('Error al enviar el mensaje.', 'danger');
        }
    });
}

/**
 * Mostrar alertas
 */
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.querySelector('main').insertBefore(alertDiv, document.querySelector('main').firstChild);
    
    // Auto-cerrar después de 5 segundos
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

/**
 * Copiar texto al portapapeles
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('¡Copiado al portapapeles!', 'success');
    }).catch(() => {
        showAlert('Error al copiar.', 'danger');
    });
}

/**
 * Abrir WhatsApp con mensaje predefinido
 */
function openWhatsApp(phone, message = '') {
    const baseUrl = 'https://wa.me/' + phone.replace(/\D/g, '');
    const url = message ? `${baseUrl}?text=${encodeURIComponent(message)}` : baseUrl;
    window.open(url, '_blank');
}
            }
        });
    }
});