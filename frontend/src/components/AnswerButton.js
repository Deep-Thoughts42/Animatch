import { React, useState, useContext } from 'react';
import { Button } from 'react-bootstrap';
import '../css/app.css'
import SmallScreenContext from './SmallScreenContext';

function AnswerButton(props) {

    // function space

    const smallScreen = useContext(SmallScreenContext)



    return (
        <div className="mb-3">
            <Button className={smallScreen ? "button-override-small d-flex justify-content-center": "button-override d-flex align-items-center justify-content-center"}><h3 style={{"margin": 0}}>{props.name}</h3></Button>
        </div>

        
    )




}

export default AnswerButton;