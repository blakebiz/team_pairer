import random
from typing import List, Union


class Teammate:
    def __init__(self, name, requests: List[Union[str, int]]):
        self.name, self.requests = name, requests

    def __repr__(self):
        return f'name: {self.name}, requests: {self.requests}'


class Team:
    def __init__(self, team_id: int, name: str, max_size: int = 6):
        self.team_id, self.names, self.max_size = team_id, [name], max_size

    def __repr__(self):
        return f'team_id: {self.team_id}, names: {self.names}'


def assign_teammates(teammates: List[Teammate]):
    assigned, team_count, teams = dict(), 0, []
    names = set(t.name for t in teammates)
    random.shuffle(teammates)
    team_full, team_object = True, None
    for teammate in teammates:
        if teammate.name not in assigned:
            if team_full:
                team_object = Team(team_count, teammate.name)
                assigned[teammate.name] = team_count
                team_count += 1
            else:
                assigned[teammate.name] = team_count
                team_object.names.append(teammate.name)

            for request in teammate.requests:
                if len(team_object.names) >= team_object.max_size:
                    break
                elif request not in assigned and request in names:
                    team_object.names.append(request)
                    assigned[request] = team_count
            team_full = len(team_object.names) >= team_object.max_size
            if team_full:
                teams.append(team_object)
    if not team_full:
        teams.append(team_object)
    return teams


def test():
    test1 = Teammate(1111, [1112, 1115])
    test2 = Teammate(1112, [])
    test3 = Teammate(1113, [1111, 1112])
    test4 = Teammate(1114, [])
    test5 = Teammate(1115, [1114])
    test6 = Teammate(1116, [1112])
    test7 = Teammate(1117, [])
    test8 = Teammate(1118, [])
    test9 = Teammate(1119, [1113])
    teams = assign_teammates([test1, test2, test3, test4, test5, test6, test7, test8, test9])
    print([team.names for team in teams])

test()
