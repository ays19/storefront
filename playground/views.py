from django.shortcuts import render
from django.db.models import Q,F # Q for using or operator etc
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem


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
    result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))

    #return render(request, 'hello.html', {'name': 'Sharar', 'orders': list(queryset)}) 
    return render(request, 'hello.html', {'name': 'Sharar', 'result': result}) 
    #return render(request, 'hello.html', {'name': 'Sharar', 'products': list(product)}) 
