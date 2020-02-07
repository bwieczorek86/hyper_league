from hyper_leaque_backend.helpers.create_match_schedule import create_balanced_round_robin
from hyper_leaque_backend.models import Team, Game


def generate_games_schedule():
    # Get all teams by ids to list
    teams = list(Team.objects.values_list('id', flat=True))
    revers_teams = teams[::-1]
    # Crate schedule for teams
    games1 = create_balanced_round_robin(teams)
    games2 = create_balanced_round_robin(revers_teams)

    # If database is empty add games
    if Game.objects.count() == 0:
        add_new_games(games1)
        add_new_games(games2)

    # Select all games from database
    games_schedule = Game.objects.all().values('home_team__team_name',
                                               'away_team__team_name',
                                               'home_team_score',
                                               'away_team_score')
    return games_schedule


def add_new_games(games):
    """ Loop thru created balance round robin list and games to database """
    for game in games:
        for game_ele in game:
            if isinstance(game_ele[0], int) and isinstance(game_ele[1], int) and game_ele[0] is not game_ele[1]:
                new_game = Game.objects.create(home_team_id=game_ele[0], away_team_id=game_ele[1],
                                               game_date='2020-01-01',
                                               home_team_score=0, away_team_score=0, winner="")
                Game.save(new_game)
