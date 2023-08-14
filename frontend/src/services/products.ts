import gql from 'graphql-tag';

export const _GET_PRODUCTS = gql`
    query _GET_PRODUCTS {
        products {
            edges {
                node {
                    id
                    createdAt
                    updatedAt
                    createdBy {
                        id
                    }
                    updatedBy {
                        id
                    }
                    title
                    subtitle
                    description
                    handle
                    isGiftCard
                    status
                    images {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                    thumbnail
                    weight
                    length
                    height
                    width
                    hsCode
                    originCountry {
                        id
                    }
                    midCode
                    material
                    collection {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                    productType {
                        id
                    }

                    category {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                    tags {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                    price {
                        id
                    }
                    profile {
                        id
                    }
                    taxRate {
                        id
                    }
                    discountable
                    externalId
                    salesChannels {
                        edges {
                            node {
                                id
                            }
                        }
                    }
                    eachUnitCount
                    unitCount
                    unitCountType
                    isExpirable
                    inventory
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
            createdBy {
                id
            }
            updatedBy {
                id
            }
            title
            subtitle
            description
            handle
            isGiftCard
            status
            images {
                edges {
                    node {
                        id
                    }
                }
            }
            thumbnail
            weight
            length
            height
            width
            hsCode
            originCountry {
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
            midCode
            material
            collection {
                edges {
                    node {
                        id
                    }
                }
            }
            productType {
                id
            }

            category {
                edges {
                    node {
                        id
                    }
                }
            }
            tags {
                edges {
                    node {
                        id
                    }
                }
            }
            price {
                id
            }
            profile {
                id
            }
            taxRate {
                id
            }
            discountable
            externalId
            salesChannels {
                edges {
                    node {
                        id
                    }
                }
            }
            eachUnitCount
            unitCount
            unitCountType
            isExpirable
            inventory
        }
    }
`;

export const _CREATE_PRODUCT = gql`
    mutation _CREATE_PRODUCT($input: CreateProductInput!) {
        createProduct(input: $input) {
            success
            errors
        }
    }
`;

export const _Update_PRODUCT = gql`
    mutation _Update_PRODUCT($input: UpdateProductInput!) {
        updateProduct(input: $input) {
            success
            errors
        }
    }
`;
