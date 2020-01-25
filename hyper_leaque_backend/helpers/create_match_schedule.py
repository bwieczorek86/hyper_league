from hyper_leaque_backend.models import Team


def create_balanced_round_robin(players):
    """ Create a schedule for the teams in the list and return it"""
    s = []
    if len(players) % 2 == 1: players = players + [None]
    # manipulate map (array of indexes for list) instead of list itself
    # this takes advantage of even/odd indexes to determine home vs. away
    n = len(players)
    map_teams = list(range(n))
    mid = n // 2
    for i in range(n - 1):
        l1 = map_teams[:mid]
        l2 = map_teams[mid:]
        l2.reverse()
        round_teams = []
        for j in range(mid):
            t1 = players[l1[j]]
            t2 = players[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                round_teams.append((t2, t1))
            else:
                round_teams.append((t1, t2))
        s.append(round_teams)
        # rotate list by n/2, leaving last element at the end
        map_teams = map_teams[mid:-1] + map_teams[:mid] + map_teams[-1:]
    return s


# teams_to_round = Team.object.all()
# # schedule = create_balanced_round_robin(teams_to_round)
# # output = ("\n".join(['{} vs. {}'.format(m[0]['team_name'], m[1]) for round_team in schedule for m in teams_to_round]))
# # return output