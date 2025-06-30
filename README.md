# Django REST API with JWT Authentication

A Django REST API project with JWT authentication, product management, and Swagger documentation. This project replicates a FastAPI application using Django REST Framework.

## Features

- **JWT Authentication** using `djangorestframework-simplejwt`
- **User Registration and Login**
- **Product CRUD Operations** (Create, Read, Update, Delete)
- **Bulk Product Creation**
- **Swagger/OpenAPI Documentation** using `drf-yasg`
- **MySQL Database** support
- **User-specific Product Management**

## Tech Stack

- **Django 4.2.23**
- **Django REST Framework 3.16.0**
- **djangorestframework-simplejwt 5.5.0**
- **drf-yasg 1.21.10** (Swagger documentation)
- **MySQL/MariaDB** (database)
- **Python 3.13**

## Prerequisites

- Python 3.13+
- MySQL/MariaDB 10.4+ (for Django 4.2)
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Navigate to Project Directory
```bash
cd C:\DJANGO
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install django==4.2.* djangorestframework drf-yasg djangorestframework-simplejwt mysqlclient
```

### 5. Database Setup
Create a MySQL database named `django_db`:
```sql
CREATE DATABASE django_db;
```

### 6. Configure Database (if needed)
Edit `config/settings.py` to match your MySQL credentials:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_db",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 7. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- **POST** `/register/` - Register a new user
- **POST** `/token/` - Login and get JWT token

### Products (Require JWT Authentication)
- **GET** `/products/` - List all products for the authenticated user
- **POST** `/products/` - Create a new product
- **PUT** `/products/{id}/` - Update a product
- **DELETE** `/products/{id}/` - Delete a product
- **POST** `/products/bulk/` - Create multiple products at once

### Documentation
- **GET** `/swagger/` - Swagger UI documentation
- **GET** `/redoc/` - ReDoc documentation

## Usage Examples

### 1. Register a New User
```bash
curl -X POST "http://127.0.0.1:8000/register/" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "password": "testpass123"
     }'
```

### 2. Login and Get JWT Token
```bash
curl -X POST "http://127.0.0.1:8000/token/" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "password": "testpass123"
     }'
```

### 3. Create a Product (with JWT token)
```bash
curl -X POST "http://127.0.0.1:8000/products/" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "iPhone 12",
       "description": "Smartphone",
       "image_url": "https://example.com/iphone12.jpg"
     }'
```

### 4. List Products
```bash
curl -X GET "http://127.0.0.1:8000/products/" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 5. Bulk Create Products
```bash
curl -X POST "http://127.0.0.1:8000/products/bulk/" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "products": [
         {
           "name": "iPhone 12",
           "description": "Smartphone",
           "image_url": "https://example.com/iphone12.jpg"
         },
         {
           "name": "Samsung Galaxy",
           "description": "Android Phone",
           "image_url": "https://example.com/samsung.jpg"
         }
       ]
     }'
```

## Database Models

### User Model (Django's built-in)
- `id` - Primary key
- `username` - Unique username
- `password` - Hashed password

### Product Model
- `id` - Primary key
- `name` - Product name (max 100 chars)
- `description` - Product description (max 255 chars, optional)
- `user` - Foreign key to User (owner of the product)
- `image_url` - URL to product image (max 255 chars, optional)

## Project Structure

```
DJANGO/
├── config/                 # Django project settings
│   ├── settings.py        # Database and app configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── api/                   # Main API application
│   ├── models.py         # Database models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   ├── urls.py           # API URL routing
│   └── migrations/       # Database migrations
├── venv/                 # Virtual environment
├── manage.py             # Django management script
└── README.md             # This file
```

## Authentication Flow

1. **Register** a user via `/register/`
2. **Login** via `/token/` to get a JWT token
3. **Use the JWT token** in the `Authorization` header for all protected endpoints
4. **Format**: `Authorization: Bearer YOUR_JWT_TOKEN`

## Development

### Running Tests
```bash
python manage.py test
```

### Creating a Superuser
```bash
python manage.py createsuperuser
```

### Accessing Django Admin
Visit `http://127.0.0.1:8000/admin/` after creating a superuser.

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL is running
   - Check database credentials in `settings.py`
   - Verify database `django_db` exists

2. **Migration Errors**
   - Delete all files in `api/migrations/` (except `__init__.py`)
   - Run `python manage.py makemigrations && python manage.py migrate`

3. **JWT Token Issues**
   - Ensure you're using the correct token format: `Bearer YOUR_TOKEN`
   - Check if the token hasn't expired
   - Verify the user exists in the database

4. **Foreign Key Errors**
   - Ensure you're authenticated with a valid user
   - Check that the user exists in the `auth_user` table

## API Documentation

Visit the interactive API documentation:
- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`

## License

This project is for educational purposes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request 