import React, { useState, useEffect } from 'react';
import './TranslationButton.css';

const TranslationButton = ({ content, onTranslationComplete }) => {
  const [isTranslating, setIsTranslating] = useState(false);
  const [translatedContent, setTranslatedContent] = useState(null);
  const [showToggle, setShowToggle] = useState(false);
  const [currentLanguage, setCurrentLanguage] = useState('en'); // 'en' or 'ur'

  // Check if content has been translated before
  useEffect(() => {
    const savedTranslation = localStorage.getItem(`translation_${getContentHash(content)}`);
    if (savedTranslation) {
      setTranslatedContent(savedTranslation);
      setShowToggle(true);
    }
  }, [content]);

  const getContentHash = (str) => {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash; // Convert to 32bit integer
    }
    return hash.toString();
  };

  const translateContent = async () => {
    if (isTranslating) return;

    setIsTranslating(true);

    try {
      // Get the full content to translate (this might need adjustment based on how it's called)
      const response = await fetch('/api/v1/translate/translate-chapter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: content,
          source_lang: 'en',
          target_lang: 'ur'
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Save translation to localStorage for caching
      const contentHash = getContentHash(content);
      localStorage.setItem(`translation_${contentHash}`, data.translated_content);
      
      setTranslatedContent(data.translated_content);
      setCurrentLanguage('ur');
      setShowToggle(true);
      onTranslationComplete && onTranslationComplete(data.translated_content);
    } catch (error) {
      console.error('Translation error:', error);
      alert('Error translating content. Please try again.');
    } finally {
      setIsTranslating(false);
    }
  };

  const toggleLanguage = () => {
    if (currentLanguage === 'ur' && content) {
      setCurrentLanguage('en');
    } else if (translatedContent) {
      setCurrentLanguage('ur');
    }
  };

  const getCurrentContent = () => {
    if (currentLanguage === 'ur' && translatedContent) {
      return translatedContent;
    }
    return content;
  };

  return (
    <div className="translation-container">
      <div className="translation-controls">
        <button 
          className={`translate-btn ${isTranslating ? 'loading' : ''}`}
          onClick={currentLanguage === 'en' ? translateContent : toggleLanguage}
          disabled={isTranslating}
        >
          {isTranslating ? (
            <>
              <span className="spinner"></span> Translating...
            </>
          ) : currentLanguage === 'en' ? (
            '.Translate to Urdu'
          ) : (
            'Back to English'
          )}
        </button>
      </div>
      
      {showToggle && (
        <div className="language-toggle">
          <button 
            className={currentLanguage === 'en' ? 'active' : ''}
            onClick={() => setCurrentLanguage('en')}
            disabled={currentLanguage === 'en'}
          >
            English
          </button>
          <button 
            className={currentLanguage === 'ur' ? 'active' : ''}
            onClick={() => translatedContent && setCurrentLanguage('ur')}
            disabled={currentLanguage === 'ur' || !translatedContent}
          >
            Urdu
          </button>
        </div>
      )}
      
      <div className="translated-content">
        {getCurrentContent()}
      </div>
    </div>
  );
};

export default TranslationButton;