from rest_framework import serializers
from .models import Product, Cart, Cartitems


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['product', 'quantity']