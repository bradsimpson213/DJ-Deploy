import React from "react";
import { NavLink } from "react-router-dom";
import { useJokes } from "../../context/JokesContext";
import "./NavBar.css"

const Navbar = () => {

    const { numJokes, setNumJokes } = useJokes();

    return(
        <div 
          className='nav-bar'
        >
             <img 
                    src="https://res.cloudinary.com/app-academy4/image/upload/v1635974577/dad-jokes/why-did-the-litigation-support-professional-cross-the-road-blog-joke-png-300_200_fbffgs.png" 
                    alt="little-site-logo"
                    height="75px"
                    width="125px"
            />
            <NavLink 
                exact to='/jokes'
                className="button-link"
            >
                Jokes Page
            </NavLink>
            <NavLink 
                exact to='/jokes/new'
                className="button-link"
            >
                Add Joke
            </NavLink>
            <div 
                className="jokes-num"
            >
                <label 
                    htmlFor="jokesNum"
                    style={{marginTop: "10px"}}
                >
                    Number of Jokes to display: 
                </label>
                <input 
                    type="number"
                    name="jokesNum"
                    className="input-num" 
                    value={ numJokes }
                    onChange={ (e) => setNumJokes(e.target.value) }    
                /> 
            </div>
            <NavLink 
                exact to='/'
                className="button-link"
            >
                Home
            </NavLink>
        </div>
    )
};

export default Navbar;