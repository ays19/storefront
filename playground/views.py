from django.shortcuts import render
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
    queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)  # Products: inventory < 10 AND price < 20

    return render(request, 'hello.html', {'name': 'Sharar', 'products': list(queryset)}) 