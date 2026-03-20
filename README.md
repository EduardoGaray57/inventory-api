# 📦 Inventory API
 
REST API para gestión de inventario de productos y categorías, con autenticación JWT y documentación Swagger interactiva.
 
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://python.org/)
[![Django](https://img.shields.io/badge/Django-REST_Framework-092E20?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?logo=railway&logoColor=white)](https://railway.app/)
[![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?logo=swagger&logoColor=black)](https://inventory-api-production-80f7.up.railway.app/api/docs/)
 
## 🔗 Documentación interactiva (Swagger)
 
👉 **[https://inventory-api-production-80f7.up.railway.app/api/docs/](https://inventory-api-production-80f7.up.railway.app/api/docs/)**
 
> Puedes probar todos los endpoints directamente desde el navegador sin necesidad de instalar nada.
 
---
 
## 🛠️ Stack tecnológico
 
| Capa | Tecnología |
|---|---|
| Backend | Python 3.13 + Django |
| API | Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Base de datos | PostgreSQL |
| Documentación | Swagger / OpenAPI 3.0 |
| Deploy | Railway |
 
---
 
## 📡 Endpoints
 
### Auth
| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/api/auth/register/` | Registro de usuario |
| POST | `/api/auth/login/` | Inicio de sesión (retorna JWT) |
| POST | `/api/auth/refresh/` | Renovar token de acceso |
 
### Products (requieren autenticación)
| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/products/` | Listar productos |
| POST | `/api/products/` | Crear producto |
| GET | `/api/products/{id}/` | Obtener producto |
| PUT | `/api/products/{id}/` | Actualizar producto |
| DELETE | `/api/products/{id}/` | Eliminar producto |
 
### Categories (requieren autenticación)
| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/categories/` | Listar categorías |
| POST | `/api/categories/` | Crear categoría |
| GET | `/api/categories/{id}/` | Obtener categoría |
| PUT | `/api/categories/{id}/` | Actualizar categoría |
| DELETE | `/api/categories/{id}/` | Eliminar categoría |
 
---
 
## ⚙️ Correr localmente
 
```bash
# 1. Clonar el repositorio
git clone https://github.com/EduardoGaray57/inventory-api.git
cd inventory-api
 
# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
 
# 3. Instalar dependencias
pip install -r requirements.txt
 
# 4. Configurar variables de entorno
# Crear archivo .env con:
# SECRET_KEY=tu_clave_secreta
# DEBUG=True
# DB_NAME=inventory_db
# DB_USER=tu_usuario
# DB_PASSWORD=tu_password
# DB_HOST=localhost
# DB_PORT=5432
 
# 5. Aplicar migraciones
python manage.py migrate
 
# 6. Iniciar servidor
python manage.py runserver
```
 
> La API queda disponible en `http://localhost:8000` y el Swagger en `http://localhost:8000/api/docs/`
 
---
 
## 📁 Estructura del proyecto
 
```
inventory-api/
├── config/         # Configuración de Django (settings, urls, wsgi)
├── products/       # App de productos y categorías (models, views, serializers)
├── users/          # App de autenticación y usuarios
├── manage.py
├── requirements.txt
├── Procfile        # Configuración para Railway
└── .gitignore
```
 
---
 
## 🔐 Variables de entorno requeridas
 
```
SECRET_KEY=
DEBUG=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
 
---

## 🔗 Proyectos relacionados

- [daily-planner-web](https://github.com/EduardoGaray57/daily-planner-web) — Aplicación fullstack con React + Django
- [daily-planner-api](https://github.com/EduardoGaray57/daily-planner-api) — Backend Django REST del daily planner

---
 
## 👨‍💻 Autor
 
**Eduardo Garay**
- 📍 Quilicura, Santiago, Chile
- 🔗 [LinkedIn](https://www.linkedin.com/in/eduardo-garay-9b067b16b)
- 🐙 [GitHub](https://github.com/EduardoGaray57)
 
