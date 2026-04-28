from django.shortcuts import render
from django.db.models import Q,F # Q for using or operator etc
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    
    #product = Product.objects.filter(pk=0).first() #can use try-catch but it is better
    #exists = Product.objects.filter(pk=0).exists()
    #queryset = Product.objects.filter(unit_price__range=(20, 30)) #can not use logical operations here, cause it is bolean expresion. so use keyword arguments like gt=greatar than ,gte= greater equal etc. for more search queryset api then fiels lookup
    #queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
    #queryset = Product.objects.filter(title__icontains='coffee') #i for remove case sensitivity
    #queryset = Product.objects.filter(last_update__year=2021)
    queryset = Product.objects.filter(description__isnull=True)
    
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
    product = Product.objects.earliest('unit_price')  #also have latest method
                                      

    #return render(request, 'hello.html', {'name': 'Sharar', 'products': list(queryset)}) 
    return render(request, 'hello.html', {'name': 'Sharar', 'product': product}) 
