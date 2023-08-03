from django.db import models
from datetime import datetime


# Create your models here.
class Months(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    datetime = models.DateTimeField(default=datetime.now)
    month = models.ForeignKey(Months, on_delete=models.CASCADE)
