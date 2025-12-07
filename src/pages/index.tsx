import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';
import Chatbot from '../theme/components/Chatbot';
import styles from './index.module.css';
import { useEffect, useState } from 'react';
import React from 'react';
// uvicorn backend.src.main:app --reload --host 127.0.0.1 --port 8000

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={styles.heroSection}>
      <div className={styles.heroContainer}>
        <div className={styles.heroContent}>
          <div className={styles.heroText}>
            <span className={styles.heroBadge}>🤖 AI-Powered Learning</span>
            <Heading as="h1" className={styles.heroTitle}>
              {siteConfig.title}
            </Heading>
            <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
            <p className={styles.heroDescription}>
              Master the fundamentals of physical AI and humanoid robotics through
              comprehensive courses, interactive examples, and hands-on projects.
            </p>
            <div className={styles.heroButtons}>
              <Link
                className={clsx('button button--primary button--lg', styles.primaryButton)}
                to="/docs/overview">
                Start Learning
              </Link>
              <Link
                className={clsx('button button--outline button--lg', styles.secondaryButton)}
                to="/blog">
                Read Blog
              </Link>
            </div>
          </div>
          <div className={styles.heroVisual}>
            <div className={styles.heroCard}>
              <div className={styles.cardIcon}>🤖</div>
              <h3>Interactive Learning</h3>
              <p>Engage with AI-powered content and real-time assistance</p>
            </div>
            <div className={styles.heroCard}>
              <div className={styles.cardIcon}>⚡</div>
              <h3>Hands-On Projects</h3>
              <p>Build real-world applications with guided tutorials</p>
            </div>
            <div className={styles.heroCard}>
              <div className={styles.cardIcon}>🎯</div>
              <h3>Expert Guidance</h3>
              <p>Learn from industry professionals and researchers</p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();

  const [selectedText, setSelectedText] = React.useState('');

  const handleTextSelection = React.useCallback(() => {
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length > 0) {
      setSelectedText(selection.toString());
    } else {
      setSelectedText('');
    }
  }, []);

  // Add event listener on mount to capture text selections
  React.useEffect(() => {
    document.addEventListener('mouseup', handleTextSelection);
    // Clean up listener on unmount
    return () => {
      document.removeEventListener('mouseup', handleTextSelection);
    };
  }, [handleTextSelection]);

  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <Chatbot selectedText={selectedText} />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
