import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from "react-router-dom";

import './App.css';
import Nav from './components/Nav'
import Home from './components/Home'
import RulesOfBingo from './components/RulesOfBingo'
import ContactUs from './components/ContactUs';
import History from './components/History';
import ExternalLinks from './components/ExternalLinks';
import AboutUS from './components/AboutUs';


function App() {
    return ( <
        Router >
        <
        Nav / >
        <
        Switch >
        <
        Route path = "/about" >
        <
        AboutUS / >
        <
        /Route> <
        Route path = "/external-links" >
        <
        ExternalLinks / >
        <
        /Route> <
        Route path = "/contact-us" >
        <
        ContactUs / >
        <
        /Route> <
        Route path = "/rules" >
        <
        RulesOfBingo / >
        <
        /Route> <
        Route path = "/history" >
        <
        History / >
        <
        /Route> <
        Route path = "/" >
        <
        Home / >
        <
        /Route> < /
        Switch > <
        /Router>
    );
}

export default App;