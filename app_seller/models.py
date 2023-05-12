from distutils.command.upload import upload
from django.db import models


# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=12)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    account_name = models.CharField(max_length =20)
    account_number = models.BigIntegerField()
    ifsc_code = models.CharField(max_length =20)
    status = models.CharField(max_length=30,default='not approved')
    

# class Category(models.Model):
#     Catagoryname=models.CharField(max_length=400)
#     Pets=models.CharField(max_length=400)


   # permission = models.CharField(max_length=10)



class Productss(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_brand = models.CharField(max_length=20)
    product_price = models.BigIntegerField()
    quantity = models.IntegerField()
    discount_price = models.BigIntegerField()
    weight = models.IntegerField()
    product_image = models.ImageField(upload_to='product_image/')
    description = models.CharField(max_length=50)
  #  seller = models.ForeignKey(Signup, on_delete= models.CASCADE)   
