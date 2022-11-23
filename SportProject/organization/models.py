from django.db import models
class Organization(models.Model):
    IdOrganization = models.AutoField(primary_key=True, unique=True)
    Title = models.CharField(default=" ",max_length=45)
    Description = models.CharField(default="Описание организации", max_length=255)
    Evaluation = models.FloatField(default=0, max=10)
# Create your models here.
