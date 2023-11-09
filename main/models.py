from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'farmers'


class Agricultural_product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)        
    stock = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    seller = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'agricultural_products'    


class Order(models.Model):
    user = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='Pending')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'orders' 


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Agricultural_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'orderdetails'