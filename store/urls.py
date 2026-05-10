from django.urls import path
#from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

#router = SimpleRouter()  #create router onject
#router = DefaultRouter()  #create router object
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products') #register the viewset with the router
router.register('collections', views.CollectionViewSet)  #register the viewset with the router

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
#URL Configuration
urlpatterns = router.urls + products_router.urls