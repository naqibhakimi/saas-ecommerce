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

export const _GET_PRODUCT_ID = gql`
    query _GET_PRODUCT_BY_ID($id: ID!) {
        product(id: $id) {
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
`;
