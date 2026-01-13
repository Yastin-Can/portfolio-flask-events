# Guía Rápida: Desarrollo vs Producción

## 🚀 DESARROLLO LOCAL

### Comando para ejecutar:
```bash
python run.py
```

### Qué pasa:
- ✅ Debug mode: **ON** (recarga automática)
- ✅ BD: SQLite local (`portfolio.db`)
- ✅ Puerto: http://localhost:5000
- ✅ Errores detallados en consola

### Archivo clave:
```
run.py → FLASK_ENV=development → DevelopmentConfig
```

---

## 🌍 PRODUCCIÓN (Render.com)

### Comando que ejecuta Render:
```bash
gunicorn wsgi:app
```

### Qué pasa:
- ✅ Debug mode: **OFF**
- ✅ BD: PostgreSQL (en Render)
- ✅ Puerto: Asignado por Render (usualmente 8000)
- ✅ Múltiples workers para concurrencia

### Archivo clave:
```
wsgi.py → FLASK_ENV=production → ProductionConfig
```

---

## 📋 Variables de Entorno Requeridas

### SIEMPRE (Ambos entornos):
```
FLASK_ENV=development o production
SECRET_KEY=una-clave-segura-aqui
MAIL_USERNAME=tu-email@gmail.com
MAIL_PASSWORD=contraseña-de-aplicacion
```

### SOLO PRODUCCIÓN (Render):
```
DATABASE_URL=postgresql://user:pass@host:5432/db
SESSION_COOKIE_SECURE=True
```

### SOLO DESARROLLO (Local):
```
DATABASE_URL=sqlite:///portfolio.db (opcional, es el default)
```

---

## 🔄 Flujo Típico

### En desarrollo:
1. `python run.py`
2. Flask dev server atiende en localhost:5000
3. Cambios en código → reload automático
4. Base de datos: `portfolio.db` (archivo local)

### En producción (Render):
1. Git push al repositorio
2. Render detecta cambios
3. Corre: `gunicorn wsgi:app`
4. Gunicorn inicia múltiples workers
5. Nginx/Load balancer distribuye requests
6. Base de datos: PostgreSQL en Render

---

## ⚠️ Errores Comunes

### Error: "ModuleNotFoundError: No module named 'app'"
**Solución**: Asegúrate de estar en la carpeta raíz:
```bash
cd portfolio-flask-events
python run.py  # ✅ Correcto
```

### Error: "SECRET_KEY not found"
**Solución**: Crea archivo `.env`:
```
FLASK_ENV=development
SECRET_KEY=mi-clave-secreta
```

### Error: "No module named 'gunicorn'" en Render
**Solución**: Agrega a `requirements.txt`:
```
gunicorn>=21.0.0
```

---

## 🛠️ Setup en Render.com

1. **Conectar repositorio Git**
2. **Agregar variables en Environment**:
   ```
   FLASK_ENV=production
   SECRET_KEY=<clave segura>
   DATABASE_URL=<postgresql://...>
   MAIL_USERNAME=<email>
   MAIL_PASSWORD=<password>
   ```
3. **Build command** (dejarlo vacío, usa requirements.txt)
4. **Start command**: `gunicorn wsgi:app`
5. **Deploy**

---

## 📊 Comparativa Final

| Parámetro | Desarrollo | Producción |
|-----------|-----------|-----------|
| Archivo | `run.py` | `wsgi.py` |
| Comando | `python run.py` | `gunicorn wsgi:app` |
| Debug | ON | OFF |
| Base de datos | SQLite | PostgreSQL |
| Variables de entorno | `.env` (local) | Render Dashboard |
| Reloads automáticos | SÍ | NO |
| Múltiples workers | NO (1) | SÍ (4+) |
| Servidor web | Flask interno | Gunicorn |
| Proxy reverso | NO | Render (Nginx) |

