from .models import CustomUser
from .serializers import *
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response


#Registration View
class UserRegistrationView(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer 
    permission_classes = [permissions.AllowAny]  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "User Registered successfully"}, status=status.HTTP_201_CREATED)
    

#Login View
class UserLoginView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

#Profile View (Get, Update, Delete)
class UserProfileView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    
    def update(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request):
        request.user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
