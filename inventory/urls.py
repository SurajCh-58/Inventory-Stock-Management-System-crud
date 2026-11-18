from django.urls import path,include
from inventory.views import SupplierView,ProductView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'supplier',SupplierView,basename='supplier')
router.register(r'product',ProductView,basename='product')

urlpatterns = [
    path('',include(router.urls))    
]
