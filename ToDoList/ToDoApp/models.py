from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 244 )
    descript = models.TextField()
    #deadline = models.TimeField()
    # priority = models.IntegerField()
    def __str__(self) :
        return self.title
