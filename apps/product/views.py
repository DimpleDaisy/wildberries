
from rest_framework import permissions
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer



class ProductlistAPIView(generics.ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    permissions_classes = [permissions.AllowAny]

