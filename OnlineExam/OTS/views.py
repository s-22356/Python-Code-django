from django.shortcuts import render
from django.http import HttpResponsRedirect,HttpResponsResponse
from OTS.models import Question
# Create your views here.
def newquestion(request):
    res=render(request,'OTS/newquestion.html')
    return res
def savequestion(request):
    question=Question()
    question.que=request.POST['question']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponsRedirect('http://localhost:8000/OTS/view-questions/')
    def viewQuestions(request):
         