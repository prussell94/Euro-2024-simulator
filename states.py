# states.py
import groups
import groups.groups_data
import random
import matches.match
from knockouts.knockout_match_data import third_place_permutations
from knockouts.knockout_match_data import r16_matches
from knockouts.knockout_match_data import knockout_bracket, knockout_match
import matches.simulator
import teams
import copy

import pandas as pd

original_knockout = copy.deepcopy(knockout_bracket)

class TournamentState:

    euro_squads = pd.read_csv("matches/modified_euro_2024_squads_2.csv")
    match_simulator = matches.simulator.Simulator(euro_squads)

    def simulate_round(self, tournament):
        raise NotImplementedError
    
    def simulate_match_impl(self, team_a, team_b):
        """
        In the case of round robin - need to allocate points 
        In the case of knockout - need to determine overtime, penalties
        """
        raise NotImplementedError
    
    def set_context(self, tournament):
        """Link the state to the tournament context."""
        self.tournament = tournament
    
    def simulate_match(self, team_a, team_b, original_match):

        team_a_goals_scored, team_b_goals_scored = self.match_simulator.simulate_match(team_a.get_countryName(), team_b.get_countryName())

        team_a_goals_scored = round(team_a_goals_scored, 0)
        team_b_goals_scored = round(team_b_goals_scored, 0)

        current_match = copy.deepcopy(original_match)

        current_match.team_a_goals_scored = 0
        current_match.team_b_goals_scored = 0

        current_match.set_teamA(team_a)
        current_match.set_teamB(team_b)
        current_match.set_teamAGoalsScored(team_a_goals_scored)
        current_match.set_teamBGoalsScored(team_b_goals_scored)

        match_complete = self.simulate_match_impl(team_a, team_b, current_match)

        return match_complete

