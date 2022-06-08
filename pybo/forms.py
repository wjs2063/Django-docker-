from django import forms
from .models import lotto


class lottoform(forms.Form):
    name=forms.CharField(max_length=10)
    number=forms.IntegerField()
    create_date=forms.DateTimeField()

