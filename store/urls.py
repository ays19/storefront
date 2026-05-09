from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('products/', views.ProductList.as_view()), #as_view method convert the class regular function based view 
    path('products/<int:id>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
]   
 