class GroupStageState(TournamentState):
    """
    A class representing the group stage state

    Attributes:
        groups (dict) : dictionary of groups 
    """
    def __init__(self, tournament="", groups={"A":groups.groups_data.group_a, "B":groups.groups_data.group_b, "C":groups.groups_data.group_c, 
                               "D":groups.groups_data.group_d, "E":groups.groups_data.group_e, "F":groups.groups_data.group_f}):

        """
        Initialize a new group stage instance.

        Args:
            groups (dict): dictionary of groups
        """
        self._groups=groups
        self._knockout_bracket=copy.deepcopy(original_knockout)

    def assign_group_placement(self, row):
        return row['Group']+str(row['Placement'])
    
    def simulate_round(self, tournament=""):
        """
        Simulates entire group stage

        Returns:
            list of results for each group
        """
        results = []
        for group_key, group_value in self._groups.items():
            result = group_value.simulate_group()
            result["Group"] = group_key
            result['GroupPlacement'] =result.apply(lambda row: self.assign_group_placement(row), axis=1)
            results.append(result)

        initial_r16_matches = self.generate_initial_knockout_round(results)

        knockout_round_bracket = self.mapGroupPlacementToTeam(initial_r16_matches, results, groups.groups_data.groups_dict)

        tournament.set_knockout_bracket(knockout_round_bracket)

        qualified_teams = []
        for match in knockout_round_bracket['round_of_16'].values():
            qualified_teams.append(match.teamA)
            qualified_teams.append(match.teamB)
        
        qualified_team_names = [team.countryName for team in qualified_teams]

        all_teams = list(teams.team_data.teams_dict.values())

        non_qualified_teams = [team for team in teams.team_data.teams_dict.values() if team.countryName not in qualified_team_names]

        [setattr(team, 'exit_round', 'group_stage') for team in teams.team_data.teams_dict.values() if team.countryName not in qualified_team_names]

        print("Simulating Group Stage...")

        tournament.transition_to(RoundOf16State())
        
        return results
    
    def update_bracket(self, tournament, current_round_title, next_round_title):

        current_bracket = tournament.get_knockout_bracket()
        if isinstance(current_round_title, list):
            next_round = current_bracket[next_round_title]
            for index, match_id in enumerate(next_round.keys()):
                knockout_game = next_round[match_id]
                next_round_knockout_match = next_round[current_round_title[index].get_gameId()]
                next_round_knockout_match.set_teamA()
                next_round_knockout_match.set_teamB()

        current_round = current_bracket[current_round_title]
        next_round = current_bracket[next_round_title]

        if current_round_title == 'final':

            original_match = current_round["51"]

            current_match = self.simulate_match(first_team, second_team, original_match)

            current_round[match_id] = current_match

            print("Tournament is complete")

        else:

            for match_id in current_round.keys():
                first_team = current_round[match_id].get_teamA()
                second_team = current_round[match_id].get_teamB()

                current_match = self.simulate_match(first_team, second_team)
                current_round[match_id] = current_match
                next_round_match_id = current_round[match_id].get_nextGameId()
                next_round_knockout_match = next_round[next_round_match_id]

                all_teams = tournament.get_teams()

                if first_team != current_round[match_id].get_winner():
                    first_team.set_exit_round(current_round_title)
                    all_teams[first_team.get_countryName()] = first_team
                    
                elif second_team != current_round[match_id].get_winner():
                    second_team.set_exit_round(current_round_title)
                    all_teams[second_team.get_countryName()] = second_team

                if next_round_knockout_match.get_teamA() != None :
                    next_round_knockout_match.set_teamA(current_round[match_id].get_winner())
                else:
                    next_round_knockout_match.set_teamB(current_round[match_id].get_winner())

                tournament.set_teams(all_teams)
                next_round[next_round_match_id] = next_round_knockout_match
    
    def simulate_match_impl(self, team_a, team_b, original_match):
        
        points_distribution = matches.match.Match.points_awarded(team_a.get_goalsScored(), team_b.get_goalsScored())

        team_a.set_pointsEarned(points_distribution[0])
        team_b.set_pointsEarned(points_distribution[1])
        
        if team_a.get_goalsScored() > team_b.get_goalsScored():
            game_winner = team_a.get_countryName()
        elif team_a.get_goalsScored() < team_b.get_goalsScored():
            game_winner = team_b.get_countryName()

        original_match.team_a = team_a
        original_match.team_b = team_b
        original_match.team_a_goals_scored = team_a.goals_scored
        original_match.team_b_goals_scored = team_b.goals_scored
        original_match.winner = game_winner

        return original_match
            
    def calculate_third_place_qualifiers(self, group_stage_tables):
        """
        Calculates the table that ranks all third placed teams

        Args:
            group_stage_tables (list): list of group tables

        Returns:
            third_place_table (DataFrame): Ranking of third place finishers
        """
        third_place_a=group_stage_tables[0][group_stage_tables[0]['Placement']==3]
        third_place_a['group']="A"
        third_place_b=group_stage_tables[1][group_stage_tables[1]['Placement']==3]
        third_place_b['group']="B"
        third_place_c=group_stage_tables[2][group_stage_tables[2]['Placement']==3]
        third_place_c['group']="C"
        third_place_d=group_stage_tables[3][group_stage_tables[3]['Placement']==3]
        third_place_d['group']="D"
        third_place_e=group_stage_tables[4][group_stage_tables[4]['Placement']==3]
        third_place_e['group']="E"
        third_place_f=group_stage_tables[5][group_stage_tables[5]['Placement']==3]
        third_place_f['group']="F"

        third_place_table=pd.concat([third_place_a, third_place_b, third_place_c, third_place_d, third_place_e, third_place_f])
        third_place_table['Goal Differential']=third_place_table['Goals Scored']-third_place_table['Goals Conceded']

        third_place_table.sort_values(by=['Points', 'Goal Differential', 'Goals Scored'], 
                           ascending=[False, False, False], inplace=True)
        return third_place_table
    
    def extract_qualifying_third_placers(self, table):
        table = pd.DataFrame(table['group'].iloc[:4])
        permutation = (table['group'].iloc[0],table['group'].iloc[1],table['group'].iloc[2],table['group'].iloc[3])
        permutation_list = list(permutation)
        permutation_list.sort()
        permutation=tuple(permutation_list)
        return permutation
    
    def generate_initial_knockout_round(self, group_stage):
        third_place_rankings=self.calculate_third_place_qualifiers(group_stage)
        qualifying_third_place=self.extract_qualifying_third_placers(third_place_rankings)
    
        third_place_mappings = third_place_permutations[qualifying_third_place]

        for i in range(0, 8):
            for k in third_place_mappings.keys():
                if r16_matches[i].get_gameId() == third_place_mappings[k]:
                    r16_matches[i].set_groupPlacementB(k+"3")
        
        new_knockout=copy.deepcopy(original_knockout)
        for matchIndex in self._knockout_bracket['round_of_16'].keys():
            
            for k in third_place_mappings.keys():                    
                if str(matchIndex) == str(third_place_mappings[k]):
                    self._knockout_bracket['round_of_16'][matchIndex].set_groupPlacementB(k+"3")

        return r16_matches
    
    def mapGroupPlacementToTeam(self, r16_matches, group_stage, groups_dict):

        group_tables=pd.concat(group_stage, ignore_index=True)

        for matchIndex in self._knockout_bracket['round_of_16'].keys():
            
            match = self._knockout_bracket['round_of_16'][matchIndex]
            
            groupPlacementA = match.get_groupPlacementA()
            groupPlacementB = match.get_groupPlacementB()

            country_name_a = group_tables[group_tables['GroupPlacement'] == groupPlacementA]['Country'].iloc[0]
            group_of_country_a = group_tables[group_tables['GroupPlacement'] == groupPlacementA]['Group'].iloc[0]
            teams_a_of_group = groups_dict[str(group_of_country_a)]
            team_a_in_group = [team for team in teams_a_of_group if team.get_countryName() == country_name_a][0]

            country_name_b = group_tables[group_tables['GroupPlacement'] == groupPlacementB]['Country'].iloc[0]

            group_of_country_b = group_tables[group_tables['GroupPlacement'] == groupPlacementB]['Group'].iloc[0]
            teams_b_of_group = groups_dict[str(group_of_country_b)]
            team_b_in_group = [team for team in teams_b_of_group if team.get_countryName() == country_name_b][0]
            
            match.set_teamA(team_a_in_group)
            match.set_teamB(team_b_in_group)

            self._knockout_bracket['round_of_16'][matchIndex] = match

        return self._knockout_bracket
    
