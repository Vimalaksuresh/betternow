from django.db import models
from django.contrib.auth.models import AbstractUser
from master.models import Address, TimeStamp


class User(AbstractUser):
    pass


class Profile(TimeStamp, models.Model):
    GENDER_CHOICES = (
        ("m", "Male"),
        ("f", "Female"),
        ("t", "Transgender"),
    )
    first_name = models.CharField(max_length=52)
    last_name = models.CharField(max_length=52)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    age = models.IntegerField()
    qualification = models.CharField(max_length=60)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True
    )
