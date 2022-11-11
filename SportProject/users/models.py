from django.db import models

class Users(models.Model):
    idUser = models.AutoField(primary_key = True, unique=True)
    Login = models.CharField(max_length = 45, default="DefauldLogin")
    Password = models.CharField(max_length=45, default="123")
    Role = models.SmallIntegerField(default=0)
    LastLogin = models.DateTimeField(auto_now = True)
    ImageUsers = models.ImageField(default="No") # Set the path for the media folder
    Mail = models.EmailField(100, default="test@mail.ru")
    UserCity = models.CharField(max_length=45, default="Ставрополь")
# Create your models here.
