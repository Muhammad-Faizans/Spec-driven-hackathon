import React from 'react';
import { useDoc } from '@docusaurus/plugin-content-docs/client';
import DocItem from '@theme-original/DocItem';
import TranslationButton from '../../components/TranslationButton';

// Safe wrapper component to handle useDoc hook with error handling
const SafeTranslationHeader = () => {
  try {
    // useDoc hook - this should only be called within DocProvider context
    const { metadata } = useDoc();

    if (!metadata) return null;

    const title = metadata?.title || '';
    const frontMatter = metadata?.frontMatter || {};

    return (
      <div className="translation-header">
        <TranslationButton
          content={title + " " + (frontMatter.description || "")}
          onTranslationComplete={() => {}}
        />
      </div>
    );
  } catch (error) {
    // If the hook is called outside of DocProvider context, suppress the error
    // This can happen if the theme override is somehow applied out of context
    console.warn('Translation header not rendered: useDoc called outside DocProvider context');
    return null;
  }
};

// Custom component to wrap the document content with translation functionality
const CustomDocItem = (props) => {
  return (
    <>
      <SafeTranslationHeader />
      <DocItem {...props} />
    </>
  );
};

export default CustomDocItem;