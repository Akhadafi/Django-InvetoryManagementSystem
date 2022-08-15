from django.shortcuts import render
from dashboard.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, "dashboard/index.html")


def staff(request):
    return render(request, "dashboard/staff.html")


def product(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request, "dashboard/products.html", context)


def order(request):
    return render(request, "dashboard/order.html")
