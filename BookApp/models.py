from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    pages = models.IntegerField()
    pdf = models.FileField(upload_to="media")

