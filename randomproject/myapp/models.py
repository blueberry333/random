from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.TextField()
    month = models.TextField()
    date = models.TextField()
    blood = models.TextField()
    season = models.TextField()
    color = models.TextField()