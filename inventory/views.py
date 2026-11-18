from rest_framework.viewsets import ModelViewSet
from inventory.serializers import SupplierSerializer,ProductSerailizer
from inventory.models import Supplier,Product
# Create your views here.

class SupplierView(ModelViewSet):
    serializer_class=SupplierSerializer
    queryset=Supplier.objects.all()

class ProductView(ModelViewSet):
    serializer_class=ProductSerailizer
    queryset=Product.objects.all()