from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_option = request.GET.get('sort', 1)
    if sort_option == 'max_price':
        phones_query = Phone.objects.order_by('-price').all()
    elif sort_option == 'min_price':
        phones_query = Phone.objects.order_by('price').all()
    elif sort_option == 'name':
        phones_query = Phone.objects.order_by('name').all()
    else:
        phones_query = Phone.objects.all()
    context = {
        'phones': phones_query
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
