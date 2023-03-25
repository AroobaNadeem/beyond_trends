from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField( max_length=50)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    feedback=models.TextField()
    date=models.DateField()

