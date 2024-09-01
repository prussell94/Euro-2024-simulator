# simulation_service.py
from flask import Flask, jsonify, request
from tournament import Tournament
import tournament
import json
import requests
import groups.group_stage
import knockouts
import knockouts.knockout_stage
import pandas as pd
from serialization_visitor import ToDictVisitor
import states
from teams import team_data
from matches.bayesian import BayesianNN


RESULTS_SERVICE_URL = "http://localhost:5002/results"

app = Flask(__name__)

new_tournament = tournament.Tournament(groups.group_stage, knockouts.knockout_match_data.knockout_bracket)

print("knockout bracket before tournament and simulate")
print(knockouts.knockout_match_data.knockout_bracket)

# tournament = Tournament()

@app.route('/simulation_summary', methods=['POST'])
def simulation_summary():

    visitor = ToDictVisitor()

    team_results = {"group_stage": 0, "round_of_16": 0, "quarter_finals": 0, "semi_finals": 0, "runner_up":0, "winner": 0}

    teams_d_ = team_data.teams_dict
    country_tournament_results = {}
    for team in teams_d_.keys():
        country_tournament_results[team] = team_results.copy()

    group_stage = states.GroupStageState()

    for i in range(0, 1000):
        print("country tournament results")
        print(country_tournament_results)

        new_tournament =  tournament.Tournament(group_stage, knockouts.knockout_match_data.knockout_bracket)
        _, _, teams = new_tournament.simulate_tournament()

        for country in country_tournament_results.keys():
            exit_round_country = teams[country].exit_round
            country_tournament_results[country][exit_round_country] += 1
    
    # country_tournament_results.to_dict(orient="records")

    response = send_results_to_results_service(country_tournament_results)

    # group_stage_results, knockout_bracket = new_tournament.simulate_tournament()

    # print("tesitng")
    # visitor = ToDictVisitor()

    # group_stage_results = pd.concat(group_stage_results, ignore_index=True)
    # gs_results_dict = group_stage_results.to_dict(orient="records")

    # for key in knockout_bracket.keys():
    #     for match_id in knockout_bracket[key]:

    #         knockout_bracket[key][match_id] = knockout_bracket[key][match_id].accept(visitor)
            
            # print(json.dumps(knockout_bracket[key][match_id], indent=4))

    # response = send_results_to_results_service(gs_results_dict, knockout_bracket)

    return jsonify({"message": "Tournament simulated successfully."})

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

def send_results_to_results_service(country_tournament_results):
    try:
        payload = {
            "results": {
                "summary_statistics": country_tournament_results,
            }
        }
        response = requests.post(RESULTS_SERVICE_URL, json=payload)
        response.raise_for_status()
        print("response json simualte")
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5007)