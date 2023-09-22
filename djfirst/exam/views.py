from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def examname(request):
    s="<a href='http://localhost:8000/exam/results/'>Result</a>\
    <h1>Its my first exam</h1>"
    return HttpResponse(s)
def result(request):
    q='what is your father name?'
    a='S'
    b='R'
    c='B'
    d='SR'
#Here i create dictionary
    D2={
        'que':q,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    res=render(request,'exam/test_template.html',D2)
    return res
def question(request):
    q='what is your name?'
    a='Sudip'
    b='Raja'
    c='Bimal'
    d='SRK'
#Here i create dictionary
    D1={
        'que':q,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    ans=render(request,'exam/test_template.html',D1)#Here i pass the dict
    return ans