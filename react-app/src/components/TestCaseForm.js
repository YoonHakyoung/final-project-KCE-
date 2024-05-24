import React, { useState } from 'react';

function TestCaseForm({ addTestCase }) {
  const [formData, setFormData] = useState({
    target_url: '',
    test_name: '',
    user_num: '',
    user_plus_num: '',
    interval_time: '',
    plus_count: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    addTestCase(formData);
    setFormData({
      target_url: '',
      test_name: '',
      user_num: '',
      user_plus_num: '',
      interval_time: '',
      plus_count: ''
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="target_url" value={formData.target_url} onChange={handleChange} placeholder="Target URL" required />
      <input type="text" name="test_name" value={formData.test_name} onChange={handleChange} placeholder="Test Name" required />
      <input type="number" name="user_num" value={formData.user_num} onChange={handleChange} placeholder="Initial Users" required />
      <input type="number" name="user_plus_num" value={formData.user_plus_num} onChange={handleChange} placeholder="Additional Users" required />
      <input type="number" name="interval_time" value={formData.interval_time} onChange={handleChange} placeholder="Interval Time" required />
      <input type="number" name="plus_count" value={formData.plus_count} onChange={handleChange} placeholder="Plus Count" required />
      <button type="submit">Save</button>
    </form>
  );
}

export default TestCaseForm;
