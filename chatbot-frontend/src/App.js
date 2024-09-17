import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [endpoint, setEndpoint] = useState('inquiry'); // Default endpoint

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`http://127.0.0.1:5000/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      if (data.error) {
        setResponse(data.error); // Display error message
      } else {
        setResponse(data.response);
      }
    } catch (error) {
      console.error("Error sending message", error);
      setResponse('Failed to get a response from the server.');
    }
  };

  return (
    <div className="App">
      <h1>Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <select onChange={(e) => setEndpoint(e.target.value)} value={endpoint}>
          <option value="inquiry">Inquiry</option>
          <option value="complaint">Complaint</option>
          <option value="recommendation">Recommendation</option>
          <option value="process_message">Process Message</option>
        </select>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
      <div>
        <h2>Response</h2>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
