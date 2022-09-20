from django.contrib import admin
from master import models

admin.site.register(models.Address)
admin.site.register(models.Location)

