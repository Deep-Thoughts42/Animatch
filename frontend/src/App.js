import logo from './images/logo.svg';
import './css/app.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Container, Row, Col, Image } from 'react-bootstrap';
import { useState, useEffect } from 'react';
// Component Imports
import SmallScreenContext from './components/SmallScreenContext';
import AnswerButton from './components/AnswerButton';
import axios from 'axios';


function App() {

  const [smallScreen, setSmallScreen] = useState(false);
  // To use in components, use "const smallScreen = useContext(SmallScreenContext);"
  // This needs to be done after importing useContext and the component itself
  useEffect(() => {
    if (window.innerWidth <= 1000) {
      setSmallScreen(true)
    }
    handleRequest()

  }, [])

  const widthChanged = () => {
    if (window.innerWidth <= 1000) {
      setSmallScreen(true)
    }
    else {
      setSmallScreen(false)
    }

  }

  window.addEventListener('resize', widthChanged)


  const [imageStrings, setImageStrings] = useState([])
  const [options, setOptions] = useState([])
  const [answer, setAnswer] = useState("")



  const [imageIdx, setImageIdx] = useState(0)

  function handleTimer() {
    let idx = 1;

    let changeInterval = setInterval(() => {
      setImageIdx(idx)
      idx++;
      if (idx > 5) {
        clearInterval(changeInterval)
      }
      
    }, 1000)

  }

  function handleRequest() {
    axios({
      method: 'get',
      url: 'https://vedaantv.pythonanywhere.com/generate',  
    })
      .then((res) => {
        // console.log(res.data);
        setImageStrings(res.data.image_strings)
        setAnswer(res.data.answer)
        setOptions(res.data.options)
      })
      .catch((err) => {
        
        console.log(err)
      });

  }






  return (
    <div className="">
      <SmallScreenContext.Provider value={smallScreen}>
        <Container fluid='lg' className="c-w change-font mt-5 ">
          <Row className="text-center">
            <h1>Welcome to <span className="fw-700 text-blue">Who's that Character!</span></h1>
            <h3>Your goal is to correctly identify as many characters as possible. Good Luck!</h3>
          </Row>
          <Row className=" mt-5">
            <Col lg="6" className="text-center d-flex flex-column align-items-center">
              <h4 className="mb-3">Who is this character?</h4>
              <Image rounded src={`data:image/jpg;base64,${imageStrings[imageIdx]}`} className={smallScreen ? "mb-4 dims-small" : "mb-4 dims-rel"} />
              <h4>Score: <span className="text-blue fw-700">0</span></h4>
              <Button onClick={handleTimer}>Test Timer</Button>

            </Col>
            <Col lg="6" className="mt-3 text-center d-flex flex-column align-items-center ">
              <div className="align-self-center">
                <AnswerButton name={options[0]} correct={answer} />
                <AnswerButton name={options[1]} correct={answer}/>
                <AnswerButton name={options[2]} correct={answer}/>
                <AnswerButton name={options[3]} correct={answer}/>

              </div>
              <Button onClick={handleRequest}>Test</Button>
              

            </Col>
          </Row>

        </Container>



      </SmallScreenContext.Provider>

    </div>
  );
}

export default App;
