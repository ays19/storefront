from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

#router = SimpleRouter()  #create router onject
router = DefaultRouter()  #create router object
router.register('products', views.ProductViewSet) #register the viewset with the router
router.register('collections', views.CollectionViewSet)  #register the viewset with the router

#URL Configuration
urlpatterns = router.urls