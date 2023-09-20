import collections
from typing import List

MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))

def match_sequence(matches, team_a, team_b):
    def build_graph(matches: List[MatchResult]):

        graph = collections.defaultdict(set())
        for match in matches:
            #if match.winning_team in graph:
            graph[match.winning_team].add(match.losing_team)

        return graph

    # Using DFS
    def does_sequence_exist(graph, curr, dest, visited=set()):

        if curr == dest:
            return True
        if curr not in graph or curr in visited:
            return False
        visited.add(curr)
        for curr in graph[curr]:
            return any(does_sequence_exist(graph, curr, dest))




    return does_sequence_exist(build_graph(), team_a, team_b)
