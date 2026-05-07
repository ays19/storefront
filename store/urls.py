from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('products/', views.product_list)
]
