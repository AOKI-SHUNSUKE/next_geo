import uuid

from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + "-" + self.title


class Coordinate(models.Model):
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    mac_id = models.CharField(max_length=60,default='No Mac')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.mac_id) + "=>" + self.latitude + ":"+self.longitude
