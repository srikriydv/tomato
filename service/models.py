from django.db import models

# Create your models here.
class Login(models.Model):
    image = models.FileField(upload_to="image/",max_length=250,unique=True,null= True,default=None)
    