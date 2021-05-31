from rest_framework import serializers, viewsets
from .models import Product, Food
from .serializers import ProductSerializer, FoodSerializer
from rest_framework.response import Response


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer