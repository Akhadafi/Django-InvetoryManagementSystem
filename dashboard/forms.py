from django import forms
from dashboard.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity"]
