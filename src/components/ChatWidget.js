import React, { useState, useEffect, useRef } from 'react';
import { useAuth } from './AuthContext';
import './ChatWidget.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [selectedText, setSelectedText] = useState('');
  const [mode, setMode] = useState('full_book'); // 'full_book' or 'selected_text'
  
  const messagesEndRef = useRef(null);
  const { isAuthenticated, token } = useAuth();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Get selected text from the page
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString();
      if (selectedText.length > 0) {
        setSelectedText(selectedText);
        setMode('selected_text');
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message to UI immediately
    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: inputValue,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Prepare request payload
      const requestBody = {
        message: inputValue,
        mode: selectedText && mode === 'selected_text' ? 'selected_text' : 'full_book',
        ...(selectedText && mode === 'selected_text' && { selected_text: selectedText })
      };

      // Add session ID if exists
      if (sessionId) {
        requestBody.session_id = sessionId;
      }

      // Make API call to backend
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}` // Add auth token if user is logged in
        },
        body: JSON.stringify({ query: inputValue }) // Backend expects 'query' field, not 'message'
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Add assistant message to UI (backend returns just the response text in 'response' field)
      const assistantMessage = {
        id: Date.now(),
        role: 'assistant',
        content: data.response, // Backend returns response in 'response' field
        timestamp: new Date()
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = {
        id: Date.now(),
        role: 'assistant',
        content: 'Sorry, there was an error processing your request. Please try again.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className={`chat-widget ${isOpen ? 'open' : ''}`}>
      {/* Chat widget header */}
      <div className="chat-header" onClick={() => setIsOpen(!isOpen)}>
        <div className="chat-title">Book Assistant</div>
        <div className="chat-toggle">
          {isOpen ? '−' : '💬'}
        </div>
      </div>

      {/* Chat widget body */}
      {isOpen && (
        <div className="chat-body">
          {/* Mode selector */}
          <div className="mode-selector">
            <button 
              className={mode === 'full_book' ? 'active' : ''}
              onClick={() => setMode('full_book')}
            >
              Full Book Context
            </button>
            <button 
              className={mode === 'selected_text' ? 'active' : ''}
              onClick={() => setMode('selected_text')}
              disabled={!selectedText}
              title={selectedText ? '' : 'Select text on the page first'}
            >
              Selected Text Only {selectedText && `(${selectedText.substring(0, 20)}...)`}
            </button>
          </div>

          {/* Messages container */}
          <div className="messages-container">
            {messages.length === 0 ? (
              <div className="welcome-message">
                <p>Hello! I'm your book assistant.</p>
                <p>Ask me questions about the content, or select text on the page and ask questions about it specifically.</p>
              </div>
            ) : (
              messages.map((message) => (
                <div 
                  key={message.id} 
                  className={`message ${message.role === 'user' ? 'user-message' : 'assistant-message'}`}
                >
                  <div className="message-content">
                    {message.content}
                  </div>
                  {message.citations && message.citations.length > 0 && (
                    <div className="citations">
                      <small>Sources: {message.citations.join(', ')}</small>
                    </div>
                  )}
                  <div className="message-timestamp">
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              ))
            )}
            {isLoading && (
              <div className="message assistant-message">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input area */}
          <div className="input-area">
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={selectedText ? "Ask about selected text..." : "Ask a question about the book..."}
              disabled={isLoading}
              rows="2"
            />
            <button 
              onClick={sendMessage} 
              disabled={!inputValue.trim() || isLoading}
              className="send-button"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;