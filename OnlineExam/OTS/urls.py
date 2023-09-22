from django.urls import path
from .views import *
urlpatterns = [
    path('view-questions/',viewQuestions)
    path('newquestions/',newquestion),
    path('savequestions/',savequestion),
]