class KnockoutState(TournamentState):
    def simulate_round(self, tournament):
        # Simulate quarter-finals matches
        
        print("Simulating Knockout...")
        # Example logic: Determine winners and transition to next state

        self.update_bracket(tournament, "round_of_16", "quarter_finals")

        tournament.transition_to(KnockoutState())
    
    def update_bracket(self, tournament, current_round_title, next_round_title):
        current_bracket = tournament.get_knockout_bracket()

        if current_round_title == 'group_stage':
            next_round = current_bracket[next_round_title]

        current_round = current_bracket[current_round_title]
        next_round = current_bracket[next_round_title]

        if current_round_title == 'final':
            print("testing final")
            print(current_round["51"].get_teamA().get_countryName())
            print(current_round["51"].get_teamAGoalsScored())
            print(current_round["51"].get_teamB().get_countryName())
            print(current_round["51"].get_teamBGoalsScored())

            original_match = current_round["51"]

            current_match = self.simulate_match(current_round["51"].get_teamA(), current_round["51"].get_teamB(), original_match)

            current_round["51"] = current_match
            print(current_match)
            first_team = current_round["51"].get_teamA()
            second_team = current_round["51"].get_teamB()

            all_teams = tournament.get_teams()
            
            if(current_round["51"].get_teamAGoalsScored() > current_round["51"].get_teamBGoalsScored()):
                # print(current_round["51"].get_teamA())
                # print("wins")
                first_team.set_exit_round("winner")
                second_team.set_exit_round('runner_up')
                current_round["51"].set_winner(current_round["51"].get_teamA())
    
            elif current_round["51"].get_teamAGoalsScored() < current_round["51"].get_teamBGoalsScored():
                # print(current_round["51"].get_teamB())
                # print("wins")
                second_team.set_exit_round("winner")
                first_team.set_exit_round('runner_up')
                current_round["51"].set_winner(current_round["51"].get_teamB())
            # else:
            #     print("checking blank score " + str(current_round["51"].get_teamBGoalsScored()))
            #     print(current_round["51"].get_teamAGoalsScored())
                # raise ValueError("No winner determined from number of goals scored.")

            all_teams[first_team.get_countryName()] = first_team
            all_teams[second_team.get_countryName()] = second_team

            tournament.set_teams(all_teams)

            print("Tournament is complete")

        else:
            # for match_id in current_round.keys():
            #     first_team = current_round[match_id].get_teamA()
            #     second_team = current_round[match_id].get_teamB()

            #     # current_match = self.simulate_match(first_team, second_team)
            #     # current_round[match_id] = current_match
            #     # next_round_match_id = current_round[match_id].get_nextGameId()
            #     # next_round_knockout_match = next_round[next_round_match_id]

            #     all_teams = tournament.get_teams()
            #     if first_team != current_round[match_id].get_winner():
            #         first_team.set_exit_round(current_round_title)
            #         all_teams[first_team.get_countryName()] = first_team
                    
            #     elif second_team != current_round[match_id].get_winner():
            #         second_team.set_exit_round(current_round_title)
            #         all_teams[second_team.get_countryName()] = second_team

            #     if next_round_knockout_match.get_teamA() != None :
            #         # // i need to set get_winner() to team object not a string!
            #         print("the winner is " + current_round[match_id].get_winner())
            #         next_round_knockout_match.set_teamA(current_round[match_id].get_winner())
            #     else:
            #         next_round_knockout_match.set_teamB(current_round[match_id].get_winner())

            #     print("setting new teams")
            #     tournament.set_teams(all_teams)
            #     next_round[next_round_match_id] = next_round_knockout_match

            for match_id in current_round.keys():
                first_team = current_round[match_id].get_teamA()
                second_team = current_round[match_id].get_teamB()

                next_round_match_id = current_round[match_id].get_nextGameId()

                original_match = current_round[match_id]

                current_match = self.simulate_match(first_team, second_team, original_match)

                #this is where the error occurs
                current_round[match_id] = current_match

                next_round_knockout_match = next_round[next_round_match_id]

                all_teams = tournament.get_teams()

                if first_team != current_round[match_id].get_winner():
                    first_team.set_exit_round(current_round_title)
                    all_teams[first_team.get_countryName()] = first_team
                    
                elif second_team != current_round[match_id].get_winner():
                    second_team.set_exit_round(current_round_title)
                    all_teams[second_team.get_countryName()] = second_team

                if next_round_knockout_match.get_teamA() != "" :
                    if(next_round_knockout_match.get_teamA().get_countryName() != ""):
                        next_round_knockout_match.set_teamB(current_round[match_id].get_winner())
                    else:
                        next_round_knockout_match.set_teamA(current_round[match_id].get_winner())
                # else:
                #     print("what is team a?")
                #     print(next_round_knockout_match.get_teamA().get_countryName())
                #     next_round_knockout_match.set_teamB(current_round[match_id].get_winner())

                print("setting new teams")
                tournament.set_teams(all_teams)
                next_round[next_round_match_id] = next_round_knockout_match

    def simulate_match_impl(self, team_a, team_b, match, current_game_id='', next_current_game_id=''):

        # print("simulating match with team A")
        # print(team_a.get_countryName())
        # print("simulating match with team b")
        # print(team_b.get_countryName())
        team_a_goals_scored_90 = match.get_teamAGoalsScored()
        team_b_goals_scored_90 = match.get_teamBGoalsScored()

        team_a_goals_scored = team_a_goals_scored_90
        team_b_goals_scored = team_b_goals_scored_90

        # print("team a goals scored 90 ------ ")
        # print(team_a_goals_scored_90)

        # print("team b goals scored 90 ------ ")
        # print(team_b_goals_scored_90)

        if(team_a_goals_scored_90 == team_b_goals_scored_90):
            team_a_goals_scored_OT = (team_a.get_offensiveQualityDistribution().get_goal_estimate()[0])/3
            team_a_goals_conceded_OT = (team_a.get_defensiveQualityDistribution().get_goal_estimate()[0])/3
            team_b_goals_scored_OT = (team_b.get_offensiveQualityDistribution().get_goal_estimate()[0])/3
            team_b_goals_conceded_OT = (team_b.get_defensiveQualityDistribution().get_goal_estimate()[0])/3

            team_a_goals_scored_avg_OT = (team_a_goals_scored_OT+team_b_goals_conceded_OT)/2
            team_b_goals_scored_avg_OT = (team_b_goals_scored_OT+team_a_goals_conceded_OT)/2
            team_a_goals_scored_OT = round(team_a_goals_scored_avg_OT, 0)
            team_b_goals_scored_OT = round(team_b_goals_scored_avg_OT, 0) 

            team_a_goals_scored_120 = team_a_goals_scored_90 + team_a_goals_scored_OT
            team_b_goals_scored_120 = team_b_goals_scored_90 + team_b_goals_scored_OT

            if(team_a_goals_scored_120 != team_b_goals_scored_120):
                team_a_goals_scored = team_a_goals_scored_120
                team_b_goals_scored = team_b_goals_scored_120

            elif(team_a_goals_scored_120 == team_b_goals_scored_120):
                kicker = 1
                choices = [0, 1]       # 0 for "no", 1 for "yes"
                weights = [0.2, 0.8]   # 20% for "no", 80% for "yes"
                team_a_PK_score = 0
                team_b_PK_score = 0
            
                for r in range(1, 6):
                    team_a_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]
                    team_b_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]

                    team_a_PK_score = team_a_PK_score + team_a_shooter_outcome
                    team_b_PK_score = team_b_PK_score + team_b_shooter_outcome
            
                if(team_a_PK_score > team_b_PK_score):
                    team_a_goals_scored_after_pk = team_a_goals_scored_120 + 1
                    team_b_goals_scored_after_pk = team_b_goals_scored_120
                    # print(team_a.get_countryName() + "wins in pk! Score is " + team_a.get_countryName() + " " + str(team_a_PK_score) + " " + team_b.get_countryName() + " " + str(team_b_PK_score))
                    # print("recorded score is " + team_a.get_countryName() + " " + str(team_a_goals_scored_after_pk) + " " + team_b.get_countryName() + " " + str(team_b_goals_scored_after_pk))

                    team_a_goals_scored = team_a_goals_scored_after_pk
                    team_b_goals_scored = team_b_goals_scored_after_pk

                elif team_a_PK_score < team_b_PK_score:
                    team_b_goals_scored_after_pk = team_b_goals_scored + 1
                    team_a_goals_scored_after_pk = team_a_goals_scored

                    # print(team_b.get_countryName() + "wins in pk! Score is " + team_a.get_countryName() + " " + str(team_a_PK_score) + " " + team_b.get_countryName() + " " + str(team_b_PK_score))
                    # print("recorded score is " + team_a.get_countryName() + " " + str(team_a_goals_scored_after_pk) + " " + team_b.get_countryName() + " " + str(team_b_goals_scored_after_pk))

                    team_a_goals_scored = team_a_goals_scored_after_pk
                    team_b_goals_scored = team_b_goals_scored_after_pk
                else:
                    no_winner = True
                    
                    while(no_winner):
                        team_a_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]
                        team_b_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]

                        if team_a_shooter_outcome > team_b_shooter_outcome:
                            team_a_goals_scored_after_pk = team_a_goals_scored + 1
                            team_b_goals_scored_after_pk = team_b_goals_scored
                            # print(team_a.get_countryName() + "wins in pk overtime!")
                            no_winner = False
                            team_a_goals_scored = team_a_goals_scored_after_pk
                            team_b_goals_scored = team_b_goals_scored_after_pk
                    
                        elif team_a_shooter_outcome < team_b_shooter_outcome:
                            team_b_goals_scored_after_pk = team_b_goals_scored + 1
                            team_a_goals_scored_after_pk = team_a_goals_scored

                            # print(team_b.get_countryName() + "wins in pk overtime!")
                            no_winner = False
                            team_a_goals_scored = team_a_goals_scored_after_pk
                            team_b_goals_scored = team_b_goals_scored_after_pk
                                 
        team_a.set_goalsScored(team_a_goals_scored)
        team_a.set_goalsConceded(team_b_goals_scored)

        team_b.set_goalsScored(team_b_goals_scored)
        team_b.set_goalsConceded(team_a_goals_scored)

        print(team_a.get_countryName() + " " + str(team_a_goals_scored) + " " + team_b.get_countryName() + " " + str(team_b_goals_scored))

        if team_a_goals_scored > team_b_goals_scored:
            game_winner = team_a
        elif team_a_goals_scored < team_b_goals_scored:
            game_winner = team_b

        # print(team_a_goals_scored)
        # print(team_b_goals_scored)

        # print("setting match stuff")
        # print(team_b)
        # km = knockout_match(game_id= current_game_id, next_game_id = next_current_game_id, teamA=team_a, teamB=team_b, team_a_goals_scored=team_a_goals_scored, team_b_goals_scored=team_b_goals_scored, winner=game_winner)
        # print(km)
        match.team_a_goals_scored = team_a_goals_scored
        match.team_b_goals_scored = team_b_goals_scored
        match.winner = game_winner
        return match

