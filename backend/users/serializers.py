from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


#User serializer:
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'phone_number', 'profile_picture',
            'date_of_birth', 'gender', 'is_email_verified', 'wallet_balance',
            'reward_points', 'is_seller'
        ]

#User registration:
class UserRegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = [
            'email', 'username', 'password', 'phone_number'
        ]
        
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
#UserLogin:
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": CustomUserSerializer(user).data
            }
        raise serializers.ValidationError("Invalid Credentials")