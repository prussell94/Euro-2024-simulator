import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ResultsComponent = () => {
  const [results, setResults] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to fetch data from results_service
    const fetchResults = async () => {
        try {
            const response = await axios.get('http://localhost:5002/results', {
              headers: {
                'Content-Type': 'application/json'
              }
            });
      } catch (error) {
        setError('Failed to fetch results');
      }
    };

    fetchResults();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Match Results</h2>
      {results.length > 0 ? (
        <ul>
          {results.map((result, index) => (
            <li key={index}>
              {result.match}: {result.score} ({result.stage})
            </li>
          ))}
        </ul>
      ) : (
        <p>No results available</p>
      )}
    </div>
  );
};

export default ResultsComponent;

