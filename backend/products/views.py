from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
# Create your views here.


#categoryviewsets:

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ permissions.AllowAny ]

#Productviewset:

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def get_queryset(self):
        """ for sellers only there products
            user see all products
        """
        user = self.request.user
        if hasattr(user, 'seller'):
            return Product.objects.filter(seller=user.seller)
        return Product.objects.all()
    
    def perform_create(self, serializer):
        """
        set seller automatically when creating a product.
        """
        serializer.save(seller=self.request.seller)

#productimageviewset:
class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [ permissions.IsAuthenticated ]

#Inventorylogview:
class InventoryLogView(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    