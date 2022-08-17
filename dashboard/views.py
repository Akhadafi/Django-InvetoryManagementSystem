from django.shortcuts import render, redirect
from dashboard.models import Product
from django.contrib.auth.decorators import login_required
from dashboard.forms import ProductForm

# Create your views here.
@login_required
def index(request):
    return render(request, "dashboard/index.html")


def staff(request):
    return render(request, "dashboard/staff.html")


def product(request):
    items = Product.objects.all()
    # items = Product.objects.raw("SELECT * FROM dashboard_product")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = ProductForm()
    context = {
        "items": items,
        "form": form,
    }
    return render(request, "dashboard/products.html", context)


def product_delet(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-product")
    return render(request, "dashboard/products_delete.html")


def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = ProductForm(instance=item)
    context = {"form": form}
    return render(request, "dashboard/products_edit.html", context)


def order(request):
    return render(request, "dashboard/order.html")
