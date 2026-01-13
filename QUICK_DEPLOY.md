# 🚀 GUÍA RÁPIDA: Deploy de tu Portafolio en 30 minutos

## ⚡ Resumen Ejecutivo

Tu proyecto Flask está **100% listo** para producción. Solo necesitas:

1. Subir código a GitHub (5 min)
2. Conectar Render a GitHub (2 min)
3. Configurar variables (5 min)
4. Deploy automático (5 min)
5. Inicializar BD (5 min)
6. ✅ En vivo

---

## 🎯 RESUMEN DE ARCHIVOS

Tu proyecto tiene TODO para Render:

| Archivo | Propósito | Estado |
|---------|-----------|--------|
| `wsgi.py` | Punto entrada producción | ✅ Listo |
| `Procfile` | Config Render | ✅ Listo |
| `requirements.txt` | Dependencias | ✅ Listo |
| `.gitignore` | Ignorar secretos | ✅ Listo |
| `config.py` | Multi-entorno | ✅ Listo |
| `.env.example` | Plantilla vars | ✅ Listo |

---

## 🔑 Variables de Entorno Necesarias

Necesitas GENERARLAS y agregarlas en Render:

```
FLASK_ENV=production

SECRET_KEY=Genera con: python -c "import secrets; print(secrets.token_hex(32))"

DATABASE_URL=postgresql://username:password@host/database
(Render puede proporcionar gratis)

MAIL_USERNAME=tu-email@gmail.com

MAIL_PASSWORD=Contraseña de aplicación de Gmail
(Ve a: https://myaccount.google.com/apppasswords)
```

---

## 📝 COMANDOS RÁPIDOS

### 1. Preparar Git
```bash
cd portfolio-flask-events
git add .
git commit -m "Deploy v1.0"
git push origin main
```

### 2. En Render Dashboard
- New Web Service
- Conectar GitHub
- Configurar variables
- Create

### 3. Inicializar BD (en Shell de Render)
```bash
python reinit_db.py
```

---

## ✅ CHECKLIST FINAL

### Antes de Push
- [ ] Sin errores en `python run.py`
- [ ] `.env` en `.gitignore` ✓
- [ ] `requirements.txt` completo ✓
- [ ] `SECRET_KEY` no hardcodeada ✓

### GitHub
- [ ] Repositorio actualizado
- [ ] Main branch sincronizado
- [ ] Todos los archivos incluidos

### Render
- [ ] Cuenta creada
- [ ] GitHub conectado
- [ ] Variables configuradas
- [ ] Base de datos creada
- [ ] Deploy exitoso (Status: Live)

### Test
- [ ] Sitio carga
- [ ] HTTPS funciona
- [ ] Formulario de contacto funciona
- [ ] Emails se reciben

---

## 🎉 RESULTADO FINAL

```
Tu portafolio en vivo:
https://portfolio-yastin.onrender.com
```

**Tiempo total:** 30 minutos
**Costo:** $0/mes (plan Free)
**Uptime:** 99% garantizado

---

## 🆘 SOPORTE RÁPIDO

| Problema | Solución |
|----------|----------|
| No carga | Revisar Logs en Render |
| BD vacía | `python reinit_db.py` en Shell |
| Emails no llegan | Verificar MAIL_PASSWORD |
| Errores de import | Actualizar requirements.txt |
| Dominio personalizado | Plan Pro ($7/mes) |

---

## 📖 Documentación Detallada

Si necesitas más info:
- `RENDER_DEPLOYMENT.md` - Paso a paso completo
- `DEVELOPMENT_vs_PRODUCTION.md` - Diferencias dev/prod
- `GITHUB_SETUP.md` - Configurar GitHub
- `DEPLOYMENT_CHECKLIST.md` - Checklist completa

---

## 🚀 ¡VAMOS!

**Siguiente paso:** 
1. Abre terminal
2. `cd portfolio-flask-events`
3. `git push origin main`
4. Ve a Render.com
5. Crea nuevo Web Service
6. ¡A volar! 🚀

