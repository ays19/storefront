from django.shortcuts import render
from django.db.models import Q, F, Func  # Q for using or operator etc, F for refference fields
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer, Product, Order, OrderItem
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    
    #product = Product.objects.filter(pk=0).first() #can use try-catch but it is better
    #exists = Product.objects.filter(pk=0).exists()
    #queryset = Product.objects.filter(unit_price__range=(20, 30)) #can not use logical operations here, cause it is bolean expresion. so use keyword arguments like gt=greatar than ,gte= greater equal etc. for more search queryset api then fiels lookup
    #queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
    #queryset = Product.objects.filter(title__icontains='coffee') #i for remove case sensitivity
    #queryset = Product.objects.filter(last_update__year=2021)
    #queryset = Product.objects.filter(description__isnull=True)
    
    #complex query
    #queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)  # Products: inventory < 10 AND price < 20
    #another way
    #queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)  # Products: inventory < 10 AND price < 20
    #queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))  # Products: inventory < 10 OR price < 20
    #Using F Object
    #queryset = Product.objects.filter(inventory=F('Collection_id'))
    #Sorting
    #queryset = Product.objects.order_by('title')  # '-title' for descending order
    #queryset = Product.objects.order_by('unit_price', '-title').reverse()  #can sort by multiple field. the reverse() change the order direction. here for unit price is desc and for -title is asc
    #queryset = Product.objects.filter(Collection__id=1).order_by('unit_price')
    #product = Product.objects.order_by('unit_price')[0]
    #product = Product.objects.earliest('unit_price')  #also have latest method

     #limiting result
    #queryset = Product.objects.all()[5:10]                                 
    
    #Selecting Fields to Query
    #queryset = Product.objects.values('id', 'title', 'collection__title')                                 
    #queryset = Product.objects.values_list('id', 'title', 'Collection__title')                                 
    #queryset = OrderItem.objects.values('product__id').distinct()                                 
    #product = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')                                 
    #Deferring Fields
    #queryset = Product.objects.only('id', 'title')                      
    #queryset = Product.objects.defer('description')                      
    #Selecting releated object 
    #queryset = Product.objects.select_related('collection').all()                      
    #Prefetch releated object
    #queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()                      
    #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
   #Aggregating Objects
    #result = Product.objects.filter(collection__id=100).aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))
    #result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))
    #return render(request, 'hello.html', {'name': 'Sharar', 'orders': list(queryset)}) 
    #Annotating objects
    #queryset = Customer.objects.annotate(is_new=Value(True)) #we can not pass bolean value here. so that import value.
    #queryset = Customer.objects.annotate(new_id=F('id') + 1)
    #Calling database Functios
    #queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    #Using Concat Class
    #queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))  #Using concat class code make sorter, the upper of this code is not use concat class but result is same
    #Grouping data
    #queryset = Customer.objects.annotate(orders_count=Count('order'))
    #Expression wrapper
    #discounted_price=ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    #queryset = Product.objects.annotate(discounted_price=discounted_price)
    #Querying Generic Relationships
    content_type = ContentType.objects.get_for_model(Product)
    

    return render(request, 'hello.html', {'name': 'Sharar', 'tags': list(queryset)}) 
    #return render(request, 'hello.html', {'name': 'Sharar', 'products': list(product)}) 
