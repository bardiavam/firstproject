from django.db import models
from django.db.models import Model
# Create your models here.


class Category(models.Model) :
    name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Category',null=True,blank=True)
    def __str__(self):
        return self.name

class Products(models.Model) :
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField()
    total = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Products',null=True,blank=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.name
    def total(self):
        if not self.discount:
            return self.price
        elif self.discount:
            total = (self.price * self.discount) /100
            return int(self.price - total)
        return self.total
