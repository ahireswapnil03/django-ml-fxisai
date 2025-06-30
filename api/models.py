from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    hashed_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    image_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
