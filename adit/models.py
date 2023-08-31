from django.db import models

class students(models.Model):
    
    Name = models.CharField(max_length=10)
    Age = models.CharField(max_length=2)
    Mobile = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Trade = models.CharField(max_length=10)
    Location = models.CharField(max_length=50)

# Create your models here.
