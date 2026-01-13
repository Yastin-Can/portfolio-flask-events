# 🚀 INICIALIZAR BASE DE DATOS EN RENDER

## ¿Por qué ves la página pero sin datos?

El sitio está **Live** ✅ pero la base de datos está **vacía** porque necesitas ejecutar el script de inicialización.

---

## 📋 PASOS PARA INICIALIZAR LA BD

### PASO 1: Acceder al Dashboard de Render

1. Ve a: https://dashboard.render.com
2. Selecciona tu servicio: **"portfolio-yastin"**
3. Verifica que diga "Status: Live" (en verde)

---

### PASO 2: Abrir el Shell

En el dashboard de tu servicio, verás una barra de opciones en la parte superior:

```
[ Logs ] [ Events ] [ Settings ] [ Shell ] [ Metrics ]
```

**Haz click en "Shell"**

Se abrirá una terminal negra en el navegador.

---

### PASO 3: Ejecutar el Script

En el Shell, copia y pega este comando:

```bash
python reinit_db.py
```

Presiona **Enter**.

---

### PASO 4: Verificar el Resultado

Deberías ver algo como esto:

```
🗑️  Eliminando todas las tablas...
✅ Tablas eliminadas

📦 Creando tablas de base de datos...
✅ Tablas creadas exitosamente

📝 Agregando servicios...
✅ 6 servicios agregados

💰 Agregando planes de mantenimiento...
✅ 3 planes de mantenimiento agregados

🎨 Agregando proyectos...
✅ 1 proyectos agregados

==================================================
✅ ¡BASE DE DATOS REINICIALIZADA EXITOSAMENTE!
==================================================

📊 Resumen:
  • 6 Servicios
  • 3 Planes de mantenimiento
  • 1 Proyectos (solo KS)
  • 0 Testimonios

🚀 Ahora puedes ejecutar: python run.py
```

---

### PASO 5: Actualizar tu Navegador

1. Abre tu sitio en otra pestaña: **https://yastin-freelance.onrender.com**
2. Presiona **Ctrl+F5** (recarga total, sin caché)
3. ¡Ahora deberías ver tus servicios y proyectos!

---

## 🎯 ¿Qué data se Agregó?

### ✅ 6 Servicios:
- Diseño Web Responsivo
- Optimización SEO
- Mantenimiento Mensual
- Hosting & Dominio
- Formularios & Contacto
- Galería & Portfolio

### ✅ 3 Planes de Mantenimiento:
- Plan Básico ($50/mes)
- Plan Profesional ($100/mes) ← Recomendado
- Plan Premium ($200/mes)

### ✅ 1 Proyecto:
- KS - E-commerce de Productos Saludables

### ✅ 0 Testimonios (puedes agregar luego)

---

## ⚠️ SI ALGO FALLA

### Error: "Module not found"
```
Problema: El script no encuentra los módulos
Solución: Espera 1-2 minutos después del deploy y reintenta
```

### Error: "Database connection failed"
```
Problema: La BD PostgreSQL no está vinculada correctamente
Solución: Verifica en Settings → Environment que DATABASE_URL esté correcta
```

### Error: "Permission denied"
```
Problema: No tienes acceso
Solución: Cierra Shell y abre uno nuevo
```

---

## 🔄 Si necesitas Reinicializar de Nuevo

Si en el futuro necesitas limpiar la BD y volver a agregar datos:

```bash
python reinit_db.py
```

Simplemente ejecuta el mismo comando nuevamente.

---

## ✅ Checklist

- [ ] Abrir https://dashboard.render.com
- [ ] Seleccionar "portfolio-yastin"
- [ ] Click en "Shell"
- [ ] Pegar: `python reinit_db.py`
- [ ] Presionar Enter
- [ ] Verificar: "BASE DE DATOS REINICIALIZADA EXITOSAMENTE!"
- [ ] Actualizar navegador: Ctrl+F5
- [ ] Ver servicios y proyectos en el sitio

---

## 🎉 Éxito

Una vez completado, tu sitio tendrá:
✅ 6 Servicios visibles en la página de Servicios
✅ 1 Proyecto en la página de Portfolio
✅ 3 Planes en la página de Planes
✅ Formulario de contacto funcional

---

**Tiempo estimado:** 2-3 minutos
