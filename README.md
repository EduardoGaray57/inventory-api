# Inventory API

REST API para gestión de inventario construida con Django REST Framework.

## Tecnologías
- Python / Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger / OpenAPI

## Endpoints

### Auth
- POST /api/auth/register/
- POST /api/auth/login/
- POST /api/auth/refresh/

### Products
- GET /api/products/
- POST /api/products/
- GET /api/products/{id}/
- PUT /api/products/{id}/
- DELETE /api/products/{id}/

### Categories
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/{id}/
- PUT /api/categories/{id}/
- DELETE /api/categories/{id}/

## Documentación
https://inventory-api-production-80f7.up.railway.app/api/docs/

## Correr localmente

1. Clonar el repositorio
2. Crear entorno virtual: python -m venv venv
3. Activar: venv\Scripts\activate
4. Instalar dependencias: pip install -r requirements.txt
5. Crear archivo .env con las variables de entorno
6. Correr migraciones: python manage.py migrate
7. Iniciar servidor: python manage.py runserver