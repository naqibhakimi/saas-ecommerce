import gql from "graphql-tag";

export const GET_PRODUCTS = gql`
  query GetProducts {
    products {
      id
      name
      description
    }
  }
`;

export const ADD_PRODUCT = gql`
  mutation AddProduct($name: String!, $description: String!) {
    addProduct(name: $name, description: $description) {
      id
      name
      description
    }
  }
`;