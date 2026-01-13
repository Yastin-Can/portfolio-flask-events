# 🌐 Portafolio Web Profesional - Yastin Villarroel

Portafolio web moderno y profesional diseñado para captar clientes del rubro de eventos, bodas, productoras, organizadores y restaurantes. Construido con **Flask**, **Python**, **Bootstrap 5** y diseño **mobile-first**.

![Flask](https://img.shields.io/badge/Flask-2.3.3-blue?logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-green?logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Tabla de Contenidos

- [Características Principales](#características-principales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Uso](#uso)
- [Deployment](#deployment)
- [Contacto](#contacto)

## ✨ Características Principales

### 🎯 Funcionalidades Core
- ✅ **Sitio 100% Responsive** - Perfectamente optimizado para móviles, tablets y desktop
- ✅ **Portafolio Dinámico** - Gestión completa de proyectos y casos de estudio
- ✅ **Formulario de Contacto** - Integración con email y validación completa
- ✅ **Panel de Servicios** - Descripción detallada de servicios ofrecidos
- ✅ **Planes de Mantenimiento** - Opciones de mantenimiento mensual
- ✅ **Base de Datos** - SQLite para desarrollo, fácil de migrar a PostgreSQL
- ✅ **Sistema de Contactos** - Almacenamiento de leads en base de datos
- ✅ **SEO Optimizado** - Meta tags, structuraS y optimización on-page

### 🎨 Diseño & UX
- Paleta de colores profesional y moderna
- Tipografía elegant (Playfair Display + Poppins)
- Animaciones suaves y transiciones elegantes
- Navegación intuitiva y clara
- Velocidad de carga optimizada
- Accesibilidad WCAG 2.1

## 📁 Estructura del Proyecto

```
portfolio-flask-events/
├── app/
│   ├── __init__.py                 # Factory de la aplicación
│   ├── routes.py                   # Rutas principales
│   ├── models.py                   # Modelos de base de datos
│   ├── forms.py                    # Formularios WTF
│   ├── email.py                    # Servicio de emails
│   ├── utils.py                    # Funciones utilitarias
│   ├── templates/
│   │   ├── base.html               # Template base
│   │   ├── index.html              # Página principal
│   │   ├── about.html              # Sobre mí
│   │   ├── services.html           # Servicios
│   │   ├── maintenance_plans.html  # Planes de mantenimiento
│   │   ├── portfolio.html          # Portafolio
│   │   ├── case_study.html         # Caso de estudio
│   │   ├── contact.html            # Contacto
│   │   ├── problems.html           # Problemas comunes
│   │   ├── technologies.html       # Tecnologías
│   │   ├── 404.html                # Página no encontrada
│   │   ├── 500.html                # Error del servidor
│   │   └── email/
│   │       ├── contact_notification.html
│   │       └── contact_confirmation.html
│   └── static/
│       ├── css/
│       │   └── main.css            # Estilos principales
│       ├── js/
│       │   └── main.js             # Script principal
│       └── fonts/
├── config.py                        # Configuración de la app
├── run.py                          # Punto de entrada (desarrollo)
├── wsgi.py                         # Punto de entrada (producción)
├── requirements.txt                 # Dependencias
├── .env                            # Variables de entorno
├── Dockerfile                      # Configuración Docker
├── docker-compose.yml              # Compose para desarrollo
└── README.md                       # Este archivo
```

## 🔧 Requisitos

- **Python 3.8+**
- **pip** (gestor de paquetes Python)
- **Virtual Environment** (recomendado)
- **Git** (para control de versiones)

### Dependencias Principales
```
Flask==2.3.3
Flask-WTF==1.1.1
Flask-Mail==0.9.1
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
python-dotenv==1.0.0
gunicorn==21.2.0
```

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/portfolio-flask-events.git
cd portfolio-flask-events
```

### 2. Crear entorno virtual
```bash
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## ⚙️ Configuración

### 1. Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:

```env
# Configuración Flask
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=tu-clave-secreta-muy-segura

# Base de datos
DATABASE_URL=sqlite:///portfolio.db

# Email (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=tu-email@gmail.com
MAIL_PASSWORD=tu-app-password  # Contraseña de aplicación, no la contraseña de Gmail

# Información personal
DEVELOPER_NAME=Yastin Villarroel Cancino
DEVELOPER_EMAIL=yastin.freelance@gmail.com
DEVELOPER_WHATSAPP=+56922326630
```

### 2. Crear Base de Datos
```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

## 🚀 Ejecución

### Desarrollo Local
```bash
# Con debug mode activado
python run.py

# La aplicación estará en http://localhost:5000
```

### Con Gunicorn (Producción)
```bash
gunicorn wsgi:app
```

### Con Docker
```bash
# Buildear imagen
docker build -t portfolio-yastin .

# Ejecutar contenedor
docker run -p 5000:5000 portfolio-yastin
```

## 💻 Uso

### Agregar Proyectos a la BD
```python
from app import create_app, db
from app.models import Project
from datetime import date

app = create_app()
with app.app_context():
    project = Project(
        title="Sitio para Restaurante XYZ",
        slug="restaurante-xyz",
        description="Transformamos el sitio web...",
        short_description="Nuevo sitio responsive",
        client_name="Restaurante XYZ",
        client_type="restaurante",
        challenge="Sitio muy antiguo, no responsive",
        solution="Diseño moderno con Flask y Bootstrap",
        results="Aumento de 40% en consultas",
        date_completed=date.today(),
        is_featured=True
    )
    db.session.add(project)
    db.session.commit()
```

### Agregar Servicios
```python
from app import create_app, db
from app.models import Service

app = create_app()
with app.app_context():
    service = Service(
        name="Diseño Web Responsivo",
        slug="diseno-web-responsivo",
        description="Creamos sitios que se ven perfectos en todos los dispositivos",
        icon="fa-mobile-alt",
        order=1
    )
    db.session.add(service)
    db.session.commit()
```

## 📧 Configurar Gmail

1. Habilitar acceso de apps menos seguras o usar contraseñas de aplicación
2. En tu cuenta Google: https://myaccount.google.com/apppasswords
3. Selecciona "Correo" y "Windows" (o tu dispositivo)
4. Copia la contraseña generada y úsala en `.env`

## 🌐 Deployment

### En Heroku
```bash
# Crear archivo Procfile
echo "web: gunicorn wsgi:app" > Procfile

# Crear archivo runtime.txt
echo "python-3.11.0" > runtime.txt

# Deployar
git push heroku main
```

### En PythonAnywhere
1. Crear cuenta en pythonanywhere.com
2. Subir archivos del proyecto
3. Configurar Virtual Environment
4. Crear Web App con Flask
5. Configurar variables de entorno

### En AWS / DigitalOcean / etc.
Ver documentación oficial de Flask para deployment en estos servicios.

## 📊 Estructura de Datos

### Tabla: Contact
```sql
- id (Integer, PK)
- name (String)
- email (String)
- phone (String)
- subject (String)
- message (Text)
- created_at (DateTime)
- is_read (Boolean)
```

### Tabla: Project
```sql
- id (Integer, PK)
- title (String)
- slug (String, UNIQUE)
- description (Text)
- short_description (String)
- client_name (String)
- client_type (String)
- challenge (Text)
- solution (Text)
- results (Text)
- image_url (String)
- before_image_url (String)
- after_image_url (String)
- technologies (String)
- project_url (String)
- date_completed (Date)
- is_featured (Boolean)
- created_at (DateTime)
- updated_at (DateTime)
```

## 🔐 Seguridad

- ✅ CSRF Protection con Flask-WTF
- ✅ Password hashing (usar Werkzeug)
- ✅ SQL Injection prevention con ORM
- ✅ XSS Protection en templates
- ✅ HTTPS en producción
- ✅ Sanitización de inputs

## 📱 Optimizaciones

- Imágenes optimizadas y lazy-loaded
- CSS/JS minificados
- Caché de navegador configurado
- Compresión GZIP habilitada
- CDN para librerías (Bootstrap, Font Awesome)

## 🤝 Contribuciones

Si quieres mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -am 'Agrega mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📞 Contacto

**Yastin Villarroel Cancino**
- 📧 Email: yastin.freelance@gmail.com
- 💬 WhatsApp: +56 9 2232 6630
- 🌐 Portafolio: [tu-sitio.com]
- 🔗 GitHub: [tu-github]
- 💼 LinkedIn: [tu-linkedin]

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- Bootstrap 5 por el framework CSS
- Flask por el framework web
- Font Awesome por los iconos
- Google Fonts por las tipografías

---

**Última actualización:** Enero 2026
**Versión:** 1.0.0
│   │   └── 404.html
│   └── static
│       ├── css
│       │   ├── main.css
│       │   └── vendor.css
│       ├── js
│       │   └── main.js
│       ├── scss
│       │   └── main.scss
│       └── fonts
├── tests
│   ├── conftest.py
│   └── test_routes.py
├── docs
│   └── wireframes.md
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.py
├── run.py
├── wsgi.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/portfolio-flask-events.git
   ```
2. Navigate to the project directory:
   ```
   cd portfolio-flask-events
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python run.py
   ```

## Usage

- Access the application in your web browser at `http://127.0.0.1:5000`.
- Explore the portfolio, services, and case studies to understand the offerings.
- Use the contact form to reach out for inquiries or collaborations.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.