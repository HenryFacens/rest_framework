from django.db import models

class Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()