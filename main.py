import groups.group_stage
import knockouts
import knockouts.knockout_stage
import sys
import states
import tournament
import knockouts.knockout_match_data
from teams import team_data
import copy

def main():

    def simulate_tournament():
        group_stage = states.GroupStageState()
        round_of_16 = states.RoundOf16State()
        quarter_finals = states.QuarterFinalsState()
        semi_finals = states.SemiFinalsState()
        finals = states.FinalsState()

        new_tournament = tournament.Tournament(group_stage, knockouts.knockout_match_data.knockout_bracket)

        group_stage.simulate_round(tournament=new_tournament)

    # knockouts.knockout_match_data.knockout_bracket
        round_of_16.simulate_round(tournament=new_tournament)
        quarter_finals.simulate_round(tournament=new_tournament)
        semi_finals.simulate_round(tournament=new_tournament)
        finals.simulate_round(tournament=new_tournament)

        return new_tournament

    team_results = {"group_stage": 0, "round_of_16": 0, "quarter_finals": 0, "semi_finals": 0, "runner-up":0, "winner": 0}

    teams_d_ = team_data.teams_dict
    country_tournament_results = {}
    for team in teams_d_.keys():
        country_tournament_results[team] = team_results.copy()
    print("country tournament results")
    print(country_tournament_results)

    all_team_results = []
    group_stage = states.GroupStageState()

    original_knockout = copy.deepcopy(knockouts.knockout_match_data.knockout_bracket)

    for i in range(0, 20):
        print("country tournament results")
        print(country_tournament_results)
        
        # knockout = knockouts.knockout_match_data.knockout_bracket
        knockout = copy.deepcopy(original_knockout)

        new_tournament =  tournament.Tournament(group_stage, knockouts.knockout_match_data.knockout_bracket)
        _, _, teams = new_tournament.simulate_tournament()

        # for team in teams.keys():
        #     teams[team] = team_results

        print("this team: ")
        print(teams['England'].get_countryName())
        print(teams['England'].exit_round)
        print(teams['England'].points_earned)

        print(teams['Serbia'].get_countryName())
        print(teams['Serbia'].exit_round)
        print(teams['Serbia'].points_earned)

        print(teams['Denmark'].get_countryName())
        print(teams['Denmark'].exit_round)
        print(teams['Denmark'].points_earned)

        print(teams['Slovenia'].get_countryName())
        print(teams['Slovenia'].exit_round)
        print(teams['Slovenia'].points_earned)

        for country in country_tournament_results.keys():
            exit_round_country = teams[country].exit_round
            country_tournament_results[country][exit_round_country] += 1

        print("testing")

    for k in country_tournament_results.keys():
        print(k)
        print(country_tournament_results[k])

# def main():
#     print(sys.path)
#     group_stage_instance = groups.group_stage.GroupStage()

#     # Call the simulate_group_stage method on the instance
#     gs_result = group_stage_instance.simulate_group_stage()

#     knockout_stage_instance = knockouts.knockout_stage.KnockoutStage(["r16", "qf", "sf", "f"])
#     knockout_stage_instance.generate_initial_knockout_round(gs_result)

#     print(gs_result)
#     r16_matches = knockout_stage_instance.generate_initial_knockout_round(gs_result)

#     print("matchups r16")
#     print(len(r16_matches))
#     print(r16_matches[0].get_teamB())
#     r16_results = []

#     r16_matches = knockout_stage_instance.mapGroupPlacementToTeam(r16_matches, gs_result, groups.groups_data.groups_dict)

#     for match in r16_matches:
#         print(len(r16_matches))
#         r16_result = knockout_stage_instance.simulateKnockoutMatch(match.get_teamA(), match.get_teamB())
#         r16_results.append(r16_result)

#     knockout_stage_instance = knockouts.knockout_stage.KnockoutStage()
#     knockout_stage_instance.get_initial_r16()
#     knockout_stage_instance.simulate_knockout_round()

if __name__ == "__main__":
    main()