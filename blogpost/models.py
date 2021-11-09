from django.db import models

# Create your models here.
class sampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()