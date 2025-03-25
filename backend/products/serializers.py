from rest_framework import serializers
from .models import *


#category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#product image serializer:
class ProductImageSerializer(serializers.ModelSerializer):
    model = ProductImage
    fields = '__all__'

#product serializer:
class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

#inventory log serializers:
class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = '__all__'
