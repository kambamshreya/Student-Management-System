import http
from django.urls import reverse
from http.client import HTTPResponse
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members
# Create your views here.
def index(request):
    student=Members.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'student':student
    }
    return HttpResponse(template.render(context,request))
def addrecord(request):
    n=request.POST["student_name"]
    r=request.POST["roll_no"]
    b=request.POST["branch"]
    s1=Members(student_name=n,roll_no=r,branch=b)
    s1.save()
    return HttpResponseRedirect(reverse('index'))
def update(request,id):
    student=Members.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        "student":student
    }
    return HttpResponse(template.render(context,request))
def updaterecord(request,id):
    n=request.POST['student_name']
    r=request.POST['roll_no']
    b=request.POST['branch']
    student=Members.objects.get(id=id)
    student.student_name=n
    student.roll_no=r
    student.branch=b
    student.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    s1=Members.objects.get(id=id)
    s1.delete()
    return HttpResponseRedirect(reverse(index))
def dele(request):
    p1=list(request.POST.keys())
    print(request.POST.keys())
    print(p1)
    p1.pop(0)
    print(p1)
    for i in p1:
        s=Members.objects.get(id=int(i))
        s.delete()
    return HttpResponseRedirect(reverse('index'))