import React from 'react';

const SummaryStatistics = ({ results, totalSimulations }) => (
  <ul>
    {results.summary_statistics && Object.keys(results.summary_statistics).map(teamName => (
      <li key={teamName}>
        <p>{teamName}</p>
        <p>Group Stage Exit Probability: {(results.summary_statistics[teamName]['group_stage'] / totalSimulations * 100).toFixed(2)}%</p>
        <p>Round of 16 Exit Probability: {(results.summary_statistics[teamName]['round_of_16'] / totalSimulations * 100).toFixed(2)}%</p>
        <p>Quarter Finals Exit Probability: {(results.summary_statistics[teamName]['quarter_finals'] / totalSimulations * 100).toFixed(2)}%</p>
        <p>Semi Finals Exit Probability: {(results.summary_statistics[teamName]['semi_finals'] / totalSimulations * 100).toFixed(2)}%</p>
        <p>Runner-up Probability: {(results.summary_statistics[teamName]['runner_up'] / totalSimulations * 100).toFixed(2)}%</p>
        <p>Winner Probability: {(results.summary_statistics[teamName]['winner'] / totalSimulations * 100).toFixed(2)}%</p>
      </li>
    ))}
  </ul>
);

export default SummaryStatistics;
