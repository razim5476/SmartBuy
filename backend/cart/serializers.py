from  rest_framework import serializers
from .models import *


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = [ 'id','product','quantity','total_price' ]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [ 'id', 'user', 'items', 'created_at' ]

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class WhishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whishlist
        fields = [ 'id', 'user', 'product', 'added_at' ]
