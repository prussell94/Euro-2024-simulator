import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Results = () => {
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch results from the backend
        axios.get('http://localhost:5001/results')
            .then(response => {
                setResults(response.data.data);
            })
            .catch(error => {
                setError(error.message);
            });
    }, []);

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h1>Euro 2024 Tournament Results</h1>
            {/* <ul>
                {results.map((result, index) => (
                    <li key={index}>
                        Match: {result.match}, Score: {result.score}, Stage: {result.stage}
                    </li>
                ))}
            </ul> */}
        </div>
    );
};

export default Results;