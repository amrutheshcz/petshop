from django.db import models


class Student (models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=25)




