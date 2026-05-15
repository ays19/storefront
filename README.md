# Storefront

A production-focused e-commerce backend project built with Django, REST APIs, and modern backend engineering practices.

This project focuses on scalable architecture, clean code, API development, performance optimization, and production-ready engineering workflows. Many core features have already been implemented, with additional advanced capabilities currently in development.

---

## Project Overview

This project was built to gain hands-on experience in:

- Backend application architecture
- Database design and optimization
- REST API development
- Authentication and authorization
- Background task processing
- Performance testing and profiling
- Production deployment practices

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- MySQL

### Package Management
- Pipenv

### Async & Background Jobs
- Celery

### Cache & Performance
- Redis
- Silk
- Locust

### Testing
- Pytest

### Deployment
- Heroku

---

## Features Implemented

### Core Django Development
- Django project architecture
- Application modularization
- Models and database relationships
- Django ORM queries
- Database migrations
- Admin panel customization
- Static file management
- Logging and configuration management

### Advanced Database Design
- Relational database modeling
- Generic relationships using Content Types Framework
- Dummy data generation and database seeding

### REST API Development
- RESTful API design
- Class-based views
- Serializers
- Mixins and generic views
- Router-based URL generation
- File upload APIs

### Data Management
- Filtering
- Searching
- Sorting
- Pagination

### Authentication & Security
- Django Authentication System
- JWT Authentication
- Permission-based access control

### Application Architecture
- Signals for decoupled app communication
- Email integration
- Modular backend design
- Clean code practices

---

## Features In Progress

Currently working on:

- Background jobs with Celery
- Caching with Redis
- Performance testing with Locust
- Application profiling with Silk
- Automated testing with Pytest
- Deployment optimization

---

## Project Structure

```bash
storefront/
│
├── storefront/      # Project settings and configuration
├── store/           # Core business logic
├── likes/           # Generic relationships
├── playground/      # Testing and experimentation
├── manage.py
└── Pipfile
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/ays19/storefront.git
cd storefront
```

### Install dependencies

```bash
pipenv install
```

### Activate environment

```bash
pipenv shell
```

### Apply migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run development server

```bash
python manage.py runserver
```

Application will be available at:

```bash
http://127.0.0.1:8000/
```

---

## API Highlights

This project includes APIs for:

- Products
- Collections
- Customers
- Shopping Cart
- Orders
- Reviews
- Authentication
- File Uploads

---

## Engineering Practices Applied

This project follows:

- Clean architecture principles
- Separation of concerns
- Reusable components
- API-first development
- Performance optimization
- Debugging and troubleshooting workflows

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Backend engineering
- Database design
- API architecture
- Authentication systems
- Performance optimization
- Testing strategies
- Deployment workflows

---

## Future Roadmap

Planned improvements:

- Docker containerization
- CI/CD pipeline
- Kubernetes deployment
- Monitoring and observability
- Rate limiting
- API versioning

---

## Author

**ays19**

Software Engineer focused on backend engineering, APIs, system design, and AI-powered applications.

GitHub: https://github.com/ays19

---

⭐ If you find this project useful, feel free to star the repository.
