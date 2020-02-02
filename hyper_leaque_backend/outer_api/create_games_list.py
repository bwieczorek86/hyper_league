from hyper_leaque_backend.helpers.create_match_schedule import create_balanced_round_robin
from hyper_leaque_backend.models import Team, Games


def add_data_to_db():

    # Get all teams by ids to list
    teams = list(Team.objects.values_list('id', flat=True))
    # Crate schedule for teams
    games = create_balanced_round_robin(teams)
    # Insert schedule to database

    if Games.objects.all is not None:
        for x in games:
            if x[0][0] is not None or x[0][1] is not None:
                Games.objects.create(home_team_id=x[0][0], away_team_id=x[0][1], game_date='2020-01-01',
                                     home_team_score=0, away_team_score=0, winner="")
                Games.save()

    games_schedule = Games.objects.All()

    return games_schedule




