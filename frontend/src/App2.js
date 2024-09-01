import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import SimulationPage from './pages/SimulationPage';
import StatisticsPage from './pages/StatisticsPage';
import NavBar from './components/NavBar';
import './App2.css'; // Add this line


function App2() {
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

  return (
    <Router>
      <div>
        <NavBar />
        <Routes>
          <Route path="/" element={<SimulationPage />} />
          <Route path="/statistics" element={<StatisticsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App2;
