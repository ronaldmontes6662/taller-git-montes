# Manual de Inicio en GitHub

Este manual proporciona una guía paso a paso para la configuración de cuentas, gestión de repositorios y flujos de trabajo básicos en GitHub utilizando la terminal de comandos.

## 1. Creación de una Cuenta en GitHub

1. Diríjase al sitio oficial [github.com](https://github.com/).
2. Haga clic en el botón **"Sign up"** ubicado en la esquina superior derecha.
3. Introduzca su dirección de correo electrónico, defina una contraseña segura y elija un nombre de usuario disponible.
4. Complete el proceso de verificación (CAPTCHA) y confirme su cuenta mediante el código enviado a su correo electrónico.

## 2. Creación de un Repositorio y Subida de Proyecto Local

### En la plataforma GitHub:
1. Una vez iniciada la sesión, haga clic en el icono **"+"** de la barra superior y seleccione **"New repository"**.
2. En el campo **Repository name**, escriba `taller-git-montes`.
3. Establezca la visibilidad como **Public**.
4. No inicialice con archivos adicionales (README o .gitignore) si planea subir un proyecto existente. Haga clic en **"Create repository"**.

### En su máquina local (Terminal/CMD):
1. Abra la terminal en la carpeta de su proyecto.
2. Inicialice Git con el comando: `git init`.
3. Agregue sus archivos al área de preparación: `git add .`.
4. Realice el primer commit: `git commit -m "Carga inicial del proyecto de cajero automático"`.
5. Vincule su carpeta local con el servidor: `git remote add origin https://github.com/SU_USUARIO/taller-git-montes.git`.
6. Suba los cambios a la rama principal: `git push -u origin main`.

## 3. Gestión de Ramas y Commits en `develop`

Para simular un entorno de desarrollo real, se debe trabajar sobre una rama distinta a la principal.

1. **Crear la rama de desarrollo:**
   Ejecute el comando `git checkout -b develop`. Esto creará la rama y lo cambiará automáticamente a ella.
   
2. **Realizar Commits Descriptivos:**
   - **Commit 1 (Modificación):** Realice un cambio en el código (ej. editar un mensaje de bienvenida) y ejecute:
     `git add .`
     `git commit -m "Actualización del mensaje de bienvenida para personalizar la interfaz"`
     
   - **Commit 2 (Adición):** Agregue un nuevo archivo (ej. este manual) y ejecute:
     `git add MANUAL.md`
     `git commit -m "Incorporación del archivo de documentación inicial para el usuario"`

3. **Subir cambios a la nube:**
   Para finalizar, envíe la rama al repositorio remoto: `git push origin develop`.