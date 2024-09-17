// src/MessageComponent.js
import React, { useState } from 'react';
import { sendMessage } from './apiService';

const MessageComponent = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await sendMessage(message);
      setResponse(result.response);
    } catch (error) {
      setResponse("Error sending message.");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
      <p>Response: {response}</p>
    </div>
  );
};

export default MessageComponent;
