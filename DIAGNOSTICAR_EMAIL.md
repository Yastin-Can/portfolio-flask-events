# 🔧 DIAGNOSTICAR PROBLEMA CON EMAIL EN RENDER

## ❌ El Problema

No recibes emails cuando pruebas el formulario de contacto en Render.

---

## 🔍 POSIBLES CAUSAS

### 1️⃣ Variables de Entorno Incorrectas o No Configuradas

**Lo que Render recibe:**
- `MAIL_USERNAME` = ???
- `MAIL_PASSWORD` = ???

Sin estas, Flask-Mail no puede autenticarse en Gmail.

### 2️⃣ Contraseña de Aplicación Incorrecta

El `MAIL_PASSWORD` debe ser una **contraseña de aplicación** generada en Google, NO tu contraseña de Gmail.

### 3️⃣ Gmail bloqueando la conexión

Si usas tu contraseña real (no app-password), Google la rechaza automáticamente por seguridad.

### 4️⃣ El formulario tiene error en validación

Si el formulario tiene error, no llega a la parte de enviar email.

---

## ✅ CÓMO VERIFICAR PASO A PASO

### PASO 1: Verifica las Variables en Render

1. Abre: https://dashboard.render.com
2. Selecciona: **"portfolio-yastin"**
3. Haz click en: **"Settings"** (o "Configuración")
4. Busca: **"Environment"** (o "Variables de Entorno")
5. Verifica que existan:
   - ✅ `FLASK_ENV` = `production`
   - ✅ `MAIL_USERNAME` = `yastin.freelance@gmail.com`
   - ✅ `MAIL_PASSWORD` = [algo con 16 caracteres sin espacios]

**Si faltan o están vacías:** Ve al PASO 3.

---

### PASO 2: Verifica que MAIL_PASSWORD sea una App Password

Tu contraseña debe verse así:
```
abcd efgh ijkl mnop
```

16 caracteres con espacios (Render los ignora).

**Si es tu contraseña real de Gmail:** Ve a PASO 3 para crear una nueva.

---

### PASO 3: Generar Nueva App Password en Gmail

Si `MAIL_PASSWORD` está vacío o es incorrecto:

1. Ve a: https://myaccount.google.com/apppasswords
2. Si pide verificación, completa
3. Selecciona:
   - **App:** "Correo" (Mail)
   - **Device:** "Otros (Windows, Mac, etc.)"
4. Click en "Generar"
5. **Copia la contraseña de 16 caracteres**

---

### PASO 4: Actualizar MAIL_PASSWORD en Render

1. Dashboard → "portfolio-yastin" → "Settings"
2. Busca: **"Environment"**
3. Busca la variable: `MAIL_PASSWORD`
4. **Haz click para EDITAR** (icono de lápiz)
5. **Borra lo que tiene**
6. **Pega la nueva contraseña de 16 caracteres**
7. **Save** (Guardar)
8. Render redeploy automáticamente (2-5 min)

---

### PASO 5: Prueba el Formulario Nuevamente

1. Cuando vea "Status: Live" nuevamente
2. Abre tu sitio: https://yastin-freelance.onrender.com
3. Ve a: **"Contacto"**
4. **Llena el formulario con datos reales:**
   ```
   Nombre: Tu Nombre
   Email: TU_EMAIL_REAL@gmail.com
   Asunto: Test
   Mensaje: Este es un test
   ```
5. Click en **"Enviar"**

**Deberías recibir el email en yastin.freelance@gmail.com**

---

## 🐛 SI AÚNNO FUNCIONA

### Opción A: Revisar Logs de Render

1. Dashboard → "portfolio-yastin"
2. Click en **"Logs"** (o "Registros")
3. Busca mensajes que digan:
   - `Error enviando email`
   - `SMTP`
   - `authentication failed`
4. Copia el mensaje de error y envíamelo

### Opción B: Verificar Formulario Localmente

En tu PowerShell:

```powershell
cd "c:\Users\Universitario\Desktop\PORTAFOLIO Yasti-Can\portfolio-flask-events"
python run.py
```

Abre: http://localhost:5000/contact

Prueba el formulario localmente. ¿Funciona aquí? Si sí, el problema es con las variables en Render.

---

## 📋 CHECKLIST DE CORRECCIÓN

```
☑️ MAIL_USERNAME existe en Render
☑️ MAIL_PASSWORD existe en Render (no está vacío)
☑️ MAIL_PASSWORD es una App Password (16 caracteres)
☑️ No es tu contraseña real de Gmail
☑️ Guardaste los cambios
☑️ Esperaste redeploy (Status: Live)
☑️ Probaste el formulario nuevamente
☑️ Email llegó a yastin.freelance@gmail.com
```

---

## 💡 CONSEJO EXTRA

Si creaste la App Password hace mucho, puede estar expirada. 

**Mejor solución:** Crear una nueva app password:

1. Ve a: https://myaccount.google.com/apppasswords
2. Si ves las antiguas, **elimínalas**
3. **Crea una nueva**
4. Actualiza en Render

---

## 🎯 RESUMEN RÁPIDO

```
1. Verifica variables en Render existen
2. Asegúrate MAIL_PASSWORD sea App Password
3. Actualiza en Render si es necesario
4. Espera redeploy (Status: Live)
5. Prueba formulario nuevamente
```

**Tiempo:** 5-10 minutos máximo

¿Cuál crees que es el problema? ¿Las variables existen pero están vacías? ¿O no sé que es?
