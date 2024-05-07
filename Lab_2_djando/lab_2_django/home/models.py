from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(null=True)
    views = models.IntegerField(null=True)