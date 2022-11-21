from django.db import models

# Create your models here.

class Post(models.Model):
    idPost = models.AutoField(primary_key=True, unique=True)
    Img = models.ImageField()
    Name = models.CharField(max_length=45)
    Location = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    First_Date_Post = models.DateTimeField(auto_now_add=True)
    Edit_Date_Post = models.DateTimeField(auto_now=True)

    class Meta():
         db_table = "Post"
    
