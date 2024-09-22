# vk_assessment

# Customer Orders Django Project

This project is a Django-based web application that manages customers and their orders. The system allows admins to manage customer information and their associated order details through the Django admin interface. Additionally, the application provides a view to display the top 5 customers who have spent the most in the last 6 months.

## Features

- **Customer Management**: Admin can add, edit, and delete customers.
- **Order Management**: Admin can enter customer orders inline with customer data.
- **Top Customers**: View the top 5 customers who have spent the most in the last 6 months.
- **Django Admin**: Manage customers and orders through the Django admin panel.

## Requirements

- Python 3.x
- Django 4.x (or compatible version)
- Other dependencies listed in `requirements.txt`

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/stormshadow47/vk_assessment.git
cd django_project_q3/django_project

```
### 2. Enter Virtual Environment inside the project

```bash
.\django_project\Scripts\activate

```

### 3. Install dependecies

```bash
pip install -r requirements.txt

```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py runserver

```

### 6. Run the development server

```bash
python manage.py runserver

```

#### 7. Access the application

Open your browser and navigate to http://localhost:8000/admin/ to access the Django admin interface.
Use your superuser credentials to log in and manage customers and orders.

### Usage

Admin Interface: The admin interface is used to manage customers and their associated orders.
Navigate to /admin/ to manage records.
Customers and Orders are linked. You can add orders directly while adding/editing a customer.

Top Customers View: A view to display the top 5 customers based on their total spending in the last 6 months.
Visit /orders/top-customers/ to see the list.

### Dependencies:

Django: The web framework used to develop the application.
Python: The programming language used for development.





