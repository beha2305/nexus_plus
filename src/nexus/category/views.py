from django.shortcuts import render
from .models import Category
from nexus.geo.models import City
from nexus.product.models import Product, ProductImage
from nexus.product import services
def category(request):
    city_id = request.GET.get("city")
    category_id = request.GET.get("category")
    categories = Category.objects.all()
    products = services.one_product(city_id= city_id, category_id=category_id)
    cities = City.objects.all()
    ctx = {
        "categories" : categories,
        "products" : products,
        "cities" : cities
    }
    return render(request, 'category.html', ctx)

def category_search(request, category_id):
    products = services.one_product(category_id= category_id)

    ctx = {
        "products" : products
    }
    return render(request, 'category.html', ctx)

