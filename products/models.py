from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    img = models.URLField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name