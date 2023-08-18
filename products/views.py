from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# we need to tell django to call this function
# when we visit our /products url
# map this url /products to the index function
def index(req):
    products = Product.objects.all()
    return render(req, "index.html", {"products": products})


def new(req):
    return HttpResponse(f"from new product")

