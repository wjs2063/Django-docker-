from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .crawl import crawling
# Create your models here.

class lotto(models.Model):
    name=models.CharField(max_length=10)
    money=models.IntegerField()
    create_date=models.DateTimeField()
    def __str__(self):
        return self.name

