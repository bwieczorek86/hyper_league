from django.db import models


def add_team_name(player1, player2):
    return f'{player1} / {player2}'


class Team(models.Model):
    player_one = models.CharField(max_length=255)
    player_two = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)


class Games(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_team', null=False, on_delete=models.DO_NOTHING)
    away_team = models.ForeignKey(Team, related_name='away_team', null=False, on_delete=models.DO_NOTHING)
    game_date = models.DateTimeField()
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)
    winner = models.CharField(max_length=255, default=None, blank=True, null=True)

