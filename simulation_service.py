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
from flask_cors import CORS
from matches.bayesian import BayesianNN


RESULTS_SERVICE_URL = "http://localhost:5002/results"

app = Flask(__name__)
CORS(app)

new_tournament = tournament.Tournament(groups.group_stage, knockouts.knockout_match_data.knockout_bracket)

print("knockout bracket before tournament and simulate")
print(knockouts.knockout_match_data.knockout_bracket)

# tournament = Tournament()

@app.route('/simulate', methods=['POST'])
def simulate():

    group_stage_results, knockout_bracket, teams = new_tournament.simulate_tournament()

    print("tesitng")
    visitor = ToDictVisitor()

    group_stage_results = pd.concat(group_stage_results, ignore_index=True)
    gs_results_dict = group_stage_results.to_dict(orient="records")

    for key in knockout_bracket.keys():
        for match_id in knockout_bracket[key]:

            knockout_bracket[key][match_id] = knockout_bracket[key][match_id].accept(visitor)
            
            # print(json.dumps(knockout_bracket[key][match_id], indent=4))

    response = send_results_to_results_service(gs_results_dict, knockout_bracket)

    return jsonify({"message": "Tournament simulated successfully."})

def send_results_to_results_service(group_stage_results, knockout_stage):
    try:
        payload = {
            "results": {
                "group_stage": group_stage_results,
                "knockout_stage": knockout_stage
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
    app.run(debug=True, host='0.0.0.0', port=5006)