from django.db import models
from users.models import CustomUser

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="seller_profile")
    store_name = models.CharField(max_length=256)
    store_description = models.TextField(blank=True, null=True)
    store_logo = models.ImageField(upload_to='store_logos/', blank=True, null=True)
    store_address = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user.is_seller = True
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store_name} - {self.user.username}"
    

class BusinessDocuments(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=100) #liscense or other docs
    document_file = models.FileField(upload_to='business_doc/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.document_type } - { self.seller.store_name }"
    

class BankDetails(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="bank_details")
    account_holder_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50, unique=True)
    ifsc_code = models.CharField(max_length=20)
    upi_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{ self.seller.store_name } - {self.account_number }"

    