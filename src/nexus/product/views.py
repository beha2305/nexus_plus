from django.shortcuts import render
from nexus.category.models import Category
from nexus.geo.models import City
from .models import Product, ProductImage
from . import services
from .forms import ProductForm
def index(request):
    # products = Product.objetcs.all().order_by("-post_date")
    products = services.get_latest_products(6)
    # print(products)
    categories = Category.objects.filter(parent_id=None)
    cities = City.objects.all()

    ctx = {
        "categories" : categories,
        "products" : products,
        "cities" : cities
    }

    return render(request, 'index.html', ctx)


def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        images = request.POST.getlist('file')
        product = form.save()
        for image in images:
            print(image)
            image_form = ProductImage(product= product, image= image)
            image_form.save()
    context = {
        "form": form
    }
    return render(request, 'create.html', context)


def view_details(request, product_id):
    product = services.view_detail(product_id= product_id)
    products = services.get_latest_products(4)
    print(product)
    ctx = {
        "product": product,
        "products": products
    }
    return render(request, 'ads-details.html', ctx)


