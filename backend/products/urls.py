from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageView,InventoryLogView

# Create router instance
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-images', ProductImageView, basename='product-image')
router.register(r'inventory-logs', InventoryLogView, basename='inventory-log')

urlpatterns = [
    path('', include(router.urls)),
]
