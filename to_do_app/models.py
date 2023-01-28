from django.db import models

# Create your models here.

class ToDo_Datas(models.Model):
    Content = models.CharField(max_length=100)
    Date = models.DateField()
