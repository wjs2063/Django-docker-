from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class lotto(models.Model):
    name=models.CharField(max_length=10)
    
    number=models.IntegerField(" 금액을 입력하세요 ",default=1000,help_text="천원에서 20만원까지 입력하세요")
    create_date=models.DateTimeField()

