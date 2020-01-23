from django.http import HttpResponse
from django.shortcuts import render

from hyper_leaque_backend.models import Team


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def details(request):
    team = Team.objects.name('Backendy').get('name')
    return HttpResponse("Test")



