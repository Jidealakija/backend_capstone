from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProductSerializer, CartSerializer, CartitemsSerializer
from .models import Product, Cart, Cartitems
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class ProductHomePage(APIView):
    def get(self, request, format=None, *args, **Kwargs):
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        new_product = ProductSerializer(data=request.data)
        new_product.is_valid(raise_exception=True)
        new_product.save()
        return Response({'Success': 'Product has been added successfully!'}, status=status.HTTP_201_CREATED)
    


class ProductDetailPage(APIView):
    def get(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        serialized_product = ProductSerializer(single_product)
        return Response(serialized_product.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        serialized_product = ProductSerializer(single_product, data=request.data, partial=True)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response('Update successful', status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        single_product.delete()
        return Response('Product has been successfully deleted', status=status.HTTP_204_NO_CONTENT)
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)