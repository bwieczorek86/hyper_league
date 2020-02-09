from django.test import TestCase

from hyper_leaque_backend.helpers.create_match_schedule import create_balanced_round_robin
from hyper_leaque_backend.helpers.delete_tuples_with_none import delete_tuples_from_list
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


class GamesScheduleCreatorTest(TestCase):

    def test_create_match_schedule(self):
        team_list = [1, 2, 3]
        reverse_team_list = team_list[::-1]
        test_match = self.create_list_of_matches(reverse_team_list, team_list)
        assert_test_list = [(1, 3), (1, 2), (2, 1), (2, 3), (3, 1), (3, 2)]

        self.assertEqual(set(assert_test_list), set(test_match))

    @staticmethod
    def create_list_of_matches(reverse_team_list, team_list):
        test_match1 = delete_tuples_from_list(create_balanced_round_robin(team_list))
        test_match2 = delete_tuples_from_list(create_balanced_round_robin(reverse_team_list))
        test_match = test_match1 + test_match2
        return test_match

