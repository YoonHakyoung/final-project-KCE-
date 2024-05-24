import React from 'react';

function TestCaseList({ testCases, deleteTestCase, runTestCase }) {
  return (
    <ul>
      {testCases.map((test, index) => (
        <li key={test.test_id}>
          {test.test_name}
          <button onClick={() => deleteTestCase(index)}>Delete</button>
          <button onClick={() => runTestCase(index)}>Run</button>
        </li>
      ))}
    </ul>
  );
}

export default TestCaseList;
