import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [testCases, setTestCases] = useState([]);

  useEffect(() => {
    fetch('/testcase')
      .then(response => response.json())
      .then(data => setTestCases(data.testData));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Test Cases</h1>
        <ul>
          {testCases.map(test => (
            <li key={test.test_id}>
              {test.test_name}
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
