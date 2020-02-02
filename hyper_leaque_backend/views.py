from django.shortcuts import render

from hyper_leaque_backend.models import Team
from hyper_leaque_backend.outer_api.create_games_list import add_data_to_db


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def team_details(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team_details.html', {'team': team})


def games_list(request):
    games_schedule = add_data_to_db()
    return render(request, 'games_list.html', {'games': games_schedule})



