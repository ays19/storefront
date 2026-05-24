# 🛒 Storefront — Production-Grade E-Commerce REST API

A fully production-ready e-commerce backend built with **Django REST Framework**, deployed on **Railway**, containerized with **Docker**, and engineered with real-world backend practices including async task processing, JWT authentication, Redis caching, performance profiling, and automated testing.

> Built to demonstrate backend engineering depth — not just CRUD.

🔗 **Live API:** [sharar-prod.up.railway.app](https://sharar-prod.up.railway.app/store)  
📦 **GitHub:** [github.com/ays19/storefront](https://github.com/ays19/storefront)

---

## ⚡ What Makes This Different

Most Django projects stop at basic CRUD. This one goes further:

- 🔐 **JWT authentication** with Djoser — register, login, token refresh, user profile
- 🛒 **UUID-based cart system** — carts can't be enumerated or guessed by clients
- ⚛️ **Atomic order transactions** — cart-to-order conversion is fully atomic; no partial data
- 🗄️ **Django ORM optimization** — `annotate()`, `select_related()`, `prefetch_related()`, `only()`, and `bulk_create()` used throughout to minimize queries and maximize performance
- 📡 **Django Signals** — order creation triggers decoupled downstream events
- 👥 **Group-based permissions** — scalable access control, not per-user assignments
- ⚙️ **Celery + Redis** — async background tasks with scheduled jobs via Celery Beat
- 📊 **Silk profiling** — every SQL query tracked; N+1 problems caught before production
- 🚀 **Locust load testing** — realistic traffic simulation with weighted task distribution
- 🐳 **Docker Compose** — full 7-service local environment in one command
- ☁️ **Railway deployment** — live production API with automated deploy pipeline

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 6.0.4 + Django REST Framework |
| ORM | Django ORM (annotations, select_related, prefetch_related, bulk_create) |
| Database | MySQL 8.0 |
| Cache & Broker | Redis |
| Auth | JWT (SimpleJWT + Djoser) |
| Async Tasks | Celery + Celery Beat |
| Task Monitor | Flower |
| Profiling | Django Silk |
| Load Testing | Locust |
| Testing | Pytest + pytest-django |
| Email (dev) | smtp4dev |
| Containerization | Docker + Docker Compose |
| Deployment | Railway (Nixpacks) |
| Static Files | WhiteNoise |

---

## 🏗️ Architecture Overview

```
storefront/
├── store/               # Core business logic — products, orders, carts, customers
│   ├── models.py        # Domain models with UUID, signals, custom permissions
│   ├── views.py         # ViewSets with filtering, search, sorting, pagination
│   ├── serializers.py   # Nested serializers, computed fields, validation
│   ├── permissions.py   # Custom permission classes
│   ├── filters.py       # django-filter integration
│   ├── signals/         # Order created signal
│   ├── admin.py         # Fully customized admin panel
│   └── tests.py         # Pytest test suite
├── core/                # Custom User model, user signals, Djoser serializers
├── playground/          # Celery task demos
├── tags/                # Generic relationships via ContentTypes
├── likes/               # Generic like system
├── locustfiles/         # Load testing scenarios
└── storefront/
    ├── settings/
    │   ├── common.py    # Shared config — JWT, Celery, logging, email
    │   ├── dev.py       # Local dev overrides
    │   └── prod.py      # Production config — env vars, CSRF, console logging
    ├── celery.py        # Celery app config
    └── wsgi.py
```

---

## 🔑 Key Engineering Decisions

### Django ORM Optimization
```python
# Annotating querysets instead of extra queries
Collection.objects.annotate(products_count=Count('products'))

# Avoiding N+1 with select_related and prefetch_related
Cart.objects.prefetch_related('items__product').all()
Customer.objects.select_related('user').all()

# Bulk insert instead of N individual queries
OrderItem.objects.bulk_create(order_items)

# Fetch only needed fields
Customer.objects.only('id').get(user_id=user.id)
```

### UUID Cart IDs
```python
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
```
Integer IDs are sequential and guessable. UUIDs make cart enumeration impossible — a deliberate security choice.

### Atomic Order Creation
```python
def save(self, **kwargs):
    with transaction.atomic():
        order = Order.objects.create(customer=customer)
        OrderItem.objects.bulk_create(order_items)
        Cart.objects.filter(pk=cart_id).delete()
        order_created.send_robust(self.__class__, order=order)
```
Cart-to-order conversion is wrapped in a transaction. If anything fails, nothing is committed. `bulk_create` replaces N individual inserts with one query.

### Decoupled Signals
```python
# core/signals/handlers.py
@receiver(order_created)
def on_order_created(sender, **kwargs):
    print(kwargs['order'])  # send email, trigger webhook, log — decoupled

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])
```
Business logic is decoupled from the signal sender. The order serializer doesn't need to know what happens after an order is created.

### Group-Based Permissions
```python
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')
```
Permissions are assigned to Groups, not individual users. Adding a user to `Content Manager` gives them all required permissions instantly.

### User Data Isolation
```python
def get_queryset(self):
    if user.is_staff:
        return Order.objects.all()
    customer_id = Customer.objects.only('id').get(user_id=user.id)
    return Order.objects.filter(customer_id=customer_id)
```
Users can only see their own orders. Staff sees everything. Enforced at the queryset level — not in the view.

---

## 🌐 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `store/products/` | No | List products with filter/search/sort/pagination |
| GET | `store/products/{id}/` | No | Single product with images |
| GET | `store/products/{id}/reviews/` | No | Product reviews |
| POST | `store/products/{id}/images/` | Admin | Upload product image |
| GET | `store/collections/` | No | Collections with product count |
| POST | `store/carts/` | No | Create cart (returns UUID) |
| GET/POST | `store/carts/{id}/items/` | No | View/add cart items |
| PATCH | `store/carts/{id}/items/{id}/` | No | Update item quantity |
| GET/POST | `store/orders/` | ✅ JWT | List own orders / place order |
| GET/PUT | `store/customers/me/` | ✅ JWT | View/update own profile |
| GET | `store/customers/{id}/history/` | ✅ Permission | Customer order history |
| POST | `auth/users/` | No | Register new user |
| POST | `auth/jwt/create/` | No | Get access + refresh tokens |
| POST | `auth/jwt/refresh/` | No | Refresh access token |
| GET | `auth/users/me/` | ✅ JWT | Current user info |

### Filtering Examples
```
store/products/?collection_id=3
store/products/?unit_price__gt=20&unit_price__lt=100
store/products/?search=coffee
store/products/?ordering=-unit_price
store/products/?page=2
```

---

## 🔐 Authentication Flow

```
POST /auth/users/          → Register
POST /auth/jwt/create/     → Get JWT token
Authorization: JWT <token> → Use in every protected request
POST /auth/jwt/refresh/    → Refresh expired token
```

JWT config:
```python
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3)
}
```

---

## ⚙️ Background Tasks — Celery

```python
# playground/tasks.py
@shared_task
def notify_customers(message):
    print('Sending 10k emails...')
    sleep(10)
    print('Emails were successfully sent!')
```

Scheduled via Celery Beat:
```python
CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task': 'playground.tasks.notify_customers',
        'schedule': crontab(day_of_week=1, hour=7, minute=30),
        'args': ['Hello, customers!']
    }
}
```

Monitor at **Flower dashboard** → `localhost:5555`

---

## 🐳 Running Locally with Docker

```bash
git clone https://github.com/ays19/storefront.git
cd storefront
chmod +x docker-entrypoint.sh wait-for-it.sh
docker-compose up --build
```

**Services started:**

| Service | URL |
|---------|-----|
| Django API | http://localhost:8000 |
| Admin Panel | http://localhost:8000/admin |
| Flower (Celery) | http://localhost:5555 |
| smtp4dev (Email) | http://localhost:5000 |
| Silk (Profiler) | http://localhost:8000/silk |

Default superuser: `admin` / `admin1234`

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🚀 Performance Testing with Locust

```bash
locust -f locustfiles/browse_products.py
```

Open `http://localhost:8089` and simulate concurrent users hitting:
- Product list with collection filters
- Individual product detail pages
- Add-to-cart operations

Task weights reflect realistic traffic — product detail views are 4x more frequent than list views.

---

## 📊 Profiling with Silk

Every request is profiled in development. Access at `/silk/` to inspect:
- SQL query count per request
- Slow query detection
- Request/response timeline

Example optimization caught by Silk:
```python
# Before — N+1 queries (11 queries for 10 products)
queryset = Product.objects.all()

# After — 2 queries total
queryset = Product.objects.prefetch_related('images').all()
```

---

## ☁️ Deployment

Deployed on **Railway** using Nixpacks (no Dockerfile needed in production).

```toml
# railway.toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt && python manage.py collectstatic --noinput"

[deploy]
startCommand = "gunicorn storefront.wsgi:application --bind 0.0.0.0:$PORT --workers 2"
releaseCommand = "python manage.py migrate && python manage.py create_superuser_env"
```

Every push to `main` triggers an automatic deploy.

---

## 👤 Author

**Ahsan Yasir Sharar**  
Backend Engineer — Django · REST APIs · System Design  

[![GitHub](https://img.shields.io/badge/GitHub-ays19-181717?style=flat&logo=github)](https://github.com/ays19)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/ahsan-yasir-sharar-71670a1a2/)

---

⭐ Star this repo if you found it useful.
