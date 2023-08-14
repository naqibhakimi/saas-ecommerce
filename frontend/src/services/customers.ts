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

export const _GET_COUNTRIES = gql`
    query _GET_COUNTRIES {
        countries {
            edges {
                node {
                    id
                    iso2
                    iso3
                    numCode
                    name
                    displayName
                    region {
                        id
                        name
                    }
                }
            }
        }
    }
`;
