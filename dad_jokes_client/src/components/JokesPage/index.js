import React, { useState, useEffect } from "react";
import { useJokes } from "../../context/JokesContext";
import JokeCard from "../JokeCard";
import "./JokePage.css";


const JokesPage = () => {
    const { numJokes, getRandomJokes } = useJokes();
    const [ jokes, setJokes ] = useState([]);
    const [ toggle, setToggle] = useState(false)

    // rewrite below async in useEffect
    const getAsyncJokes = async () => {
        const newJokes = await getRandomJokes(numJokes)
        setJokes(newJokes);
    }

    useEffect( ()=> {
        getAsyncJokes()
    }, [numJokes, toggle])
    

    return (
        <div>
            <h1>Here are your Jokes!</h1>
            <p 
                style={{ fontStyle:"italic" }}
            >
                Click the joke card to reveal its punchline!
            </p>
            <div
                className="card-holder"
            >
                {jokes ? jokes.map( joke => (
                  <JokeCard joke={joke} key={joke.id}/>
                )) : ''}
            </div>
            <button
                onClick={ () => setToggle(prevState => !prevState)}
                className="refresh-button"
            >
                Refresh Tomfoolery!
            </button>
        </div>
    );
};

export default JokesPage;