import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import JokeCard from '../JokeCard';
import "./Home.css"


const Home = () => {
    const [joke, setJoke] = useState({})

    const getJoke = async () => {
        const response = await fetch('/api/jokes/');
        const data = await response.json();
        setJoke(data)
    };

    useEffect( ()=> {
        getJoke()
    }, [])
 
    return (
        <div className='main-page-container'>
            <h1>Welcome to Dad Jokes!</h1>
            <div 
                style={
                    {
                    display:"flex", 
                    flexDirection: "column",
                    alignItems: "center"
                    }
                }
            >
                <img 
                    src="https://res.cloudinary.com/app-academy4/image/upload/v1635974577/dad-jokes/why-did-the-litigation-support-professional-cross-the-road-blog-joke-png-300_200_fbffgs.png" 
                    alt="loading-bar"
                    height="250px"
                    width="350px"
                />
            <div>
            <div>
                <JokeCard joke={ joke } />
            </div>
            </div>
                <p 
                    style={{ fontStyle:"italic", fontSize:"20px" }}
                >
                    Click the joke card to reveal its punchline!
                </p>
                <Link 
                    to="/jokes" 
                    className="button-link" 
                >
                    Enter Site
                </Link>
            </div>
        </div>
    )
}

export default Home;
