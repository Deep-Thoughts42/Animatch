import { React, useState, useContext } from 'react';
import { Button } from 'react-bootstrap';
import '../css/app.css'
import SmallScreenContext from './SmallScreenContext';
import ScoreContext from './ScoreContext';
import MiscContext from './MiscContext';
import axios from 'axios';

function AnswerButton(props) {

    // function space

    const smallScreen = useContext(SmallScreenContext)
    const [score, setScore] = useContext(ScoreContext)
    const [imageIdx, setImageIdx, handleRequest, userLogMessage, setUserLogMessage, scoreEarned, setScoreEarned] = useContext(MiscContext)

    function handleClick() {
        if (props.name === props.correct) {
            console.log("Your Answer was correct")
            setScore(score + scoreEarned)
            handleRequest()
            setUserLogMessage("Your answer was correct, good job!")
            setTimeout(() => {
                setUserLogMessage("")
            }, 5000)
            setScoreEarned(10)

        }
        else {
            console.log("Your answer was incorrect, the correct answer was " + props.correct)
            setScore(0)
            setImageIdx(5)
            handleRequest()
            setUserLogMessage("Your answer was incorrect, the correct answer was " + props.correct + ". The game is restarting.")
            setTimeout(() => {
                setUserLogMessage("")
            }, 5000)
            setScoreEarned(10)

        }
    }

    


    return (
        <div className="mb-3 d-flex justify-content-center">
            <Button onClick={handleClick} className={smallScreen ? "button-override-small d-flex justify-self-center justify-content-center" : "button-override d-flex align-items-center justify-content-center justify-self-center"}><h3 style={{ "margin": 0 }}>{props.name}</h3></Button>
        </div>


    )

}

export default AnswerButton;