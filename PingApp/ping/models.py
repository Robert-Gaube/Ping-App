from django.db import models

class Setup(models.Model):
     name = models.CharField(max_length=50)
     ip = models.CharField(max_length=30)
