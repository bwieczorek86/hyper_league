from django.db import models


def add_team_name(player1, player2):
    return f'{player1} / {player2}'


class Team(models.Model):
    player_one = models.CharField(max_length=255)
    player_two = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255, default=add_team_name(player_one, player_two))
    created_date = models.DateTimeField(auto_now_add=True)


class Games(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_team', null=False, on_delete=models.DO_NOTHING)
    away_team = models.ForeignKey(Team, related_name='away_team', null=False, on_delete=models.DO_NOTHING)
    game_date = models.DateTimeField()


