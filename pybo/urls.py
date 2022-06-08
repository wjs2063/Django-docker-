from django.urls import path
from . import views 


urlpatterns=[
    path('',views.index),
    path('lotto/',views.lottoview),
    path('result/',views.result,name='result')
]