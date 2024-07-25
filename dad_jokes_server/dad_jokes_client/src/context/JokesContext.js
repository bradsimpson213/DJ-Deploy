import React, { createContext, useContext, useState } from "react";


export const JokesContext = createContext()

export const JokesProvider = (props) => {
  const [numJokes, setNumJokes] = useState(3)

  const getRandomJokes = async (num) => {
    if ( num > 40) {
      alert(`${numJokes} is too many jokes! You will laugh too hard and die!`)
      return;
    }
    
    const response = await fetch(`/api/jokes/jokes/${num}`);
    const data = await response.json();
    const {jokes} = data
    return jokes

    // const selectedJokes =[];
    // for(let i = 1; i <= num; i++ ){
    //   let joke = starterJokes[Math.floor((Math.random() * starterJokes.length))]
    //   while (selectedJokes.includes(joke)){
    //     joke = starterJokes[Math.floor((Math.random() * starterJokes.length))]
    //   }
    //   selectedJokes.push(joke);
    // }
    // return selectedJokes;
  };

  return (
    <JokesContext.Provider value={{numJokes, setNumJokes, getRandomJokes}}>
      {props.children}
    </JokesContext.Provider>
  )
}

export const useJokes = () => {
  return useContext(JokesContext)
}