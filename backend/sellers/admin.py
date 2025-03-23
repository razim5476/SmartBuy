from django.contrib import admin
from backend.settings import JAZZMIN_SETTINGS
from .models import *

# Register your models here.

class SellerAdminSite(admin.AdminSite):
    """Custom Seller Admin Panel"""
    site_header = "Seller Dashboard"
    site_title = "Seller Admin"
    index_title = "Manage Your Store"

    def has_permission(self, request):
        """Allow access only to users marked as sellers"""
        return request.user.is_active and request.user.is_seller

seller_admin_site = SellerAdminSite(name="seller_admin")

seller_admin_site.register(Seller)
seller_admin_site.register(BankDetails)
seller_admin_site.register(BusinessDocuments)