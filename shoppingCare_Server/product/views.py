from django.shortcuts import render
from itsdangerous import Serializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
  def get(self, request, format=None):
    products = Product.objects.all()[0:4]
    Serializer = ProductSerializer(products, many=True)
    return Response(Serializer.data)