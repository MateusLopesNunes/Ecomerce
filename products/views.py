from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator


def home(request):
    findAllProducts = Product.objects.all()
    search = request.GET.get('search')
    if search:
        findAllProducts = findAllProducts.filter(name__icontains=search)
    paginator = Paginator(findAllProducts, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'products/index.html', {'products': products, 'categories': categories})

def findProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/findProduct.html', {'product': product})
