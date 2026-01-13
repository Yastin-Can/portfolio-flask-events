# 🚀 Guía de Despliegue - Portafolio Yastin

Instrucciones para desplegar la aplicación Flask en diferentes plataformas.

## 📋 Requisitos Previos

- Git instalado
- Cuenta en la plataforma de despliegue
- Archivos del proyecto listos
- Variables de entorno configuradas

## 🌐 Despliegue en Heroku

### Paso 1: Instalar Heroku CLI
```bash
# Windows - usar instalador o
choco install heroku-cli

# macOS
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

### Paso 2: Autenticarse con Heroku
```bash
heroku login
```

### Paso 3: Crear aplicación en Heroku
```bash
heroku create tu-app-name
```

### Paso 4: Establecer variables de entorno
```bash
heroku config:set SECRET_KEY="tu-clave-secreta-muy-segura"
heroku config:set FLASK_ENV="production"
heroku config:set MAIL_USERNAME="tu-email@gmail.com"
heroku config:set MAIL_PASSWORD="tu-app-password"
heroku config:set DATABASE_URL="postgresql://..." (si usas PostgreSQL)
```

### Paso 5: Desplegar a Heroku
```bash
git push heroku main
```

### Paso 6: Inicializar base de datos (primera vez)
```bash
heroku run python init_db.py
```

### Ver logs
```bash
heroku logs --tail
```

## ☁️ Despliegue en PythonAnywhere

### Paso 1: Crear cuenta
Ir a https://www.pythonanywhere.com y registrarse

### Paso 2: Subir archivos
- Opción A: Via Web console
- Opción B: Via Git
```bash
git clone <tu-repositorio>
```

### Paso 3: Crear virtual environment
```bash
mkvirtualenv --python=/usr/bin/python3.9 myapp
pip install -r requirements.txt
```

### Paso 4: Configurar Web App
1. En PythonAnywhere, ir a Web
2. Add a new web app
3. Elegir "Manual configuration"
4. Seleccionar Python 3.9
5. Editar WSGI configuration file

Agregar:
```python
import sys
path = '/home/your_username/portfolio-flask-events'
if path not in sys.path:
    sys.path.append(path)

from wsgi import app
application = app
```

### Paso 5: Configurar variables de entorno
En PythonAnywhere, crear archivo `.env` en la carpeta raíz del proyecto

### Paso 6: Recargar Web App
En la sección Web, hacer clic en "Reload"

## 🐳 Despliegue con Docker

### Paso 1: Construir imagen Docker
```bash
docker build -t portfolio-yastin:latest .
```

### Paso 2: Ejecutar contenedor localmente
```bash
docker run -p 5000:5000 \
  -e FLASK_ENV=production \
  -e SECRET_KEY="tu-clave" \
  -e MAIL_USERNAME="tu-email" \
  -e MAIL_PASSWORD="tu-password" \
  portfolio-yastin:latest
```

### Paso 3: Desplegar en servidor con Docker
```bash
# Transferir imagen al servidor
docker save portfolio-yastin | ssh user@server "docker load"

# En el servidor
docker run -d \
  -p 80:5000 \
  --restart always \
  -e FLASK_ENV=production \
  --name portfolio \
  portfolio-yastin:latest
```

## 🖥️ Despliegue en DigitalOcean

### Paso 1: Crear Droplet
- Imagen: Ubuntu 20.04 LTS
- Plan: Basic ($5/mes minimo)
- Región: Cercana a tus usuarios

### Paso 2: Conectarse al servidor
```bash
ssh root@tu-ip-del-servidor
```

### Paso 3: Instalar dependencias
```bash
apt update && apt upgrade
apt install python3-pip python3-venv nginx
```

### Paso 4: Clonar repositorio
```bash
cd /var/www
git clone <tu-repositorio>
cd portfolio-flask-events
```

### Paso 5: Crear virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 6: Configurar Nginx
Crear archivo `/etc/nginx/sites-available/portfolio`:

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /var/www/portfolio-flask-events/app/static/;
    }
}
```

Habilitar sitio:
```bash
ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
systemctl restart nginx
```

### Paso 7: Crear servicio systemd
Crear archivo `/etc/systemd/system/portfolio.service`:

```ini
[Unit]
Description=Portfolio Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/portfolio-flask-events
ExecStart=/var/www/portfolio-flask-events/venv/bin/gunicorn wsgi:app -w 4
Restart=always

[Install]
WantedBy=multi-user.target
```

Iniciar servicio:
```bash
systemctl enable portfolio
systemctl start portfolio
```

### Paso 8: Configurar SSL (HTTPS)
```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d tu-dominio.com
```

## 🔒 Configuración de Seguridad

Independientemente de la plataforma:

1. **Usar HTTPS siempre** - Obtener certificado SSL
2. **Variables de entorno seguras** - Nunca hardcodear secretos
3. **Base de datos segura** - Usar contraseñas fuertes
4. **Backups automáticos** - Configurar respaldos diarios
5. **Monitoreo** - Usar herramientas de monitoreo

## 📧 Configurar Email en Producción

### Opción 1: Gmail
1. Habilitar "Contraseñas de aplicación"
2. Usar `MAIL_USERNAME` y `MAIL_PASSWORD` en variables de entorno

### Opción 2: SendGrid
```bash
pip install sendgrid
```

Configurar en `config.py`:
```python
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = 587
MAIL_USERNAME = 'apikey'
MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
```

### Opción 3: MailGun
Similar a SendGrid, usar credenciales de Mailgun

## 🔧 Solución de Problemas

### Error: ModuleNotFoundError
```bash
source venv/bin/activate  # En Linux/Mac
source venv/Scripts/activate  # En Windows
pip install -r requirements.txt
```

### Error: Database locked
```bash
# Eliminar base de datos antigua
rm *.db
python init_db.py
```

### Error: Port already in use
```bash
# En Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# En Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Error: Static files not loading
Asegurar que `app.config['STATIC_FOLDER']` está bien configurado en `config.py`

## 📊 Monitoreo en Producción

### Heroku
```bash
heroku logs -t
heroku logs -t --source app
```

### DigitalOcean/VPS
```bash
systemctl status portfolio
journalctl -u portfolio -f
tail -f /var/log/portfolio.log
```

## 🔄 Actualizar Aplicación

### Con Heroku
```bash
git push heroku main
```

### Con DigitalOcean/VPS
```bash
cd /var/www/portfolio-flask-events
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
systemctl restart portfolio
```

## 📈 Optimizaciones para Producción

1. **Minificar CSS/JS** - Usar herramientas como MinifyCode
2. **Comprimir imágenes** - Usar TinyPNG o similar
3. **Caché** - Configurar caché de navegador
4. **CDN** - Usar CloudFlare para servir archivos estáticos
5. **Base de datos** - Migrar a PostgreSQL en producción

---

**Última actualización:** Enero 2026
