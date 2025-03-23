from django.db import models

from sellers.models import Seller

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="subcategories")

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")
    is_primary = models.BooleanField(default=False)


    def __str__(self):
        return f"{ self.product.name } - Image"
    

class InventoryLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventory_log")
    change_type = models.CharField(max_length=10, choices=[("ADD","Added"),("REMOVE","Removed")])
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{ self.product.name } - { self.change_type } { self.quantity_changed }"
    