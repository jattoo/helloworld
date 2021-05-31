from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    manufactured = models.DateTimeField(auto_now_add=True)

class Food(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=100)
    preparations = models.TextField(blank=True)
