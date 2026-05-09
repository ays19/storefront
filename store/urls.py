from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('products/', views.ProductList.as_view()), #as_view method convert the class regular function based view 
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view()),
]   
 