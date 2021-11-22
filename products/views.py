from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator


def nav(request):
    findAllProducts = Category.objects.all()
    context = {'categories': findAllProducts}
    return render(request, 'base.html', context)

def filterCategory(request, id):
    findAllProducts = Product.objects.all()
    categories = Category.objects.all()
    products = findAllProducts.filter(category_id=id)
    search = request.GET.get('search')
    if search:
        products = findAllProducts.filter(name__icontains=search)
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'products/home.html', {'products': products, 'categories': categories})


def index(request):
    return render(request, 'products/index.html')

def home(request):
    findAllProducts = Product.objects.all()
    search = request.GET.get('search')
    if search:
        findAllProducts = findAllProducts.filter(name__icontains=search)
    paginator = Paginator(findAllProducts, 15)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'products': products, 'categories': categories})

def findProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/findProduct.html', {'product': product})
