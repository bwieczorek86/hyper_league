from django.db import models


class Team(models.Model):
    player_one = models.CharField(max_length=255)
    player_two = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Team: {}'.format(self.team_name)


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_team', null=False, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_team', null=False, on_delete=models.CASCADE)
    game_date = models.DateTimeField()
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)
    winner = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return 'Game: {}-{}'.format(self.home_team.team_name, self.away_team.team_name)