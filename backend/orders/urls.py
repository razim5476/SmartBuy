from django.urls import path
from .views import OrderViewSet, OrderDetailView


urlpatterns = [
    path('orders/',OrderViewSet.as_view({"post":"create"}), name="create-order"),
    path('orders/<int:pk>/',OrderDetailView.as_view({"get": 'retrieve'}), name="order-detail"),
]
