# Guía para Subir a GitHub

## Opción A: Repositorio NUEVO (si no existe)

### 1. Crear repositorio en GitHub
1. Ve a https://github.com/new
2. Nombre: `portfolio-flask-events`
3. Descripción: `Portafolio web profesional con Flask`
4. Privado o Público (Render puede acceder a ambos)
5. ✅ Crear

### 2. Conectar tu repositorio local con GitHub
```bash
git remote add origin https://github.com/Yastin-Can/portfolio-flask-events.git
git branch -M main
git push -u origin main
```

---

## Opción B: Repositorio EXISTENTE

### 1. Verificar remote
```bash
git remote -v
```

### 2. Si está conectado, solo hacer push
```bash
git push origin main
```

---

## Verificar que todo esté ok
```bash
git remote -v
# Debe mostrar:
# origin  https://github.com/TuUsuario/portfolio-flask-events.git (fetch)
# origin  https://github.com/TuUsuario/portfolio-flask-events.git (push)
```

