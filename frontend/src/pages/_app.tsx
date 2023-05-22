// File: pages/_app.tsx
import React, { useState } from 'react';
import { useEffect } from 'react';
import { Provider } from 'react-redux';
import Router from 'next/router';

import { ApolloProvider } from '@apollo/react-hooks';
import client from '@/services/apolloClient';

import '@/styles/global.css';
import '@/styles/material.css';
import { UserContext } from '@/contexts/user';

import { wrapper } from '@/store/store';

import ErrorsMessage from '@/components/alerts/errorsMessage';
import SuccessMessage from '@/components/alerts/successMessage';

import NonSSRWrapper from '@/utils/nonSSRWrapper';

import TopicEventsBanner from '@/components/topicEventsBanner';

function App({ Component, ...rest }) {
    const { store, props } = wrapper.useWrappedStore(rest);
    const { pageProps } = props;
    const user = JSON.parse(localStorage.getItem('auth') as string)?.user;

    if (pageProps.protected && !user) {
        typeof window !== 'undefined' && Router.push(`/auth/login`);
        return <></>;
    }

    return (
        <div>
            <Provider store={store}>
                <ApolloProvider client={client}>
                    <UserContext.Provider value={user}>
                        <ErrorsMessage />
                        <SuccessMessage />
                        <TopicEventsBanner />
                        <Component {...pageProps} />
                    </UserContext.Provider>
                </ApolloProvider>
            </Provider>
        </div>
    );
}

export default function NoSSRApp(props) {
    return (
        <NonSSRWrapper>
            <App {...props}></App>
        </NonSSRWrapper>
    );
}
