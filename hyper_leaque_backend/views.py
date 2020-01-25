from django.shortcuts import render

from hyper_leaque_backend.helpers.create_match_schedule import create_balanced_round_robin
from hyper_leaque_backend.models import Team


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def team_details(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team_details.html', {'team': team})


def games_list(request):
    teams = Team.objects.all()
    games = create_balanced_round_robin(teams)
    return render(request, 'games_list.html', {'games': games})



