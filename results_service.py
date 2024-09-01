import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stored_results = {
    "group_stage": [],
    "knockout_stage": {},
    "summary_statistics": {}
}

@app.route('/results', methods=['POST', 'GET'])
def process_results():
    if request.method == 'POST':
        data = request.json
        if "results" in data:
            stored_results["group_stage"] = data["results"].get("group_stage", [])
            stored_results["knockout_stage"] = data["results"].get("knockout_stage", {})
            stored_results["summary_statistics"] = data["results"].get("summary_statistics", {})
            print(data)
            return jsonify({"status": "success", "message": "Results processed successfully", "data": stored_results}), 200
        else:
            return jsonify({"status": "error", "message": "No results found in request"}), 400
    
    elif request.method == 'GET':
        return jsonify({"status": "success", "data": stored_results}), 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)



# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# dummy_results = [
#     {"match": "Team A vs Team B", "score": "2-1", "stage": "Group Stage"},
#     {"match": "Team C vs Team D", "score": "1-1", "stage": "Group Stage"}
# ]

# @app.route('/results', methods=['GET', 'POST'])
# def process_results():
#     if request.method == 'GET':
#         return jsonify({"status": "success", "data": dummy_results}), 200

#     if request.method == 'POST':
#         data = request.json
#         print("Received data:", data)
#         # Process the received JSON data (data["results"]) as needed
#         return jsonify({"status": "success", "message": "Results received"}), 200

# if __name__ == "__main__":
#     app.run(port=5002, debug=True)
