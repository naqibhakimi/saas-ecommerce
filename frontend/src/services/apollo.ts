import { ApolloClient, HttpLink, InMemoryCache, split } from '@apollo/client';
import { getMainDefinition } from 'apollo-utilities';
import { setContext } from 'apollo-link-context';
import { WebSocketLink } from 'apollo-link-ws';

// Create an instance of the HttpLink that will be used for sending GraphQL requests over HTTP
// const httpLink = new HttpLink({
//   uri: process.env.GRAPHQL_HTTP_URI,
// });

// Create an instance of the setContext function from apollo-link-context
// to set the authorization header on each request with the JWT token
// const authLink = setContext((_, { headers }) => {
//   // Get the authentication token from local storage if it exists
//   const token = localStorage.getItem('token');
//   // Return the headers to the context so httpLink can read them
//   return {
//     headers: {
//       ...headers,
//       authorization: token ? `Bearer ${token}` : "",
//     }
//   }
// });

// // Create an instance of the WebSocketLink that will be used for sending GraphQL subscriptions over WebSockets
// const wsLink = new WebSocketLink({
//   uri: process.env.GRAPHQL_WS_URI,
//   options: {
//     reconnect: true,
//   },
// });

// // Use the split function from the apollo-link library to split operations 
// // based on their type (query or subscription) and send them over the appropriate link
// const splitLink = split(
//   ({ query }) => {
//     // Get the main definition of the query
//     const definition = getMainDefinition(query);
//     // Return true if the operation is a subscription
//     return (
//       definition.kind === 'OperationDefinition' &&
//       definition.operation === 'subscription'
//     );
//   },
//   wsLink, // Use the WebSocketLink for subscriptions
//   authLink.concat(httpLink), // Concatenate the authLink and the httpLink for queries
// );


// const wsLink = process.browser ? new WebSocketLink({ // if you instantiate in the server, the error will be thrown
//   uri: 'ws://localhost:8000/graphql',
//   options: {
//     reconnect: true
//   }
// }) : null;

const httplink = new HttpLink({
    uri: 'http://localhost:8000/graphql',
    headers: {
      'Content-Type': 'application/json',
    },
    // fetchOptions: {
    //   mode: 'no-cors'
    // }
});

// const link = process.browser ? split( //only create the split in the browser
//   // split based on operation type
//   ({ query }) => {
//     const { kind, operation } = getMainDefinition(query);
//     return kind === 'OperationDefinition' && operation === 'subscription';
//   },
//   wsLink,
//   httplink,
// ) : httplink;


// Create an instance of the ApolloClient that will manage the data cache and communication with the API
const client = new ApolloClient({
  link: httplink,
  cache: new InMemoryCache(),
});

// Export the client as the default export
export default client;
