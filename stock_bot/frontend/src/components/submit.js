import React, { useState } from 'react';
import { CircularProgress } from '@mui/material';

function App() {
  const [prediction, setPrediction] = useState({});
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const stockSymbol = event.target.elements.stockSymbol.value;
    setLoading(true);

    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ stock_symbol: stockSymbol }),
    });

    const data = await response.json();

    setPrediction(data);
    setLoading(false);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Stock Symbol:
          <input type="text" name="stockSymbol" required />
        </label>
        <button type="submit">Predict</button>
      </form>

      {loading ? (
        <CircularProgress />
      ) : (
        <div> 
          <h2>Prediction Results</h2>
          <p>Next Day Open: {prediction.next_day_open}</p>
          <p>Next Day Close: {prediction.next_day_close}</p>
        </div>
      )}
    </div>
  );
}

export default App;
