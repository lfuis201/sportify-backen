# proyecto_gestion_deportiva

Este proyecto de gestión deportiva utiliza Django para su desarrollo.

### Configuración del Entorno Virtual y Ejecución del Proyecto Django

Para ejecutar este proyecto Django, es recomendable usar un entorno virtual y luego instalar las dependencias necesarias desde un archivo `requirements.txt`.

1. **Configuración del Entorno Virtual:**
   Si no tienes instalado `virtualenv`, puedes hacerlo con `pip` (el gestor de paquetes de Python). Abre tu terminal y ejecuta:

   ```bash
   pip install virtualenv
1. **Configuración del Entorno Virtual:**
   Si no tienes instalado `virtualenv`, puedes hacerlo con `pip` (el gestor de paquetes de Python). Abre tu terminal y ejecuta:

   ```bash
   pip install virtualenv

1. **creacion del Entorno Virtual:**
   Abre tu terminal y ejecuta:

   ```bash
   virtualenv venv

1. **Activación del Entorno Virtual:**
   Para activar el entorno virtual en Windows, ejecuta:



   ```bash
   venv\Scripts\activate
1. **En macOS y Linux, ejecuta:**

   ```bash
   source venv/bin/activate
1. **Instalación de Dependencias:**
    Una vez activado el entorno virtual, instala las dependencias del proyecto desde el archivo requirements.txt. Ejecuta:
   ```bash
   pip install -r requirements.txt

1. **Ejecución del Servidor Django:**
    Finalmente, para iniciar el servidor de desarrollo de Django, ejecuta:
   ```bash
   python manage.py runserver