from rest_framework import serializers
from inventory.models import Supplier,Product
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields=['id','name','phone','email']

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','supplier','name','unit_price','stock']