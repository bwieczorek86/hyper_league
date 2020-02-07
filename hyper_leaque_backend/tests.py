from django.test import TestCase

from hyper_leaque_backend.models import Team, Game


class TeamModelTest(TestCase):

    def test_team_model(self):
        team1 = Team(player_one='Bartek', player_two='Kuba')
        self.assertEqual('Bartek', team1.player_one)
        self.assertEqual('Kuba', team1.player_two)


class GamesModelTest(TestCase):

    def test_games_model(self):
        team1 = Team(player_one='Bartek', player_two='Kuba')
        team1.save()
        team2 = Team(player_one='Dawid', player_two='Rogal')
        team2.save()
        game1 = Game(home_team_id=team1.id,
                     away_team_id=team2.id,
                     game_date='2020-01-01',
                     home_team_score=3,
                     away_team_score=4,
                     winner=None)

        self.assertEqual(1, game1.home_team_id)
        self.assertEqual(2, game1.away_team_id)
        self.assertEqual('2020-01-01', game1.game_date)
        self.assertEqual(3, game1.home_team_score)
        self.assertEqual(4, game1.away_team_score)

