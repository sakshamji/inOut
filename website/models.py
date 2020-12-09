from django.db import models

# Create your models here.
class Public(models.Model):
    name  = models.CharField(max_length= 100)
    father_name = models.CharField(max_length= 100)
    mother_name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 100) 
    religion = models.CharField(max_length= 100)
    sex  = models.CharField(max_length= 10)
    nationality = models.CharField(max_length= 10)

    def __str__(self):
        return self.name

class Private(models.Model):
    dob = models.DateField()
    phone = models.IntegerField()
    category = models.CharField(max_length= 10)
    address = models.TextField(max_length= 100)
    city = models.CharField(max_length= 100)
    pincode = models.IntegerField()
    state = models.CharField(max_length= 100)
    father_occupation = models.CharField(max_length= 100)
