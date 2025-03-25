from rest_framework import viewsets,permissions,status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
# Create your views here.

#cart view:

class CartViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
#add to cart api:
class AddToCartView(APIView):
    permission_classes = [ permissions.IsAuthenticated ]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            product = Product.objects.filter(id=product_id).first()
            if not product:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
            
            cart, created = Cart.objects.get_or_create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return Response({"message": "Item added to cart"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#remove from cart:
class RemoveFromCartView(APIView):
    permission_classes = [ permissions.IsAuthenticated ]

    def delete(self, request, product_id):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if not cart_item:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)
        
        cart_item.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_200_OK)
    

#wishlist api:

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WhishListSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def get_queryset(self):
        return Whishlist.objects.filter(user=self.request.user)
    