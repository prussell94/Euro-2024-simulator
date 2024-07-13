import groups.group_stage
import knockouts
import knockouts.knockout_stage
import sys
import states
import tournament
import knockouts.knockout_match_data

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

    new_tournament =  tournament.Tournament(states.GroupStageState(), knockouts.knockout_match_data.knockout_bracket)
    new_tournament.simulate_tournament()
    print("testing")

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