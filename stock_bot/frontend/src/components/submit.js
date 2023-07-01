import React, { useState } from 'react';
import { CircularProgress } from '@mui/material';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import SendIcon from '@mui/icons-material/Send';

const button_theme = createTheme({
  palette: {primary: {main: '#3CD070'}, text: {primary: '#ffffff'}}
});

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
    <div className = "ret"> 
      <div className = "results">
        {(
          <div> 
            <h2>Prediction Results</h2>
            <p>Next Day Open: {prediction.next_day_open}</p>
            <p>Next Day Close: {prediction.next_day_close}</p>
          </div>
        )}
      </div>

      <div className = "form">
        <form onSubmit={handleSubmit}>
          <input className = "input" type="text" name="stockSymbol" required /> 
          <ThemeProvider theme = {button_theme}>
            <Button className = "button" variant="contained" type = "submit"> <SendIcon /> </Button>
          </ThemeProvider>
        </form>        
      </div>
    </div>
  );
}

export default App;
