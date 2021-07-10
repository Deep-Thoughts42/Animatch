import logo from './images/logo.svg';
import './css/app.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Container, Row, Col  } from 'react-bootstrap';
import { useState, useEffect } from 'react';
// Component Imports
import SmallScreenContext from './components/SmallScreenContext';



function App() {

  const [smallScreen, setSmallScreen] = useState(false);
  // To use in components, use "const smallScreen = useContext(SmallScreenContext);"
  // This needs to be done after importing useContext and the component itself
  useEffect(() => {
    if (window.innerWidth <= 1000) {
      setSmallScreen(true)
    }

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




  return (
    <div className="">
      <SmallScreenContext.Provider value={smallScreen}>
        <Container fluid='lg' className="c-w change-font mt-5 ">
          <Row className="text-center">
            <h1>Welcome to <span className="fw-700 text-blue">Who's that Waifu!</span></h1>
            <h3>Your goal is to correctly identify as many characters as possible. Good Luck!</h3>
          </Row>
          <Row className=" mt-5">
            <Col className="text-center  align-items-center d-flex flex-column align-items-center">
              <h2 >Image will go here</h2>
              <h4>Score: <span className="text-blue fw-700">0{}</span></h4>
            
            </Col>
            <Col>
            </Col>
          </Row>

        </Container>



      </SmallScreenContext.Provider>
      
    </div>
  );
}

export default App;
