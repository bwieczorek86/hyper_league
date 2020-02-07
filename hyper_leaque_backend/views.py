from django.shortcuts import render

from hyper_leaque_backend.models import Team
from hyper_leaque_backend.create_schedule_service.create_games_list import generate_games_schedule


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def team_details(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team_details.html', {'team': team})


def games_list(request):
    games_schedule = generate_games_schedule()
    return render(request, 'games_list.html', {'games_schedule': games_schedule})


def generate_score_table():
    dupa = [1, 2, 3]
    return dupa


def score_table(request):
    scores = generate_score_table()
    return render(request, 'score_table.html', {'scores': scores})




