from django.contrib import admin
from .models import lotto



# admin.site.Register(lotto)
# Register your models here.

class Lottoadmin(admin.ModelAdmin):
    search_fields=['name']
admin.site.register(lotto,Lottoadmin)