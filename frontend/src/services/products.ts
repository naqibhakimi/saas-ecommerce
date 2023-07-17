import gql from 'graphql-tag';

export const _GET_PRODUCTS = gql`
    query _GET_PRODUCTS {
        products {
            edges {
                node {
                    id
                    createdAt
                    updatedAt
                    updatedBy {
                        id
                        firstName
                        lastName
                    }
                    title
                    subtitle
                    description
                    handle
                    isGiftCard
                    status
                    thumbnail
                    weight
                    length
                    height
                    width
                    originCountry
                    midCode
                    material
                    discountable
                    externalId
                }
            }
        }
    }
`;
