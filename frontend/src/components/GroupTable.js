import React from 'react';

const GroupTable = ({ group }) => {
  return (
    <div>
      <h2>Group {group[0].Group}</h2>
      <table>
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Points</th>
            <th>Goals Scored</th>
            <th>Goals Conceded</th>
            <th>Placement</th>
          </tr>
        </thead>
        <tbody>
          {group.map((team, index) => (
            <tr key={index}>
              <td>{team.Country}</td>
              <td>{team.Points}</td>
              <td>{team['Goals Scored']}</td>
              <td>{team['Goals Conceded']}</td>
              <td>{team.Placement}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default GroupTable;
