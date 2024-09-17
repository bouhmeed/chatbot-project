// src/SendMessageComponent.js
import React, { useState } from 'react';
import { sendMessage } from './apiService';

const SendMessageComponent = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    try {
      const result = await sendMessage(message);
      setResponse(result.response);
    } catch (error) {
      console.error("Failed to send message", error);
    }
  };

  return (
    <div>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message here"
      />
      <button onClick={handleSend}>Send</button>
      {response && <p>Response: {response}</p>}
    </div>
  );
};

export default SendMessageComponent;
