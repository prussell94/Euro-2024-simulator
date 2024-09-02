class Team():
    """
    A class representing a team

    Attributes:
        country_name (str): The name of country.
        squad (list): The squad of team.
        offensive_quality_distribution (quality_distribution): The probability distribution of offensive quality of team.
        defensive_quality_distribution (quality_distribution): The probability distribution of defensive quality of team.
        points_earned (int): Number of points earned so far.
        goals_scored (int): Number of goals scored so far.
        goals_conceded (int): Number of goals conceded so far.
        group_placement (int): Current placement in table.
        list_of_games (list): list of games played by team
        exit_round (string): round team exits in (group_stage, round_of_16, quarter_finals, semi_finals, final, winner)
    """
    def __init__(self, countryName, squad, offensive_quality_distribution, defensive_quality_distribution, points_earned=0, goals_scored=0, goals_conceded=0, group_placement=4, list_of_games=[], exit_round="", quality_metrics=None):
        """
        Initialize a new team instance.

        Args:
            country_name (str): The name of country.
            squad (list): The squad of team.
            offensive_quality_distribution (qualityDistribution): The probability distribution of offensive quality of team.
            defensive_quality_distribution (qualityDistribution): The probability distribution of defensive quality of team.
            points_earned (int): Number of points earned so far.
            goals_scored (int): Number of goals scored so far.
            goals_conceded (int): Number of goals conceded so far.
            group_placement (int): Current placement in table.
            list_of_games (list): list of games played by team
            exit_round (string): round team exits in (group_stage, round_of_16, quarter_finals, semi_finals, final, winner)
        """
        self._countryName = countryName
        self._squad = squad
        self._offensiveQualityDistribution = offensive_quality_distribution
        self._defensiveQualityDistribution = defensive_quality_distribution
        self._pointsEarned = points_earned
        self._goalsScored = goals_scored
        self._goalsConceded = goals_conceded
        self._groupPlacement = group_placement
        self._games = list_of_games
        self._exitRound = exit_round
        self.quality_metrics = quality_metrics if quality_metrics is not None else {}

    @property
    def countryName(self):
        return self._countryName

    @property
    def squad(self):
        return self._squad

    @property
    def offensive_quality_distribution(self):
        return self._offensiveQualityDistribution

    @property
    def defensive_quality_distribution(self):
        return self._defensiveQualityDistribution
    
    @property
    def points_earned(self):
        return self._pointsEarned
    
    @property
    def goals_scored(self):
        return self._goalsScored
    
    @property
    def goals_conceded(self):
        return self._goalsConceded
    
    @property
    def group_placement(self):
        return self._groupPlacement
    
    @property
    def list_of_games(self):
        return self._games
    
    @property
    def exit_round(self):
        return self._exitRound

    @countryName.setter
    def name(self, country_name):
        self._countryName = country_name

    @squad.setter
    def squad(self, squad):
        self._squad = squad

    @offensive_quality_distribution.setter
    def offensive_quality_distribution(self, offensive_quality_distribution):
        self._offensiveQualityDistribution = offensive_quality_distribution
    
    @defensive_quality_distribution.setter
    def defensive_quality_distribution(self, offensive_quality_distribution):
        self._offensiveQualityDistribution = offensive_quality_distribution

    @points_earned.setter
    def points_earned(self, points_earned):
        if points_earned < 0:
            raise ValueError("points earned cannot be negative")
        self._pointsEarned = self._pointsEarned+points_earned

    @goals_scored.setter
    def goals_scored(self, goals_scored):
        if goals_scored < 0:
            raise ValueError("Goals scored cannot be negative")
        self._goalsScored = self._goalsScored+goals_scored

    @goals_conceded.setter
    def goals_conceded(self, goals_conceded):
        if goals_conceded < 0:
            raise ValueError("Goals conceded cannot be negative")
        self._goalsConceded = self._goalsConceded+goals_conceded

    @group_placement.setter
    def group_placement(self, group_placement):
        if group_placement < 1 or group_placement > 4:
            raise ValueError("placment must be between 1 and 4")
        self._groupPlacement = group_placement

    @list_of_games.setter
    def list_of_games(self, games):
        self._games = games

    @exit_round.setter
    def exit_round(self, round):
        self._exitRound = round

    def get_countryName(self):
        return self._countryName
    def get_squad(self):
        return self._squad
    def get_offensiveQualityDistribution(self):
        return self._offensiveQualityDistribution
    def get_defensiveQualityDistribution(self):
        return self._defensiveQualityDistribution
    def get_pointsEarned(self):
        return self._pointsEarned
    def get_goalsScored(self):
        return self._goalsScored
    def get_goalsConceded(self):
        return self._goalsConceded
    def get_groupPlacement(self):
        return self._groupPlacement

    def set_goalsScored(self, goals):
        if goals < 0:
            goals = 0
        self._goalsScored = self._goalsScored+goals
    
    def set_goalsConceded(self, goals):
        if goals < 0:
            goals = 0
        self._goalsConceded = self._goalsConceded+goals

    def set_pointsEarned(self, points):
        if points < 0:
            points = 0
        self._pointsEarned = self._pointsEarned+points
        
    def set_groupPlacement(self, placement):
        if placement < 1 or placement > 4:
            raise ValueError("placment must be between 1 and 4")
        self._groupPlacement = placement

    def set_list_of_games(self, games):
        self._list_of_games = games

    def add_to_list_of_games(self, game):
        self._list_of_games.append(game)

    def set_exit_round(self, round):
        self._exitRound = round

    def accept(self, visitor):
        return visitor.visit_team(self)
    
    def set_quality_metrics(self, metrics_dict):
        self.quality_metrics.update(metrics_dict)

    def get_quality_metric(self, metric_name):
        return self.quality_metrics.get(metric_name, None)