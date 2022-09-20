from django.contrib import admin
from product import models

admin.site.register(models.ProductModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.Unit)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)



# Register your models here.
