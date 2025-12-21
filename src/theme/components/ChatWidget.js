import React, { useState, useEffect } from 'react';
import Chatbot from './Chatbot';

const ChatWidget = () => {
  const [selectedText, setSelectedText] = useState('');

  // Listen for text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection.toString().trim();
      if (text.length > 0 && text.length < 500) { // Limit to 500 characters
        setSelectedText(text);
      } else {
        setSelectedText('');
      }
    };

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection); // For keyboard selections
    
    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, []);

  return <Chatbot selectedText={selectedText} />;
};

export default ChatWidget;