from django.db import models

class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Location(TimeStamp, models.Model):
    lattitude = models.FloatField(max_length=150)
    longitude = models.FloatField(max_length=150)

    def __str__(self) -> str:
        return f"{self.lattitude},{self.longitude}"


class Address(TimeStamp, models.Model):
    building_name = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    post_office = models.CharField(max_length=10)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.building_name},{self.district}-{self.postal_code}"


