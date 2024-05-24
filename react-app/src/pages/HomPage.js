import React, { useState, useEffect } from 'react';
import TestCaseForm from '../components/TestCaseForm';
import TestCaseList from '../components/TestCaseList';
import { fetchTestCases, addTestCase, deleteTestCase, runTestCase } from '../services/api';

function HomePage() {
  const [testCases, setTestCases] = useState([]);

  useEffect(() => {
    fetchTestCases().then(data => setTestCases(data.testData));
  }, []);

  const handleAddTestCase = (testCase) => {
    addTestCase(testCase).then(newTestCase => setTestCases([...testCases, newTestCase]));
  };

  const handleDeleteTestCase = (index) => {
    const testCaseId = testCases[index].test_id;
    deleteTestCase(testCaseId).then(() => {
      setTestCases(testCases.filter((_, i) => i !== index));
    });
  };

  const handleRunTestCase = (index) => {
    const testCaseId = testCases[index].test_id;
    runTestCase(testCaseId);
  };

  return (
    <div>
      <h1>Test Cases</h1>
      <TestCaseForm addTestCase={handleAddTestCase} />
      <TestCaseList testCases={testCases} deleteTestCase={handleDeleteTestCase} runTestCase={handleRunTestCase} />
    </div>
  );
}

export default HomePage;