class RoundOf16State(KnockoutState):
    def simulate_round(self, tournament):
        # Simulate quarter-finals matches
        print("Simulating Round of 16...")

        self.update_bracket(tournament, "round_of_16", "quarter_finals")

        # Example logic: Determine winners and transition to next state
        tournament.transition_to(QuarterFinalsState())

class QuarterFinalsState(KnockoutState):
    def simulate_round(self, tournament):
        # Simulate quarter-finals matches
        print("Simulating Quarter Finals...")

        self.update_bracket(tournament, "quarter_finals", "semi_finals")

        # Example logic: Determine winners and transition to next state
        tournament.transition_to(SemiFinalsState())

class SemiFinalsState(KnockoutState):
    def simulate_round(self, tournament):
        # Simulate semi-finals 
        print("Simulating Semi Finals...")

        self.update_bracket(tournament, "semi_finals", "final")

        # Example logic: Determine winners and transition to next state
        tournament.transition_to(FinalsState())

class FinalsState(KnockoutState):
    def simulate_round(self, tournament):
        # Simulate finals match
        print("Simulating Finals...")
        
        self.update_bracket(tournament, "final", "final")

        print("tournament")
        print(tournament.get_knockout_bracket()['round_of_16']['37'].get_teamA().get_countryName())

        # Example logic: Determine winner and optionally transition to completed state
        return tournament.get_knockout_bracket()
        tournament.transition_to(CompletedState())

class CompletedState(TournamentState):
    def simulate_round(self, tournament):
        # Tournament is completed
        print("Tournament completed.")
        tournament.display_results()
        # Optionally, perform final actions or display results
