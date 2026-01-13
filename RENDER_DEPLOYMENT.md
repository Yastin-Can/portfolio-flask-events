# 🚀 Guía Completa: Deploy en Render.com

## ✅ Pre-requisitos

- [ ] Proyecto en GitHub (público o privado)
- [ ] Cuenta en Render.com (gratuita: https://render.com)
- [ ] Variables de entorno configuradas

---

## 📋 PASO A PASO

### 1️⃣ Crear cuenta en Render.com

1. Ve a https://render.com
2. Registrate con GitHub
3. Autoriza la conexión

### 2️⃣ Crear nuevo servicio Web

1. Dashboard → "New +"
2. Selecciona "Web Service"
3. Busca tu repositorio `portfolio-flask-events`
4. Conecta (selecciona la rama `main`)

### 3️⃣ Configurar el servicio

**Nombre del servicio:**
```
portfolio-yastin  (o el que prefieras)
```

**Plan:**
- Free (gratis, perfectamente válido)
- Pro ($7/mes, si necesitas subdominio personalizado)

**Región:**
- Selecciona la más cercana a tus usuarios

**Runtime:**
```
Python 3.11
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn wsgi:app
```

⚠️ **IMPORTANTE**: 
- Build: Dejar vacío si no hay instalación personalizada
- Start: Debe ser exactamente: `gunicorn wsgi:app`

### 4️⃣ Variables de Entorno

En la sección "Environment", agregar:

```
FLASK_ENV=production
SECRET_KEY=genera-una-clave-segura-aleatoria-aqui-cambiar-cada-vez
DATABASE_URL=postgresql://usuario:password@host:5432/database_name
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=tu-email@gmail.com
MAIL_PASSWORD=tu-app-password
```

#### 🔐 Cómo generar SECRET_KEY segura:

**Opción 1: Python interactivo**
```python
python
>>> import secrets
>>> secrets.token_hex(32)
# Copia el resultado
```

**Opción 2: OpenSSL**
```bash
openssl rand -hex 32
```

#### 📧 Cómo obtener MAIL_PASSWORD (Gmail):

1. Ve a https://myaccount.google.com/apppasswords
2. Selecciona "Correo" y "Otros (Windows, Mac, etc.)"
3. Copia la contraseña generada
4. Úsala en MAIL_PASSWORD

#### 🗄️ DATABASE_URL (PostgreSQL):

Render proporciona PostgreSQL gratis (hasta cierto límite).

1. Crea una Base de Datos PostgreSQL en Render
2. Copia la URL de conexión
3. Reemplaza en DATABASE_URL

**Formato:**
```
postgresql://username:password@host:port/database
```

**Ejemplo:**
```
postgresql://portfolio_user:abc123def456@dpg-xyz.render.com:5432/portfolio_db
```

### 5️⃣ Crear el servicio

1. Revisa que todo esté correcto
2. Botón "Create Web Service"
3. Espera 2-5 minutos (Render construye y despliega)

### 6️⃣ Inicializar Base de Datos

Una vez desplegado:

1. Ve a tu dashboard de Render
2. Abre "Logs"
3. Si ves errores de BD, ejecuta el init script

**Opción A: Shell de Render**
```bash
# En Render dashboard → Shell
python reinit_db.py
```

**Opción B: Comando remoto**
```bash
# Desde tu terminal local
heroku run python reinit_db.py  # Si usas Heroku

# Para Render, no hay comando directo, usar Shell en dashboard
```

---

## 🎯 Resultado Final

```
Tu sitio estará en:
https://portfolio-yastin.onrender.com

Render también genera URLs automáticas:
https://portfolio-yastin-xxxxxx.onrender.com
```

---

## 🔄 Actualizar cambios futuros

Simplemente:
```bash
git add .
git commit -m "Descripción del cambio"
git push origin main
```

Render automáticamente detecta el cambio y redeploya ✨

---

## ⚠️ Solución de Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'app'"
**Causa:** Build command incorrecto
**Solución:** Asegúrate de ejecutar:
```
pip install -r requirements.txt
```

### Error: "gunicorn: command not found"
**Causa:** gunicorn no instalado
**Solución:** Verifica que `gunicorn==21.2.0` esté en `requirements.txt`

### Error: "DATABASE_URL not configured"
**Causa:** Variable de entorno no establecida
**Solución:** Agrega en Render Environment:
```
DATABASE_URL=postgresql://...
```

### Error: "Secret key too short" en producción
**Causa:** SECRET_KEY no es suficientemente segura
**Solución:** Genera una con:
```python
import secrets
secrets.token_hex(32)
```

### Base de datos vacía después de deploy
**Causa:** No se ejecutó el init script
**Solución:** Usa el Shell de Render o crea datos manualmente

---

## 📊 Comparativa: Free vs Pro

| Característica | Free | Pro |
|---|---|---|
| Coste | $0/mes | $7/mes |
| CPU | Compartido | Dedicado |
| Memoria RAM | 512 MB | 1 GB+ |
| Hibernación | 15 min inactividad | NO |
| Subdominio | onrender.com | Personalizado |
| SSL | Incluido | Incluido |
| Uptime | ~99% | ~99.99% |

**Para empezar:** Free es perfecto. Upgradea si necesitas dominio personalizado.

---

## ✨ Tips Finales

1. **Monitorea logs regularmente** → Dashboard → Logs
2. **Configura alertas** → Settings → Notifications
3. **Haz backup de BD** → Render → PostgreSQL → Backups
4. **Actualiza dependencias** regularmente
5. **Usa HTTPS siempre** → Render lo hace automático

