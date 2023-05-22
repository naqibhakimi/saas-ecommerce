import gql from 'graphql-tag';

export const _GET_USERS = gql`
    query _GET_USERS {
        users {
            edges {
                node {
                    id
                    firstName
                    lastName
                    email
                }
            }
        }
    }
`;

export const GET_USERS_BY_ORGANIZATION = gql`
    query GET_USERS_BY_ORGANIZATION($organizationId: String) {
        users(organizationId: $organizationId) {
            edges {
                node {
                    id
                    firstName
                    lastName
                    email
                    isActive
                    status {
                        verified
                    }
                }
            }
        }
    }
`;
