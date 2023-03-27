import gql from "graphql-tag";

export const SIGNIN = gql`
mutation SIGNIN($input: SignInInput!){
  signin(input: $input){
    success
    errors
    token
  }
}
`;