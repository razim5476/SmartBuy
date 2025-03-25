from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from cart.models import Cart, CartItem
from .serializers import *

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = Order.objects.all()
    permission_classes = [ permissions.IsAuthenticated ]

    def create(self, request):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()

        if not cart:
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items.exists():
            return Response({'error': 'No items in cart'}, status=status.HTTP_404_NOT_FOUND)
        
        total_price = sum(item.total_price() for item in cart_items)

        order = Order.objects.create(user=user, total_price=total_price)

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.total_price())

        cart_items.delete()

        return Response({'message': 'Order placed successfully', "order_id" : order.id}, status=status.HTTP_201_CREATED)
    
class OrderDetailView(viewsets.ViewSet):
    permission_classes = [ permissions.IsAuthenticated ]

    def retrieve(self, request, pk=None):
        try:
            order = Order.object.get(pk=pk, user=request.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

