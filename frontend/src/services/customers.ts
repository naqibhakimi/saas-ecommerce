import gql from 'graphql-tag';

export const _GET_CUSTOMERS = gql`
    query _GET_CUSTOMERS {
        customers {
            edges {
                node {
                    id
                    fullName
                    phone
                    email
                    numberOfOrders
                }
            }
        }
    }
`;
