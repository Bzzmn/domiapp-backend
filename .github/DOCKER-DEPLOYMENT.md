# Configuración de GitHub Actions para Docker

Este repositorio utiliza GitHub Actions para construir y publicar automáticamente una imagen Docker en DockerHub cada vez que se hace un push a las ramas `main` o `master`, o cuando se crea un tag con el formato `v*` (ej. v1.0.0).

## Configuración de Secretos

Antes de que el workflow pueda ejecutarse correctamente, necesitas configurar los siguientes secretos en tu repositorio de GitHub:

1. Ve a tu repositorio en GitHub
2. Haz clic en "Settings" (Configuración)
3. En el menú lateral, haz clic en "Secrets and variables" y luego en "Actions"
4. Haz clic en "New repository secret" para añadir cada uno de los siguientes secretos:

### Secretos Requeridos

- `DOCKERHUB_USERNAME`: Tu nombre de usuario de DockerHub
- `DOCKERHUB_TOKEN`: Un token de acceso para DockerHub (no uses tu contraseña)
  - Para generar un token, ve a [DockerHub Account Settings > Security > New Access Token](https://hub.docker.com/settings/security)

### Secretos Opcionales

- `SLACK_WEBHOOK`: URL del webhook de Slack para notificaciones (opcional)

## Creación de Tags

Para publicar una versión específica de tu imagen Docker:

```bash
git tag v1.0.0  # Cambia esto a la versión que quieras
git push origin v1.0.0
```

Esto disparará el workflow y publicará una imagen con el tag `v1.0.0` y también actualizará el tag `latest`.

## Ejecución Manual

También puedes ejecutar el workflow manualmente:

1. Ve a la pestaña "Actions" en tu repositorio
2. Selecciona el workflow "Build and Push Docker Image"
3. Haz clic en "Run workflow"
4. Selecciona la rama desde la que quieres construir
5. Haz clic en "Run workflow"

## Configuración Adicional

Si necesitas personalizar el nombre de la imagen o el registro de Docker, puedes modificar las variables de entorno en el archivo `.github/workflows/docker-build-push.yml`. 