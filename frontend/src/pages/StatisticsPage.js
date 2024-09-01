import React, { useEffect, useState } from 'react';
import axios from 'axios';

function StatisticsPage() {
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

    const totalSimulations = 1000;

    const sortedSummaryStatistics = Object.entries(results.summary_statistics).sort(
      ([teamNameA, statsA], [teamNameB, statsB]) => statsB.winner - statsA.winner
    );
  // Display simulation statistics
  return (
    <div>
      <h1>Simulation Statistics</h1>
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
      </div>
  );
}

export default StatisticsPage;
