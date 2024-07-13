class MatchVisitor:
    def visit_team(self, team):
        raise NotImplementedError
    
    def visit_quality_distribution(self, quality_distribution):
        raise NotImplementedError

    def visit_knockout_match(self, match):
        raise NotImplementedError

class ToDictVisitor(MatchVisitor):
    def visit_team(self, team):
        return {
            'country_name': team.countryName,
            'squad' : team.squad,
            'offensive_quality_distribution' : team.offensive_quality_distribution.accept(self),
            'defensive_quality_distribution' : team.defensive_quality_distribution.accept(self),
            'points_earned' : team.points_earned,
            'goals_scored' : team.goals_scored,
            'goals_conceded' : team.goals_conceded,
            'group_placement' : team.group_placement,
            'games' : team.list_of_games,
            'exitRound': team.exit_round
        }
    
    def visit_quality_distribution(self, quality_distribution):
        return {
            'mean': quality_distribution.mean,
            'stdev': quality_distribution.stdev
        }

    def visit_knockout_match(self, match):
        return {
            'gameId': match.gameId,
            'nextGameId': match.next_game_id,
            'teamA': match.teamA.accept(self),
            'teamB': match.teamB.accept(self),
            'team_a_goals_scored': match.team_a_goals_scored,
            'team_b_goals_scored': match.team_b_goals_scored,
            'group_placement_a': match.groupPlacementA,
            'group_placement_b': match.groupPlacementB,
            'winner': match.winner.accept(self)
        }
    
