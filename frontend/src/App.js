import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GroupTable from './components/GroupTable';
import SummaryStatistics from './components/SummaryStatistics';

function App() {
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

  const groupStageTables = results.group_stage.reduce((groups, team) => {
    if (!groups[team.Group]) {
      groups[team.Group] = [];
    }
    groups[team.Group].push(team);
    return groups;
  }, {});

  const totalSimulations = 1000;

  const sortedSummaryStatistics = Object.entries(results.summary_statistics).sort(
    ([teamNameA, statsA], [teamNameB, statsB]) => statsB.winner - statsA.winner
  );

  // const generateGradient = (index) => {
  //   const startColor = `rgba(173, 216, 230, ${1 - (index / 10)})`; // Light blue with varying opacity
  //   const endColor = `rgba(0, 0, 255, ${1 - (index / 10)})`; // Dark blue with varying opacity
  //   return `linear-gradient(to right, ${startColor}, ${endColor})`;
  // };

  return (
    <div>
      <h1>Euro 2024 Simulator</h1>
      <h2>Summary Statistics</h2>
      <table>
        <thead>
          <tr style={{backgroundColor:"lightblue"}}>
            <th>Team</th>
            <th>Group Stage Exit Probability (%)</th>
            <th>Round of 16 Exit Probability (%)</th>
            <th>Quarter Finals Exit Probability (%)</th>
            <th>Semi Finals Exit Probability (%)</th>
            <th>Runner-up Probability (%)</th>
            <th>Winner Probability (%)</th>
          </tr>
        </thead>
        <tbody>
          {sortedSummaryStatistics.map(([teamName, stats], index) => {
            // Calculate the background color based on the index
            // const hue = (index * 10) % 360; // Adjust the hue value for each row
            // const backgroundColor = `hsl(${hue}, 70%, 90%)`;

            return (
              // <tr key={index}>

              <tr key={teamName} style={{ backgroundColor:"lightsteelblue" }}>
                <td>{teamName}</td>
                <td>{(stats.group_stage / totalSimulations * 100).toFixed(2)}</td>
                <td>{(stats.round_of_16 / totalSimulations * 100).toFixed(2)}</td>
                <td>{(stats.quarter_finals / totalSimulations * 100).toFixed(2)}</td>
                <td>{(stats.semi_finals / totalSimulations * 100).toFixed(2)}</td>
                <td>{(stats.runner_up / totalSimulations * 100).toFixed(2)}</td>
                <td>{(stats.winner / totalSimulations * 100).toFixed(2)}</td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <h2>Group Stage</h2>
      {Object.keys(groupStageTables).map((group, index) => (
        <GroupTable key={index} group={groupStageTables[group]} />
      ))}

      <h2>Knockout Stage</h2>
      <ul>
        {results.knockout_stage.round_of_16 && Object.keys(results.knockout_stage.round_of_16).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.round_of_16[matchId].teamA.country_name} {results.knockout_stage.round_of_16[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.round_of_16[matchId].teamB.country_name} {results.knockout_stage.round_of_16[matchId].team_b_goals_scored}</p>
          </li>
        ))}
      </ul>

      <ul>
        {results.knockout_stage.quarter_finals && Object.keys(results.knockout_stage.quarter_finals).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.quarter_finals[matchId].teamA.country_name} {results.knockout_stage.quarter_finals[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.quarter_finals[matchId].teamB.country_name} {results.knockout_stage.quarter_finals[matchId].team_b_goals_scored}</p>
          </li>
        ))}
      </ul>

      <ul>
        {results.knockout_stage.semi_finals && Object.keys(results.knockout_stage.semi_finals).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.semi_finals[matchId].teamA.country_name} {results.knockout_stage.semi_finals[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.semi_finals[matchId].teamB.country_name} {results.knockout_stage.semi_finals[matchId].team_b_goals_scored}</p>
          </li>
        ))}
      </ul>

      <ul>
        {results.knockout_stage.final && Object.keys(results.knockout_stage.final).map(matchId => (
          <li key={matchId}>
            <p>{results.knockout_stage.final[matchId].teamA.country_name} {results.knockout_stage.final[matchId].team_a_goals_scored}</p>
            <p>{results.knockout_stage.final[matchId].teamB.country_name} {results.knockout_stage.final[matchId].team_b_goals_scored}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;




