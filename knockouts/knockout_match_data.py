from knockouts.knockout_match import knockout_match
import teams
from teams.quality_distribution import QualityDistribution

third_place_permutations = {("A", "B", "C", "D"):{"A": 39, "B": 43, "C":40, "D": 41}, ("A", "B", "C", "E"): {"A": 39, "E": 43, "C":40, "D": 41}, ("A", "B", "C", "F"): {"A": 39, "F": 43, "C":40, "D":41},
        ("A", "B", "D", "E"): {"D": 39, "E": 43, "A": 40, "B": 41}, ("A", "B", "D", "F"): {"D": 39, "F": 43, "A": 40, "B": 41}, ("A", "B", "E", "F"): {"E": 39, "B": 43, "F": 40, "A":41},
         ("A", "C", "D", "E"): {"E": 39, "C": 43, "D": 40, "A": 41}, ("A", "C", "D", "F"): {"F": 39, "C": 43, "D": 40, "A": 41}, ("A", "C", "E", "F"): {"E": 39, "C": 43, "F": 40, "A": 41},
         ("A", "D", "E", "F"): {"E": 39, "D": 43, "F": 40, "A": 41}, ("B", "C", "D", "E"): {"E": 39, "B": 43, "D": 40, "C": 41}, ("B", "C", "D", "F"): {"F": 39, "C": 43, "D": 40, "B": 41},
        ("B", "C", "E", "F"): {"F": 39, "C": 43, "E": 40, "B": 41}, ("B", "D", "E", "F"): {"F": 39, "D": 43, "E": 40, "B": 41}, ("C", "D", "E", "F"): {"F":39, "D": 43, "E": 40, "C": 41}}

r16_1 = knockout_match(game_id="37", next_game_id="45", groupPlacementA='A1', groupPlacementB='C2')
r16_2 = knockout_match(game_id="38", next_game_id="48", groupPlacementA='A2', groupPlacementB='B2')
r16_3 = knockout_match(39, 45, groupPlacementA='B1')
r16_4 = knockout_match(40, 48, groupPlacementA='C1')
r16_5 = knockout_match(41, 46, groupPlacementA='F1')
r16_6 = knockout_match(42, 46, groupPlacementA='D2', groupPlacementB='E2')
r16_7 = knockout_match(43, 47, groupPlacementA='E1')
r16_8 = knockout_match(44, 47, groupPlacementA='D1', groupPlacementB='F2')

r16_matches = [r16_1, r16_2, r16_3, r16_4, r16_5, r16_6, r16_7, r16_8]

qf_1 = knockout_match(45, 49)
qf_2 = knockout_match(46, 49)
qf_3 = knockout_match(47, 50)
qf_4 = knockout_match(48, 50)

qf_matches = [qf_1, qf_2, qf_3, qf_4]

sf_1 = knockout_match(50, 52)
sf_2 = knockout_match(51, 52)

sf_matches = [sf_1, sf_2]

final = knockout_match(52, None)

knockout_bracket = {
        "round_of_16": {"37": knockout_match(game_id="37", next_game_id="45", teamA=teams.team.Team("", [], QualityDistribution(1.0, .5), QualityDistribution(1.0, .5)), teamB =teams.team.Team("", [], QualityDistribution(1.0, .5), QualityDistribution(1.0, .5)), groupPlacementA='A1', groupPlacementB='C2'), 
                            "38": knockout_match(game_id="38", next_game_id="48", groupPlacementA='A2', groupPlacementB='B2'), 
                            "39": knockout_match(game_id="39", next_game_id="45", groupPlacementA='B1'),
                            "40": knockout_match(game_id="40", next_game_id="48", groupPlacementA='C1'), 
                            "41": knockout_match(game_id="41", next_game_id="46", groupPlacementA='F1'), 
                            "42": knockout_match(game_id="42", next_game_id="46", groupPlacementA='D2', groupPlacementB='E2'),
                            "43": knockout_match(game_id="43", next_game_id="47", groupPlacementA='E1'), 
                            "44": knockout_match(game_id="44", next_game_id="47", groupPlacementA='D1', groupPlacementB='F2')}, 

        "quarter_finals": {"45": knockout_match(game_id="45", next_game_id="49"), 
                               "46": knockout_match(game_id="46", next_game_id="49"), 
                               "47": knockout_match(game_id="47", next_game_id="50"), 
                               "48": knockout_match(game_id="48", next_game_id="50")},
        "semi_finals": {"49": knockout_match(game_id="49", next_game_id="51"), 
                            "50": knockout_match(game_id="50", next_game_id="51")}, 
        "final": {"51": knockout_match(game_id="51", next_game_id=None)}}
