import {
    ApolloClient,
    ApolloLink,
    HttpLink,
    InMemoryCache,
    split,
} from '@apollo/client';
import { getMainDefinition } from 'apollo-utilities';
import { setContext } from 'apollo-link-context';
import { WebSocketLink } from 'apollo-link-ws';
import { onError } from '@apollo/client/link/error';
import { createUploadLink } from 'apollo-upload-client';
import { customFetch } from '@/utils/helpers';

const getToken = () => {
    if (process.browser && localStorage.getItem('auth')) {
        return JSON.parse(localStorage.getItem('auth') as any).token;
    }
};

const httpOptions = {
    uri: process.env.NEXT_PUBLIC_GRAPHQL_HTTP_URI,
    credentials: 'include',
    fetch: typeof window === 'undefined' ? global.fetch : customFetch,
    fetchOptions: {
        onProgress: progress => {
            console.log(progress);
        },
    },
};

const wsOptions = {
    uri: process.env.NEXT_PUBLIC_GRAPHQL_WS_URI || '',
    options: {
        lazy: true,
        reconnect: true,
        connectionParams: {
            authToken: getToken(),
        },
    },
};

const Options = {
    watchQuery: {
        fetchPolicy: 'no-cache',
        errorPolicy: 'ignore',
    },
    updateQuery: {
        fetchPolicy: 'no-cache',
        errorPolicy: 'ignore',
    },
    query: {
        fetchPolicy: 'no-cache',
        errorPolicy: 'all',
    },
    mutate: {
        fetchPolicy: 'no-cache',
        errorPolicy: 'all',
    },
    subscription: {
        fetchPolicy: 'no-cache',
        errorPolicy: 'all',
    },
};

const authLink = setContext((_, { headers }) => {
    const token =
        localStorage.getItem('auth') &&
        JSON.parse(localStorage.getItem('auth') as any).token;
    return {
        headers: {
            ...headers,
            Authorization: token ? `Bearer ${token}` : '',
        },
    };
});

const wsLink = process.browser ? new WebSocketLink(wsOptions) : null;

const customErrors = new ApolloLink((operation, forward) => {
    // errorStore.setError(null);
    return forward(operation).map(response => {
        // const data = response.data;
        // const errors = getErrorFromReponse(data, "errors");

        // if (errors && errors.length > 0) {
        //   errorStore.setError(errors);
        // }

        return response;
    });
});

const Errors = onError(
    ({ graphQLErrors, networkError, operation, forward }) => {
        if (graphQLErrors) {
            graphQLErrors.map(({ message, locations, path }) => {
                if (
                    message === 'Error decoding signature' ||
                    message === 'Signature has expired'
                ) {
                    localStorage.removeItem('auth');
                }
                console.log(message, locations, path);
            });
        }
        if (networkError) {
            console.log(networkError);
        }

        return forward(operation);
    },
);

const httpLink = ApolloLink.split(
    operation => {
        return operation.getContext().hasUpload;
    },
    createUploadLink(httpOptions),
    new HttpLink(httpOptions),
);

// const httpLink = createUploadLink(httpOptions);

const link = process.browser
    ? split(
          ({ query }) => {
              const { kind, operation } = getMainDefinition(query) as any;
              return (
                  kind === 'OperationDefinition' && operation === 'subscription'
              );
          },
          wsLink as any,
          customErrors.concat(ApolloLink.from([authLink, httpLink, Errors])),
      )
    : customErrors.concat(ApolloLink.from([authLink, Errors, httpLink]));

const ApolloParams = {
    link: customErrors.concat(ApolloLink.from([authLink, Errors, httpLink])),

    cache: new InMemoryCache(),
    defaultOptions: Options,
    connectToDevTools: true,
};

const client = new ApolloClient(ApolloParams as any);

export default client;
