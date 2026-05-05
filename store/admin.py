from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html

# Register your models here.

#Customize the list page
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    #adding computed column
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'In Stock'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10    
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist') 
            + '?' 
            + urlencode({
                'customer_id': str(customer.id)
                }))
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']    

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']    

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?' 
            + urlencode({
                'collection_id': str(collection.id)
                }))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
         
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))

