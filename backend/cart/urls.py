from django.urls import path
from .views import CartViewSet, AddToCartView, RemoveFromCartView, WishlistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename="cart")
router.register(r'wishlist', WishlistViewSet, basename="wishlist")

urlpatterns = [
    path('cart/add/', AddToCartView.as_view(), name="add-to-cart"),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name="remove-from-cart"),
]

urlpatterns += router.urls
