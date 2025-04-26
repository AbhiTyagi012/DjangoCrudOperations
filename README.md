Car Rental API - Django + DRF + JWT Auth
========================================

This project is a Car Rental Management API built with Django, Django REST Framework (DRF), and SimpleJWT for token-based authentication.

It includes CRUD operations for:
- Cars
- Customers
- Bookings
- Plus, available cars lookup for a date range.


Project Structure
-----------------
testproject/
│
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── testproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md


Installation and Setup
-----------------------
1. Clone the repository
   git clone https://github.com/AbhiTyagi012/DjangoCrudOperations.git

2. Install dependencies
   pip install -r requirements.txt

3. Apply migrations
   python manage.py migrate

4. Create a superuser
   python manage.py createsuperuser

5. Run the development server
   python manage.py runserver


Authentication
--------------
This project uses JWT Authentication (rest_framework_simplejwt).

To use the API:
- First login with your username/password to obtain an access token.
- Use this token in Authorization Header for all protected requests.


API Endpoints
-------------
Method | Endpoint | Description
POST   | /api/token/           | Get JWT access and refresh token
POST   | /api/token/refresh/   | Refresh access token
GET    | /api/cars/            | List all cars
POST   | /api/cars/            | Create a new car
GET    | /api/customers/       | List all customers
POST   | /api/customers/       | Create a new customer
GET    | /api/bookings/        | List all bookings
POST   | /api/bookings/        | Create a new booking
GET    | /api/available-cars/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD | List available cars in date range

Note: 
All GET, POST, PUT, DELETE requests (except login) require Authorization header:
Authorization: Bearer your_access_token


Models
------
Car
- id: AutoField (Primary Key)
- make: CharField
- model: CharField
- year: CharField
- available: BooleanField (default=True)

Customer
- id: AutoField (Primary Key)
- name: CharField
- email: EmailField (Unique)
- license_number: CharField

Booking
- id: AutoField (Primary Key)
- car: ForeignKey to Car
- customer: ForeignKey to Customer
- start_date: DateField
- end_date: DateField


Postman API Testing
-------------------
1. First call /api/token/ with username and password.
2. Copy the access token.
3. Add it to every request's Authorization Header:

Example:
Key: Authorization
Value: Bearer eyJ0eXAiOiJKV1QiLCJh...

Validation and Features
------------------------
- A car cannot be double booked.
- Cars available during a date range are fetched dynamically.
- JWT Authentication secured APIs.
- Django Admin Panel for manual operations.


===============
