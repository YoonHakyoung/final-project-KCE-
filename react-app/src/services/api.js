export const fetchTestCases = async () => {
    const response = await fetch('/testcase');
    return response.json();
  };
  
  export const addTestCase = async (testCase) => {
    const response = await fetch('/testcase', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(testCase),
    });
    return response.json();
  };
  
  export const deleteTestCase = async (testCaseId) => {
    await fetch(`/testcase/${testCaseId}`, {
      method: 'DELETE',
    });
  };
  
  export const runTestCase = async (testCaseId) => {
    await fetch(`/testcase/${testCaseId}/execute`, {
      method: 'GET',
    });
  };
  