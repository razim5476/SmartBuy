from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=False )
    profile_picture = models.ImageField(upload_to='profile_pic/', default="default.jpg")
    

    date_of_birth = models.DateField(blank=True, null=True)


    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Prefer not to say', 'Prefer not to say')
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    newsletter_subscribed = models.BooleanField(default=False)

    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    reward_points = models.IntegerField(default=0)
    is_seller = models.BooleanField(default=False)


    def __str__(self):
        return self.username
    

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses")
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.street_address}, { self.city }"



