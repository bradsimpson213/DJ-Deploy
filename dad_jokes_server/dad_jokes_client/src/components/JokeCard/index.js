import React from "react";
import useToggle from "../../hooks/useToggle";
import "./JokeCard.css"

const JokeCard = ({joke}) => {
    const[ display, toggleDisplay ] = useToggle(false)

    return (
        <div 
        className="joke-card"
        onClick={ () => toggleDisplay()}
        >
            <p 
                className="rating"
                style={{ backgroundColor: joke.rating === "G" ? 
                    'green' : joke.rating === "PG" ? 
                    'orange' : 'red' }}
            >
                Rated: { joke.rating }
            </p>
            <div className="joke-content">
                <p>{ joke.joke_body }</p>
                { display && 
                    <p 
                        className="punchline"
                    >
                        { joke.punchline }
                    </p>      
                }
            
            </div>
            
        </div>
    )
};

export default JokeCard;