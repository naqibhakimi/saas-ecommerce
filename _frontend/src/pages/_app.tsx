// File: pages/_app.tsx
import React from 'react';
import App from 'next/app';

import { ApolloProvider } from '@apollo/react-hooks';
import client from '@/services/apollo';

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props;
    return (
      <div>
        <ApolloProvider client={client}>
          <Component {...pageProps} />
        </ApolloProvider>
      </div>
    );
  }
}

export default MyApp;