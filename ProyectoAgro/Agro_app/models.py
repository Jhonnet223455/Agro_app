from django.db import models


class user(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=True, unique=True)
    password = models.CharField(max_length=50)
    wallet = models.CharField(max_length=50)
    Birthdate = models.DateField()

    class Meta:
        db_table = 'user'

class agricultural_product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'agricultural_product'    

class transaction(models.Model):
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_agricultural_product = models.ForeignKey(agricultural_product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'

class calification(models.Model):
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_agricultural_product = models.ForeignKey(agricultural_product, on_delete=models.CASCADE)
    calification = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'calification'


class harvester(models.Model):
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_agricultural_product = models.ForeignKey(agricultural_product, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    image = models.FileField()
    ubication = models.CharField(max_length=50)
    telephone = models.IntegerField()   

    class Meta:
        db_table = 'harvester'
             