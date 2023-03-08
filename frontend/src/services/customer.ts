import gql from "graphql-tag";

export const _GET_USERS = gql`
query _GET_USERS{
    users{
      edges{
        node{
          id
          firstName
          lastName
          email
        }
      }
    }
  }`;