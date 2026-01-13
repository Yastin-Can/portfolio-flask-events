# ✅ Checklist de Deployment - Portfolio Yastin

## 🔍 ANTES de hacer Push

### Código
- [ ] Sin errores en terminal (sin imports rotos)
- [ ] `python run.py` funciona localmente
- [ ] Base de datos local sin errores
- [ ] Formularios de contacto funcionan
- [ ] Emails se envían correctamente

### Seguridad
- [ ] `.env` NO está en `.gitignore` (verificar)
- [ ] `.env.example` SÍ está en el repo
- [ ] `SECRET_KEY` tiene valor seguro local
- [ ] No hay contraseñas hardcodeadas
- [ ] `DEBUG=False` en producción

### Git
- [ ] Todos los cambios están commiteados
- [ ] Ningún archivo indeseado (venv/, __pycache__)
- [ ] Mensajes de commit claros
- [ ] Branch main está actualizado

### Dependencias
- [ ] `requirements.txt` actualizado
- [ ] `gunicorn==21.2.0` incluido
- [ ] Sin librerías innecesarias

---

## 📤 SUBIR A GITHUB

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit
git commit -m "Proyecto listo para producción - versión 1.0"

# Push a main
git push origin main

# Verificar en GitHub
# https://github.com/tuusuario/portfolio-flask-events
```

---

## 🌐 CONFIGURAR EN RENDER.COM

### Dashboard
- [ ] Cuenta creada
- [ ] GitHub conectado
- [ ] Repositorio autorizado

### Nuevo Web Service
- [ ] Nombre: `portfolio-yastin`
- [ ] Runtime: Python 3.11
- [ ] Build: `pip install -r requirements.txt`
- [ ] Start: `gunicorn wsgi:app`

### Variables de Entorno
```
✅ FLASK_ENV=production
✅ SECRET_KEY=<generar-aleatorio>
✅ DATABASE_URL=postgresql://...
✅ MAIL_SERVER=smtp.gmail.com
✅ MAIL_PORT=587
✅ MAIL_USE_TLS=True
✅ MAIL_USERNAME=tu-email@gmail.com
✅ MAIL_PASSWORD=app-password
```

---

## 🚀 DESPUÉS DEL DEPLOYMENT

### Verificaciones Inmediatas
- [ ] Sitio carga (https://portfolio-yastin.onrender.com)
- [ ] Página principal funciona
- [ ] Estilos CSS cargan correctamente
- [ ] Imágenes se muestran
- [ ] Links de navegación funcionan

### Funcionalidades
- [ ] Portfolio muestra proyectos
- [ ] Formulario de contacto aparece
- [ ] Formulario de contacto envía emails
- [ ] Email de confirmación llega
- [ ] Email de notificación al admin llega

### Performance
- [ ] Sitio carga rápido
- [ ] No hay errores en consola (F12)
- [ ] Responsive en móvil (F12 → móvil)
- [ ] Logs sin errores críticos

### Seguridad
- [ ] HTTPS funciona
- [ ] Certificado SSL válido
- [ ] No exposición de datos sensibles
- [ ] Formularios funcionan sin errores

---

## 🐛 Si algo falla

### No carga la página
1. Revisa Logs en Render dashboard
2. Verifica BUILD SUCCESS
3. Revisa variables de entorno
4. Intenta redeploy

### Base de datos vacía
```
# En Shell de Render:
python reinit_db.py
```

### Errores de email
1. Verifica MAIL_PASSWORD
2. Habilita acceso apps de Gmail
3. Usa contraseña de aplicación, no tu password

### Errores de importación
1. Verifica que requirements.txt esté actualizado
2. Revisa que no haya typos en nombres de paquetes
3. Redeploy

---

## 📊 URLs Importantes

- **Dashboard Render**: https://dashboard.render.com
- **Mi Servicio**: https://portfolio-yastin.onrender.com
- **GitHub Repo**: https://github.com/tuusuario/portfolio-flask-events
- **Gmail AppPasswords**: https://myaccount.google.com/apppasswords

---

## 💡 Próximos Pasos

1. **Dominio personalizado** (Pro plan)
   - Agregar dominio: `tu-dominio.com`
   - En Render → Settings → Custom Domain

2. **Monitoreo**
   - Configurar alertas
   - Revisar logs periódicamente

3. **Actualizaciones futuras**
   - Solo hacer `git push origin main`
   - Render redeploya automáticamente

4. **Backups**
   - Configurar backups automáticos de BD
   - Exportar datos regularmente

---

## 🎉 ¡LISTO!

Tu portafolio profesional está en vivo y disponible para el mundo 🌍

**Comparte tu URL:**
```
https://portfolio-yastin.onrender.com
```

