# Storefront

A production-focused e-commerce backend project built with Django and Django REST framework.

This project was built as part of my backend engineering journey to deeply understand Django, database design, API development, performance optimization, testing, and deployment.

This project is designed to explore real-world backend engineering, focusing on scalable architecture, clean code practices, API development, performance optimization, and production-ready workflows. Many core features have already been implemented, with additional advanced features currently in progress.

---

## Project Goals

This project was built to:

- Master Django fundamentals and architecture
- Understand Django internals and request lifecycle
- Design scalable database models
- Build secure RESTful APIs
- Apply clean code and industry best practices
- Work with background tasks and performance optimization
- Learn production-ready deployment workflows

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

## Features Already Implemented

### Django Core
✅ Project and app architecture  
✅ Models and relationships  
✅ Database migrations  
✅ Django ORM queries  
✅ Django admin customization  
✅ Dummy data generation  
✅ Content Types Framework  
✅ Static file management  
✅ Logging and configuration management  

---

### REST API Development

✅ RESTful API design  
✅ Class-based views  
✅ Serializers  
✅ Mixins  
✅ Generic views  
✅ Routers  
✅ Nested resources  
✅ File upload APIs  

---

### Data Handling

✅ Filtering  
✅ Searching  
✅ Sorting  
✅ Pagination  

---

### Authentication & Security

✅ Django Authentication System  
✅ JSON Web Token (JWT) authentication  
✅ API permissions and access control  

---

### Application Architecture

✅ Signals for decoupled communication  
✅ Email integration  
✅ Modular app design  
✅ Clean architecture practices  

---

## Features In Progress

Currently working on implementing:

- Background jobs with Celery  
- Caching with Redis  
- Performance testing with Locust  
- Application profiling with Silk  
- Automated testing with Pytest  
- Production deployment improvements  

---

## Project Structure

```bash
storefront/
│
├── storefront/       # Main project settings
├── store/            # Core e-commerce logic
├── likes/            # Generic relationships
├── playground/       # Testing and experimentation
├── manage.py
└── Pipfile
```

---

## Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/ays19/storefront.git
cd storefront
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Activate shell

```bash
pipenv shell
```

### 4. Configure database

Create your `.env` file and configure your database settings.

Example:

```env
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

---

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```

Application will run at:

```bash
http://127.0.0.1:8000/
```

---

## API Highlights

This project includes APIs for:

- Products
- Collections
- Customers
- Orders
- Shopping Cart
- Reviews
- File Uploads
- Authentication

---

## Engineering Practices Applied

This project follows:

- Clean code principles
- Modular architecture
- Separation of concerns
- Reusable components
- API-first development
- Performance optimization mindset
- Debugging and troubleshooting workflows

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Real-world Django development
- Database design
- API architecture
- Authentication systems
- Performance optimization
- Testing strategies
- Production deployment

---

## Future Roadmap

Planned improvements:

- Docker support
- CI/CD pipeline
- Kubernetes deployment
- Monitoring and observability
- Rate limiting
- API versioning

---

## Author

**ays19**

Software Engineer focused on backend engineering, Django, APIs, system design, and AI-powered applications.

### Connect with me

GitHub: [Ays19 GitHub](https://github.com/ays19?utm_source=chatgpt.com)

---

⭐ If you found this project useful, feel free to star the repository.
