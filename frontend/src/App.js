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
    <div>
      <SmallScreenContext.Provider value={smallScreen}>
        <Container fluid='lg' className="c-w change-font mt-5">
          <h2>Test</h2>
          <Button>Test</Button>

        </Container>



      </SmallScreenContext.Provider>
      
    </div>
  );
}

export default App;
