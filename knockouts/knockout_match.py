from matches.match import Match
from teams import team, team_data
class knockout_match(Match):
    """
    A class representing a soccer match in knockout rounds

    Attributes:
        gameId (int): id of game.
        nextGameId (int): id of game that winner will advance to.
        teamA (Team): The first team in the match.
        teamB (Team): The second team in the match.
        team_a_goals_scored (int): The number of goals scored by first team.
        team_b_goals_scored (int): The number of goals scored by second team.
        group_placement_a (str): String that contains the group team played in followed by the placement within that group
        group_placement_b (str): String that contains the group team played in followed by the placement within that group
    """
    def __init__(self, game_id='', next_game_id='', teamA=team_data.dummy_team, teamB=team_data.dummy_team, team_a_goals_scored=0, team_b_goals_scored=0, groupPlacementA='', groupPlacementB='', winner=None):
        # Lazy import to avoid circular dependency
        if teamA is None:
            from teams.team_data import germany as teamA
        if teamB is None:
            from teams.team_data import switzerland as teamB
        if winner is None:
            from teams.team_data import germany as winner
        
        super().__init__(teamA=teamA, teamB=teamB, team_a_goals_scored=team_a_goals_scored, team_b_goals_scored=team_b_goals_scored)
        self._gameId = game_id
        self._nextGameId = next_game_id
        self._teamA = teamA
        self._teamB = teamB
        self._groupPlacementA = groupPlacementA
        self._groupPlacementB = groupPlacementB
        self._winner = winner

    @property
    def groupPlacementA(self):
        return self._groupPlacementA

    @groupPlacementA.setter
    def groupPlacementA(self, placement):
        self._groupPlacementA = placement

    @property
    def groupPlacementB(self):
        return self._groupPlacementB

    @groupPlacementB.setter
    def groupPlacementB(self, placement):
        self._groupPlacementB = placement

    def get_gameId(self):
        return self._gameId
    def get_teamA(self):
        return self._teamA
    def get_teamB(self):
        return self._teamB
    def get_nextGameId(self):
        return self._nextGameId
    def get_groupPlacementA(self):
        return self._groupPlacementA
    def get_groupPlacementB(self):
        return self._groupPlacementB
    def get_winner(self):
        return self._winner

    def set_gameId(self, gameId):
        self._gameId = gameId
    def set_nextGameId(self, nextGameId):
        self._nextGameId = nextGameId
    def set_teamA(self, teamA):
        self._teamA = teamA
    def set_teamB(self, teamB):
        self._teamB = teamB
    def set_groupPlacementA(self, groupPlacementA):
        self._groupPlacementA = groupPlacementA
    def set_groupPlacementB(self, groupPlacementB):
        self._groupPlacementB = groupPlacementB
    def set_winner(self, winner):
        self._winner = winner

    def to_dict(self):
        return {
            'gameId': self._game_id,
            'nextGameId': self._nextGameId,
            'teamA': self._teamA,
            'teamB': self._teamB,
            'team_a_goals_scored': self.team_a_goals_scored,
            'team_b_goals_scored': self.team_b_goals_scored,
            'groupPlacementA': self._groupPlacementA,
            'groupPlacementB': self._groupPlacementB,
            'winner': self._winner
        }
    
    def accept(self, visitor):
        print("accept method country a")
        print(self.get_teamA().get_countryName())
        print("accept method -----")
        print(self.get_teamB().get_countryName())
        return visitor.visit_knockout_match(self)
    
    def __repr__(self):
        return (f"knockout_match(gameId={self._gameId}, nextGameId={self._nextGameId}, "
                f"teamA={self.teamA}, teamB={self.teamB}, team_a_goals_scored={self.team_a_goals_scored}, "
                f"team_b_goals_scored={self.team_b_goals_scored}, groupPlacementA={self._groupPlacementA}, "
                f"groupPlacementB={self._groupPlacementB}, winner={self._winner})")

    def __str__(self):
        return (f"knockout_match: Game ID {self._gameId}, Next Game ID {self._nextGameId}, "
                f"Teams: {self.teamA} vs {self.teamB}, Score: {self.team_a_goals_scored}-{self.team_b_goals_scored}, "
                f"Group Placements: {self._groupPlacementA} vs {self._groupPlacementB}, Winner: {self._winner}")