from django.db import models

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField()
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    unit_price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)