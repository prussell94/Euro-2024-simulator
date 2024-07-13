import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GroupTable from './components/GroupTable';

function App() {
  const [results, setResults] = useState({ group_stage: [], knockout_stage: [] });

  useEffect(() => {
    axios.get('http://localhost:5002/results')
      .then(response => {
        console.log(response.data);
        setResults(response.data.data);
      })
      .catch(error => {
        console.error("There was an error fetching the results!", error);
      });
  }, []);

  const groupStageTables = results.group_stage.reduce((groups, team) => {
    if (!groups[team.Group]) {
      groups[team.Group] = [];
    }
    groups[team.Group].push(team);
    return groups;
  }, {});

  return (
    <div>
      <h1>Euro 2024 Simulator</h1>
      <h2>Group Stage</h2>
      {Object.keys(groupStageTables).map((group, index) => (
        <GroupTable key={index} group={groupStageTables[group]} />
      ))}
<h2>Knockout Stage</h2>
      {/* Render Knockout Stage Fixtures */}
      <h3>Round of 16</h3>
      <ul>
        {results.knockout_stage.round_of_16 && Object.keys(results.knockout_stage.round_of_16).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.round_of_16[matchId].teamA.country_name} {results.knockout_stage.round_of_16[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.round_of_16[matchId].teamB.country_name} {results.knockout_stage.round_of_16[matchId].team_b_goals_scored}</p>
            {/* Add more details as needed */}
          </li>
        ))}
      </ul>

      <h3>Quarter Finals</h3>
      <ul>
        {results.knockout_stage.quarter_finals && Object.keys(results.knockout_stage.quarter_finals).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.quarter_finals[matchId].teamA.country_name} {results.knockout_stage.quarter_finals[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.quarter_finals[matchId].teamB.country_name} {results.knockout_stage.quarter_finals[matchId].team_b_goals_scored}</p>
            {/* Add more details as needed */}
          </li>
        ))}
      </ul>

      <h3>Semi Finals</h3>
      <ul>
        {results.knockout_stage.semi_finals && Object.keys(results.knockout_stage.semi_finals).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.semi_finals[matchId].teamA.country_name} {results.knockout_stage.semi_finals[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.semi_finals[matchId].teamB.country_name} {results.knockout_stage.semi_finals[matchId].team_b_goals_scored}</p>
            {/* Add more details as needed */}
          </li>
        ))}
      </ul>

      <h3>Finals</h3>
      <ul>
        {results.knockout_stage.final && Object.keys(results.knockout_stage.final).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.final[matchId].teamA.country_name} {results.knockout_stage.final[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.final[matchId].teamB.country_name} {results.knockout_stage.final[matchId].team_b_goals_scored}</p>
            {/* Add more details as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;



