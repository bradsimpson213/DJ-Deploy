import React from 'react';
import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa';
// Style imports
import "./Footer.css"
import { profileLinks } from '../../config';


const Footer = () => {

const { linkedin, github, email } = profileLinks;
return (
    <footer className="footer">
        <span className="text">Created by Brad Simpson ©2021</span>
        <a href={github} >
            <FaGithub className="icons"/>
        </a>
        <a href={linkedin} >
            <FaLinkedin className="icons" />
        </a>
        <a href={`mailto:${email}`}>
            <FaEnvelope className="icons" />
        </a> 
    </footer>
)
};
export default Footer;
