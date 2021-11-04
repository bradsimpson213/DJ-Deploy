import React from 'react';
import { Route, Switch } from 'react-router-dom';
import './App.css';
// component imports
import Footer from "./components/Footer";
import Home from "./components/Home";
import JokesPage from './components/JokesPage';
import JokesForm from './components/JokesForm';
import Navbar from './components/Navbar';


const App = () => {

  return (
    <div className="App">
      <Switch>
        <Route exact path='/'>
          <Home/>
        </Route>
        <Route exact path='/jokes'>
          <Navbar/> 
          <JokesPage/> 
        </Route>
        <Route exact path='/jokes/new'> 
          <Navbar/>
          <JokesForm/>
        </Route>
      </Switch>
      <Footer />
    </div>
  );
}

export default App;
