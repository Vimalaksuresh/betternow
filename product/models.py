from django.contrib.auth import get_user_model
from django.db import models
from master.models import TimeStamp
from django.db.models import F, Count, Sum

from customer.models import Customer



USER = get_user_model()


class CategoryModel(TimeStamp, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    secondary_unit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    conversion_rate = models.FloatField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class ProductModel(TimeStamp, models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="products", default="default/products.jpg")
    private = models.BooleanField(default=False)
    stock = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(
        USER, on_delete=models.SET_NULL, null=True, blank=True, default="1"
    )
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, null=True, blank=True, default="1"
    )

    def __str__(self):
        return f"{self.name}"


class Cart(TimeStamp, models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)

    def total(self):
        cart_total = (
            CartItem.objects.filter(Cart=self, status=True)
            .annotate(amount=F("product_price") * F("quantity"))
            .aggregate("amount")
            .get("amount_sum")
        )
        return cart_total

    def __str__(self):
        return f"user: {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default="1")
