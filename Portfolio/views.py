from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Interest, Skill, DevOps

def home(request):
    skills = Skill.objects.all()
    interests = Interest.objects.all()
    devops = DevOps.objects.all()
    return render(request, "Portfolio/home.html", {'skills': skills,'interests':interests, 'devops':devops})
