from django.http import HttpResponse
from django.shortcuts import render

from hyper_leaque_backend.models import Team


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def team_details(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team_details.html', {'team': team})



