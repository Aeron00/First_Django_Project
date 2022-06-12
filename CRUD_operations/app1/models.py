from django.db import models

# Create your models here.

class reg(models.Model):
    uname=models.CharField(max_length=50)
    uemail=models.EmailField(max_length=50)
    upass=models.CharField(max_length=50)
    uadd=models.CharField(max_length=200)

class login(models.Model):
    uname=models.CharField(max_length=50)
    upass=models.CharField(max_length=50)
    