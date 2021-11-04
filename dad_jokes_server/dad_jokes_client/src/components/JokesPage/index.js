import React, { useState, useEffect } from "react";
import { useJokes } from "../../context/JokesContext";
import JokeCard from "../JokeCard";
import "./JokePage.css";

const JokesPage = () => {
    const { numJokes, getRandomJokes } = useJokes();
    const [ jokes, setJokes ] = useState([]);

    useEffect( async ()=> {
        const newJokes = await getRandomJokes(numJokes)
        setJokes(newJokes);
    }, [numJokes])
    

    return (
        <div>
            <h1>Here are your Jokes!</h1>
            <p 
                style={{ fontStyle:"italic" }}
            >
                Click on a Joke Card to See the Punchline!
            </p>
            <div
                className="card-holder"
            >
                {jokes ? jokes.map( joke => (
                  <JokeCard joke={joke} key={joke.id}/>
                )) : ''}
            </div>
        </div>
    );
};

export default JokesPage;