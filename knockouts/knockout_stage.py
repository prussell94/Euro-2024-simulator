import pandas as pd
from knockouts.knockout_match_data import third_place_permutations
from knockouts.knockout_match_data import r16_matches
from knockouts.knockout_match import knockout_match
import knockouts
import random

class KnockoutStage():
    """
    A class representing the knockout stage of euro tournament

    Attributes:
        knockout_rounds (list): list of knockout rounds
    """
    def __init__(self, knockout_rounds):
        self._knockout_rounds = knockout_rounds

# def generateR16(groupStage):
#     r16_1 = knockout_match(37, 45, groupPlacementA='A1', groupPlacementB='C2')
#     r16_2 = knockout_match(38, 48, groupPlacementA='A2', groupPlacementB='B2')
#     r16_3 = knockout_match(39, 45, groupPlacementA='B1')
#     r16_4 = knockout_match(40, 48, groupPlacementA='C1')
#     r16_5 = knockout_match(41, 46, groupPlacementA='F1')
#     r16_6 = knockout_match(42, 46, groupPlacementA='D2', groupPlacementB='E2')
#     r16_7 = knockout_match(43, 47, groupPlacementA='E1')
#     r16_8 = knockout_match(44, 47, groupPlacementA='D2', groupPlacementB='F2')

#     r16_matches= [r16_1, r16_2, r16_3, r16_4, r16_5, r16_6, r16_7, r16_8]
    
#     thirdPlaceRankings=calculateThirdPlaceQualifiers(groupStage)
#     qualifyingThirdPlace=extractQualifyingThirdPlacers(thirdPlaceRankings)
    
#     thirdPlaceMappings = thirdPlacePermutations[qualifyingThirdPlace]

#     for i in range(0, 8):
#         for k in thirdPlaceMappings.keys():
#             if r16_matches[i].get_gameId() == thirdPlaceMappings[k]:
#                 print("can i ?")
#                 r16_matches[i].set_groupPlacementB(k+"3")
#                 print(r16_matches[i].get_groupPlacementB())

#     return r16_matches
    def calculate_third_place_qualifiers(self, group_stage):
        third_place_a=group_stage[0][group_stage[0]['Placement']==3]
        third_place_a['group']="A"
        third_place_b=group_stage[1][group_stage[1]['Placement']==3]
        third_place_b['group']="B"
        third_place_c=group_stage[2][group_stage[2]['Placement']==3]
        third_place_c['group']="C"
        third_place_d=group_stage[3][group_stage[3]['Placement']==3]
        third_place_d['group']="D"
        third_place_e=group_stage[4][group_stage[4]['Placement']==3]
        third_place_e['group']="E"
        third_place_f=group_stage[5][group_stage[5]['Placement']==3]
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

        print("generating initial knockout_round")
        print("r 16 matches")
        print(r16_matches[0].get_teamA())
        print(r16_matches[0].get_teamB())
        return r16_matches
    
    def mapGroupPlacementToTeam(self, r16_matches, group_stage, groups_dict):

        print(group_stage)
        group_tables=pd.concat(group_stage, ignore_index=True)
        for match in r16_matches:
            gameId = match.get_gameId()
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

        return r16_matches
    
    def simulateKnockoutMatch(self, team_a, team_b):
        team_a_goals_scored = team_a.get_offensiveQualityDistribution().get_goal_estimate()[0]
        team_a_goals_conceded = team_a.get_defensiveQualityDistribution().get_goal_estimate()[0]
        team_b_goals_scored = team_b.get_offensiveQualityDistribution().get_goal_estimate()[0]
        team_b_goals_conceded = team_b.get_defensiveQualityDistribution().get_goal_estimate()[0]

        team_a_goals_scored_avg = (team_a_goals_scored+team_b_goals_conceded)/2
        team_b_goals_scored_avg = (team_b_goals_scored+team_a_goals_conceded)/2
    
        # points_distribution = pointsAwarded(teamAGoalsScoredAvg, teamBGoalsScoredAvg)
    
        team_a_goals_scored = round(team_a_goals_scored_avg, 0)
        team_b_goals_scored = round(team_b_goals_scored_avg, 0)

        if(team_a_goals_scored == team_b_goals_scored):
            print((team_a.get_offensiveQualityDistribution().get_goal_estimate()))
            team_a_goals_scored_OT = (team_a.get_offensiveQualityDistribution().get_goal_estimate()[0])/3
            team_a_goals_conceded_OT = (team_a.get_defensiveQualityDistribution().get_goal_estimate()[0])/3
            team_b_goals_scored_OT = (team_b.get_offensiveQualityDistribution().get_goal_estimate()[0])/3
            team_b_goals_conceded_OT = (team_b.get_defensiveQualityDistribution().get_goal_estimate()[0])/3

            team_a_goals_scored_avg_OT = (team_a_goals_scored_OT+team_b_goals_conceded_OT)/2
            team_b_goals_scored_avg_OT = (team_b_goals_scored_OT+team_a_goals_conceded_OT)/2
            team_a_goals_scored_OT = round(team_a_goals_scored_avg_OT, 0)
            team_b_goals_scored_OT = round(team_b_goals_scored_avg_OT, 0) 

            team_a_goals_scored = team_a_goals_scored + team_a_goals_scored_OT
            team_b_goals_scored = team_b_goals_scored + team_b_goals_scored_OT
            
            if(team_a_goals_scored == team_b_goals_scored):
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
                    team_a_goals_scored = team_a_goals_scored + 1
                    print(team_a.get_countryName() + "scores in pk! score is " + team_a.get_countryName())
                elif team_a_PK_score < team_b_PK_score:
                    team_b_goals_scored = team_b_goals_scored + 1
                else:
                    no_winner = True
                    
                    while(no_winner):
                        team_a_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]
                        team_b_shooter_outcome =  random.choices(choices, weights=weights, k=1)[0]

                        if team_a_shooter_outcome > team_b_shooter_outcome:
                            team_a_goals_scored = team_a_goals_scored + 1
                            print(team_a.get_countryName() + "wins in pk overtime!")
                            no_winner = False
                    
                        elif team_a_shooter_outcome < team_b_shooter_outcome:
                            team_b_goals_scored = team_b_goals_scored + 1
                            print(team_b.get_countryName() + "wins in pk overtime!")
                            no_winner = False
                    
                
        # pointsDistribution = pointsAwarded(teamAGoalsScored, teamBGoalsScored)
        team_a.set_goalsScored(team_a_goals_scored)
        team_a.set_goalsConceded(team_b_goals_scored)
        # teamA.set_pointsEarned(pointsDistribution[0])

        team_b.set_goalsScored(team_b_goals_scored)
        team_b.set_goalsConceded(team_a_goals_scored)
        # teamB.set_pointsEarned(pointsDistribution[1])

        print(team_a.get_countryName() + " " + str(team_a_goals_scored) + " " + team_b.get_countryName() + " " + str(team_b_goals_scored))
        return knockout_match(team_a, team_b, team_a_goals_scored, team_b_goals_scored)
        
    # mapGroupPlacementToTeam(r16_matches, gs_concat, groups_dict)
    

