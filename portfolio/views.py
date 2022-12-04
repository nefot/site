from django.shortcuts import render
from .models import Project


def user(request):
    project = Project.objects.all()
    return render(request, 'home/home.html', {'projects': project})
