# Django REST Framework (DRF) - Proyecto de Práctica

Este proyecto es una API desarrollada con Django y Django Rest Framework (DRF). A continuación, se detallan los pasos para la configuración e instalación del entorno.

## Requisitos previos

Antes de comenzar, asegúrete de tener instalado:
- Python (>=3.x)
- pip (>=20.x)
- virtualenv (opcional, pero recomendado)

## Instalación y Configuración

1. **Crear un entorno virtual**
   ```bash
   python -m virtualenv venv
   ```
2. **Activar el entorno virtual**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar Django**
   ```bash
   pip install Django
   ```

4. **Crear un proyecto Django**
   ```bash
   django-admin startproject drf .
   ```

5. **Crear una aplicación dentro del proyecto**
   ```bash
   django-admin startapp api
   ```

6. **Instalar el backend de base de datos SQL Server (opcional)**
   ```bash
   pip install django-mssql-backend
   ```

7. **Realizar la primera migración**
   ```bash
   python manage.py migrate
   ```

8. **Crear migraciones personalizadas y aplicarlas**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Crear un superusuario para el panel de administración**
   ```bash
   python manage.py createsuperuser
   ```

10. **Ejecutar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```

## Instalación de Django REST Framework

11. **Instalar Django Rest Framework**
    ```bash
    pip install djangorestframework
    ```

12. **Instalar CoreAPI (opcional para navegación en la API)**
    ```bash
    pip install coreapi
    ```

## Configuración de Django REST Framework

Para habilitar DRF en el proyecto, edita el archivo `settings.py` y agrega lo siguiente:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',  # Agregar la aplicación creada
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
```

## Conexión a Bases de Datos

### MySQL
Para conectar Django con MySQL, instala el conector necesario:
```bash
pip install mysqlclient
```
Luego, en `settings.py`, configura la base de datos:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_base',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### PostgreSQL
Para conectar Django con PostgreSQL, instala el conector necesario:
```bash
pip install psycopg2-binary
```
Configura la base de datos en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Microsoft SQL Server (Django <= 4.x)
Para conectar Django con SQL Server, instala el backend adecuado:
```bash
pip install django-mssql-backend
```
Configura `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'nombre_de_tu_base',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

### Microsoft SQL Server (Django >= 5.0)
Para versiones de Django 5 o superior, usa `mssql-django` en lugar de `django-mssql-backend`:
```bash
pip install mssql-django
```
Configura `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'nombre_de_tu_base',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```
**Nota:** `mssql-django` es un backend mantenido activamente para la compatibilidad con Django 5 y versiones futuras. Más información en [MSSQL-Django](https://pypi.org/project/mssql-django/).

## Ejecución del proyecto

Para iniciar el servidor de desarrollo y probar la API, ejecuta:
```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`.

## Notas
- Puedes modificar el archivo `urls.py` para definir rutas de la API.
- Se recomienda usar `pip freeze > requirements.txt` para guardar dependencias.
- Para salir del entorno virtual, usa `deactivate` en la terminal.

---

Este README te ayudará a configurar y ejecutar tu proyecto en Django con DRF. ¡Felices desarrollos! 🚀

