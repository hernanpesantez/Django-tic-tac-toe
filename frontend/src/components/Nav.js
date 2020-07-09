import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function Nav() {
    return(
    <nav id='nav'>
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/about">About Us</Link>
            </li>
            <li>
                <Link to="/contact-us">Contact us</Link>
            </li>
            <li>
                <Link to="/rules">Rules of the Game</Link>
            </li>
            <li>
                <Link to="/history">History</Link>
            </li>
            <li>
                <Link to="/external-links">Other places to play bing</Link>
            </li>
            <li>
                <a href="https://www.google.com/search?q=bingo&rlz=1C5CHFA_enUS852US852&oq=bingo&aqs=chrome..69i57j69i59j46l2j0j69i61l3.1781j0j4&sourceid=chrome&ie=UTF-8">google search link</a>
            </li>
        </ul>
    </nav>
    );
}

export default Nav;