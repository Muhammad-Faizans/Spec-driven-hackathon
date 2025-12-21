import React, { useEffect, useState } from 'react';
import { useLocation } from '@docusaurus/router';
import TranslationButton from './TranslationButton';

const DocumentTranslation = () => {
  const location = useLocation();
  const [documentContent, setDocumentContent] = useState('');

  // Only work on docs pages
  const isDocsPage = location.pathname.startsWith('/docs/');

  // Extract the content to be translated
  useEffect(() => {
    if (!isDocsPage) return;
    
    // This is a simplified approach - in reality you'd need to extract 
    // the actual markdown content differently
    if (typeof window !== 'undefined') {
      // Wait for the document to be fully rendered 
      const docElement = document.querySelector('article');
      if (docElement) {
        setDocumentContent(docElement.innerText || '');
      }
    }
  }, [isDocsPage]);

  // If we want to add translation capability to document pages
  if (!isDocsPage || !documentContent) return null;

  return (
    <div className="document-translation">
      <TranslationButton 
        content={documentContent} 
        onTranslationComplete={() => {}} 
      />
    </div>
  );
};

export default DocumentTranslation;