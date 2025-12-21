import React, { useState } from 'react';
import { useLocation } from '@docusaurus/router';
import ChatWidget from './components/ChatWidget';
import LoginModal from './components/LoginModal';
import { AuthProvider, useAuth } from './components/AuthContext';
import './CustomRoot.css';

// Separate component to handle auth context within the provider
const RootWithAuth = ({ children }) => {
  const location = useLocation();
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const { loading } = useAuth();

  // Don't show chat widget on auth pages
  const isAuthPage = location.pathname.includes('/login') || location.pathname.includes('/register');

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      {children}
      {!isAuthPage && <ChatWidget />}
      <LoginModal
        isOpen={isLoginModalOpen}
        onClose={() => setIsLoginModalOpen(false)}
      />
    </>
  );
};

const CustomRoot = ({ children }) => {
  return (
    <AuthProvider>
      <RootWithAuth>
        {children}
      </RootWithAuth>
    </AuthProvider>
  );
};

export default CustomRoot;