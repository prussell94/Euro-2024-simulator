// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [simulationResults, setSimulationResults] = useState(null);

    const simulateTournament = async () => {
        try {
            // Step 1: Trigger simulation
            const simulationResponse = await axios.post('http://localhost:5001/simulate');
            const results = simulationResponse.data;

            // Step 2: Store results
            const storeResponse = await axios.post('http://localhost:5002/results', results);
            const resultsId = storeResponse.data.id;

            // Step 3: Retrieve stored results
            const finalResultsResponse = await axios.get(`http://localhost:5002/results/${resultsId}`);
            setSimulationResults(finalResultsResponse.data);
        } catch (error) {
            console.error("Error during simulation:", error);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Euro 2024 Tournament Simulator</h1>
                <button onClick={simulateTournament}>Simulate Tournament</button>
                {simulationResults && (
                    <div className="results">
                        <h2>Simulation Results</h2>
                        <pre>{JSON.stringify(simulationResults, null, 2)}</pre>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
