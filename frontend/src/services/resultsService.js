// src/services/resultsService.js
import axios from 'axios';

const BASE_URL = 'http://localhost:5002';

const getResults = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/results`);
        console.log(response.data)
        return response.data;
    } catch (error) {
        console.error("Error fetching results:", error);
        throw error;
    }
};

const postResults = async (results) => {
    try {
        const response = await axios.post(`${BASE_URL}/results`, { results }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error posting results:", error);
        throw error;
    }
};

export default {
    getResults,
    postResults
};
