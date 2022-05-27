from django.db import models


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=120)

    last_name = models.CharField(max_length=120)
    email=models.EmailField()
    phone_number=models.IntegerField(max_length=10)

    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120)

    def __str__(self):
        return  self.first_name
# Create your models here.

