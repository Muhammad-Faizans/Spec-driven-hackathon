import React from 'react';
import type { ReactNode, HTMLAttributes } from 'react';

interface HeadingProps extends HTMLAttributes<HTMLHeadingElement> {
  as: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6';
  children: ReactNode;
}

export default function Heading({ as, children, ...props }: HeadingProps) {
  const Component = as;
  return <Component {...props}>{children}</Component>;
}

