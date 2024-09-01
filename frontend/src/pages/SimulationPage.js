import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GroupTable from '../components/GroupTable';
import '../SimulationPage.css';

function SimulationPage() {
  const [results, setResults] = useState({ group_stage: [], knockout_stage: {}, summary_statistics: {} });

useEffect(() => {
  axios.get('http://localhost:5002/results')
    .then(response => {
      console.log("API Response:");
      console.log(response.data);
      setResults(response.data.data);
    })
    .catch(error => {
      console.error("There was an error fetching the results!", error);
    });
}, []);

const fetchResults = () => {
    axios.get('http://localhost:5002/results')
      .then(response => {
        console.log("API Response:");
        console.log(response.data);
        setResults(response.data.data);
      })
      .catch(error => {
        console.error("There was an error fetching the results!", error);
      });
  };

  const simulateTournament = () => {
    axios.post('http://localhost:5006/simulate')  // Assuming this is your endpoint for simulation
      .then(response => {
        console.log("Simulation Response:");
        console.log(response.data);
        fetchResults();  // Fetch the updated results after simulation
      })
      .catch(error => {
        console.error("There was an error simulating the tournament!", error);
      });
  };

const groupStageTables = results.group_stage.reduce((groups, team) => {
    if (!groups[team.Group]) {
      groups[team.Group] = [];
    }
    groups[team.Group].push(team);
    return groups;
  }, {});

  return (
    <div>
      <h1>Simulation Results</h1>
      <button onClick={simulateTournament}>Simulate Tournament</button>

      <h2>Group Stage</h2>
      <div className="group-stage-container">
        {Object.keys(groupStageTables).map((group, index) => (
          <div key={index} className="group-container">
            <GroupTable group={groupStageTables[group]} />
          </div>
        ))}
      </div>

      <h2>Knockout Stage</h2>
      <div className="knockout-stage-container">
      <div className="round round-of-16">
        {/* <div className="matches-container"> */}
          {results.knockout_stage.round_of_16 && (
            <>
              <div key="37" className="match">
                <p>{results.knockout_stage.round_of_16["37"]?.teamA.country_name} {results.knockout_stage.round_of_16["37"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["37"]?.teamB.country_name} {results.knockout_stage.round_of_16["37"]?.team_b_goals_scored}</p>
              </div>
              <div key="39" className="match">
                <p>{results.knockout_stage.round_of_16["39"]?.teamA.country_name} {results.knockout_stage.round_of_16["39"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["39"]?.teamB.country_name} {results.knockout_stage.round_of_16["39"]?.team_b_goals_scored}</p>
              </div>
              <div key="41" className="match">
                <p>{results.knockout_stage.round_of_16["41"]?.teamA.country_name} {results.knockout_stage.round_of_16["41"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["41"]?.teamB.country_name} {results.knockout_stage.round_of_16["41"]?.team_b_goals_scored}</p>
              </div>
              <div key="42" className="match">
                <p>{results.knockout_stage.round_of_16["42"]?.teamA.country_name} {results.knockout_stage.round_of_16["42"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["42"]?.teamB.country_name} {results.knockout_stage.round_of_16["42"]?.team_b_goals_scored}</p>
              </div>
              <div key="43" className="match">
                <p>{results.knockout_stage.round_of_16["43"]?.teamA.country_name} {results.knockout_stage.round_of_16["43"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["43"]?.teamB.country_name} {results.knockout_stage.round_of_16["43"]?.team_b_goals_scored}</p>
              </div>
              <div key="44" className="match">
                <p>{results.knockout_stage.round_of_16["44"]?.teamA.country_name} {results.knockout_stage.round_of_16["44"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["44"]?.teamB.country_name} {results.knockout_stage.round_of_16["44"]?.team_b_goals_scored}</p>
              </div>
              <div key="38" className="match">
                <p>{results.knockout_stage.round_of_16["38"]?.teamA.country_name} {results.knockout_stage.round_of_16["38"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["38"]?.teamB.country_name} {results.knockout_stage.round_of_16["38"]?.team_b_goals_scored}</p>
              </div>
              <div key="40" className="match">
                <p>{results.knockout_stage.round_of_16["40"]?.teamA.country_name} {results.knockout_stage.round_of_16["40"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.round_of_16["40"]?.teamB.country_name} {results.knockout_stage.round_of_16["40"]?.team_b_goals_scored}</p>
              </div>
            </>
          )}
        </div>

        <div className="round quarter-finals">
        {/* <div className="matches-container"> */}

        {results.knockout_stage.quarter_finals && (
            <>
              <div key="45" className="match">
                <p>{results.knockout_stage.quarter_finals["45"]?.teamA.country_name} {results.knockout_stage.quarter_finals["45"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.quarter_finals["45"]?.teamB.country_name} {results.knockout_stage.quarter_finals["45"]?.team_b_goals_scored}</p>
              </div>
              <div key="46" className="match">
                <p>{results.knockout_stage.quarter_finals["46"]?.teamA.country_name} {results.knockout_stage.quarter_finals["46"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.quarter_finals["46"]?.teamB.country_name} {results.knockout_stage.quarter_finals["46"]?.team_b_goals_scored}</p>
              </div>
              <div key="47" className="match">
                <p>{results.knockout_stage.quarter_finals["47"]?.teamA.country_name} {results.knockout_stage.quarter_finals["47"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.quarter_finals["47"]?.teamB.country_name} {results.knockout_stage.quarter_finals["47"]?.team_b_goals_scored}</p>
              </div>
              <div key="48" className="match">
                <p>{results.knockout_stage.quarter_finals["48"]?.teamA.country_name} {results.knockout_stage.quarter_finals["48"]?.team_a_goals_scored}</p>
                <p>{results.knockout_stage.quarter_finals["48"]?.teamB.country_name} {results.knockout_stage.quarter_finals["48"]?.team_b_goals_scored}</p>
              </div>
            </>
          )}
          {/* </div> */}
        </div>

        <div className="round semi-finals">
            {/* <div className="matches-container"> */}

          {results.knockout_stage.semi_finals && Object.keys(results.knockout_stage.semi_finals).map(matchId => (
            <div key={matchId} className="match">
              <p>{results.knockout_stage.semi_finals[matchId].teamA.country_name} {results.knockout_stage.semi_finals[matchId].team_a_goals_scored}</p>
              <p>{results.knockout_stage.semi_finals[matchId].teamB.country_name} {results.knockout_stage.semi_finals[matchId].team_b_goals_scored}</p>
            </div>
          ))}
          {/* </div> */}
        </div>

        <div className="round final">
            {/* <div className="matches-container"> */}

          {results.knockout_stage.final && Object.keys(results.knockout_stage.final).map(matchId => (
            <div key={matchId} className="match">
              <p>{results.knockout_stage.final[matchId].teamA.country_name} {results.knockout_stage.final[matchId].team_a_goals_scored}</p>
              <p>{results.knockout_stage.final[matchId].teamB.country_name} {results.knockout_stage.final[matchId].team_b_goals_scored}</p>
            </div>
          ))}
          {/* </div> */}
        </div>
    </div>
    </div>
  );
}

export default SimulationPage;