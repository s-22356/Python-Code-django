from django.urls import path
from .views import examname,result,question
urlpatterns=[path('examtest/',examname),
    path('results/',result),
    path('question/',question)]