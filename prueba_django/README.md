# Prueba Técnica – Django

Mini aplicación en Django que permite registrar y listar productos, con autenticación y una API REST protegida.

## Tecnologías
- Python 3.13
- Django 5.2.8
- Django REST Framework 3.16.1
- SQLite (por defecto)

## Requisitos previos
- Python 3.10+ (se probó con 3.13.2)
- pip

## Instalación
# Clonar el repositorio
git clone https://github.com/tu_usuario/prueba_django.git
cd prueba_django

# Crear entorno virtual
python -m venv env

# Activar entorno virtual (Windows)
env\Scripts\Activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones y base de datos

python manage.py makemigrations
python manage.py migrate

# Crear usuario administrador (para entrar a /admin)
python manage.py createsuperuser

# Ejecutar el servidor
python manage.py runserver

# URLs principales
Web (lista de productos): http://127.0.0.1:8000/
Login: http://127.0.0.1:8000/accounts/login/
Logout: http://127.0.0.1:8000/accounts/logout/ (método POST desde el botón en la barra)
Admin: http://127.0.0.1:8000/admin/
API (autenticada): http://127.0.0.1:8000/api/productos/

# Notas de autenticación
Solo usuarios autenticados pueden ver la lista y crear productos.
La API REST está protegida con autenticación por sesión (DRF).

# Cómo probar rápidamente
Crear superusuario.
Iniciar sesión en /accounts/login/.
Ver lista en /.
Agregar producto en /agregar/.
Consultar la API en /api/productos/.

# Autor
Oscar Javier Vanegas Munevar