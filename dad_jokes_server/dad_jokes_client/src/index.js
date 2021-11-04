import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from "react-router-dom";
import './index.css';
import App from './App';
import { JokesProvider } from "./context/JokesContext"


ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <JokesProvider>
        <App />
      </JokesProvider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);


