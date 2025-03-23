from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationView, UserLoginView,UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view({'post': 'create'}), name='register'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profile'),
]
