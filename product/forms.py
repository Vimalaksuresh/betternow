from django import forms
from product.models import ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "price",
            "description",
            "category",
            "available",
            "unit",
            "image",
        ]


class AddToCartForm(forms.Form):
    product = forms.IntegerField()
    quantity = forms.IntegerField()
    