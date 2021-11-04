import React from "react"
import useFormInput from '../../hooks/useFormInput';
import { useHistory } from "react-router-dom"

const JokeForm = () => {
    const [jokeBody, handleJokeBody, resetJokeBody] = useFormInput('');
    const [jokePunchline, handlePunchline, resetPunchline] = useFormInput('');
    const [jokeRating, handleRating, resetRating] = useFormInput('G');
    let history = useHistory();

    const resetForm = () => {
        resetJokeBody();
        resetPunchline();
        resetRating();
     }

    const handleSubmit = async (event) => {
        event.preventDefault();

        const newJoke = {
            joke_body: jokeBody,
            punchline: jokePunchline,
            rating: jokeRating,
        };
        console.log(newJoke)
        const res = await fetch('/api/jokes/addjoke', {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify(newJoke),
        });
        const data = await res.json();
        console.log(data)
        resetForm()
        history.push('/jokes')

    }

    return(
        <div>
            <h1> Add a New Joke </h1>
            <form
                onSubmit={ handleSubmit }
            >
                <div>
                    <label htmlFor="joketext">
                            Joke body: 
                    </label>
                    <textarea 
                        name="joketext"
                        value={ jokeBody }
                        onChange={ handleJokeBody }
                    />
                </div>
                <div>
                    <label htmlFor="punchline">
                            Punchline: 
                    </label>
                    <textarea 
                        name="punchline"
                        value={ jokePunchline }
                        onChange={ handlePunchline }
                    />
                </div>
                <div>
                    <label htmlFor="rating-select">Rating Select: </label>
                        <select 
                            name="rating-select"
                            value={ jokeRating }
                            onChange={ handleRating }
                        >
                            <option value="G">Rated G</option>
                            <option value="PG">Rated PG</option>
                            <option value="R">Rated R</option>
                        </select>
                </div>
                <button type="submit">
                    Submit Joke
                </button>
            </form>
        </div>
    );
};

export default JokeForm;