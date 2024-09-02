from teams.team import Team
from matches.match import Match
import itertools
import matches.simulator

import pandas as pd

class Group():
    euro_squads = pd.read_csv("matches/modified_euro_2024_squads_2.csv")
    match_simulator = matches.simulator.Simulator(euro_squads)
    """
    A class representing a group

    Attributes:
        teams (list): List of teams in group
        standings (DataFrame): The standings of the group - includes information on points, goals scored, conceded.
    """
    def __init__(self, teams, standings=pd.DataFrame()):
        """
        Initialize a new group instance.

        Args:
            teams (list): List of teams in group
            standings (DataFrame): The standings of the group - includes information on points, goals scored, conceded.
        """
        self._teams = teams
        self._standings = standings

    @property
    def teams(self):
        return self._teams

    @property
    def standings(self):
        return self._standings

    @teams.setter
    def teams(self, teams):
        self._teams = teams

    @standings.setter
    def standings(self, standings):
        self._standings = standings

    def simulate_matches(team_a, team_b, sample):
        """
        Simulate matches.

        Args:
            team_a (Team): first team.
            team_b (Team): second team.
            sample (int): number of simulations of game

        Returns:
            matches (list): list of match
        """
        matches = []
        # euro_2024_squads = pd.read_csv("matches/modified_euro_2024_squads_2.csv")
        # match_simulator = matches.simulator.Simulator(euro_squads)

        for i in range(0, sample):
            # simulator_match = match_simulator(euro_2024_squads)
            # team_a_goals_scored, team_b_goals_scored = self.match_simulator.simulate_match(team_a.get_countryName(), team_b.get_countryName())
            matches.append(Match.simulateMatchWithModel(team_a, team_b))
        return matches

    def get_matchups(self, teams):
        """
        Retrieve matchups between given teams

        Args:
            teams (list): list of teams to include in permutations

        Returns:
            matchups (list): permutation of matches
        """
        matchups = list(itertools.combinations(teams, 2))
        return matchups
    
    def points_awarded(self, home_team_goals, away_team_goals):
        """
            Calculates points awarded based off number of goals scored for each team

            Args:
                home_team_goals (int): The number of goals scored by home team
                away_team_goals (int): The number of goals scored by away team

            Returns:
                home_team_points (int): The number of points awarded to home team
                away_team_points(int): The number of points awarded to away team
    
            Raises:
                ValueError: If home_team_goals or away_team_goals are negative.
        """
        if home_team_goals < 0:
            raise ValueError("goals for home team is not defined for negative numbers.")
        elif away_team_goals < 0:
            raise ValueError("goals for away team is not defined for negative numbers.")
        home_team_goals = round(home_team_goals, 0)
        away_team_goals = round(away_team_goals, 0)
        if(home_team_goals > away_team_goals):
            home_team_points = 3
            away_team_points = 0
        elif(home_team_goals == away_team_goals):
            home_team_points = 1
            away_team_points = 1
        else:
            home_team_points = 0
            away_team_points = 3
        return home_team_points, away_team_points
    

    def simulate_group(self):
        """
        Simulate all group games

        Args:
            group (Group) : group to be simulated

        Returns:
            group_table (DataFrame): information on placement, points earned, goals earned etc.
        """
        reset_group = []
        for reset_team in self.teams:
            reset_team = Team(reset_team.get_countryName(), [], reset_team.get_offensiveQualityDistribution(), reset_team.get_defensiveQualityDistribution(),
                         goals_conceded=0, goals_scored=0, points_earned=0)
            reset_group.append(reset_team)
        
        matches = []
        for mu in self.get_matchups(reset_group):
            teamA = mu[0]
            teamB = mu[1]
            matchResult = Match.simulateMatchWithModel(self, teamA, teamB)
            matches.append(matchResult) 
        
        data = [{
            'Country': team.get_countryName(),
            'Points': team.get_pointsEarned(),
            'Goals Scored': team.get_goalsScored(),
            'Goals Conceded': team.get_goalsConceded()
        } for team in reset_group]

        group_table = pd.DataFrame(data)
        group_table = group_table.sort_values('Points', ascending=False)

        group_table = group_table.reset_index()
        group_table['Placement'] = group_table.index+1

        group_table = group_table[['Placement', 'Country', 'Points', 'Goals Scored', 'Goals Conceded']]

        print(group_table)
    
        return group_table