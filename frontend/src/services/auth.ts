import gql from 'graphql-tag';

export const SIGNIN = gql`
    mutation SIGNIN($input: SignInInput!) {
        signin(input: $input) {
            success
            errors
            token
            user {
                id
                uid
                email
                firstName
                lastName
            }
        }
    }
`;

export const SIGNUP = gql`
    mutation SIGNUP($input: SignupInput!) {
        signup(input: $input) {
            success
            errors
        }
    }
`;

export const RESEND_ACTIVATION_EMIAL = gql`
    mutation RESEND_ACTIVATION_EMIAL($input: ResendActivationEmailInput!) {
        resendActivationEmail(input: $input) {
            success
            errors
        }
    }
`;

export const VERIFY_ACCOUNT = gql`
    mutation VERIFY_ACCOUNT($input: VerifyAccountInput!) {
        verifyAccount(input: $input) {
            success
            errors
            token
            user {
                id
                email
                firstName
                lastName
                groupName
            }
        }
    }
`;

export const SENT_PASSWORD_RESET_EMAIL = gql`
    mutation SENT_PASSWORD_RESET_EMAIL($input: SendPasswordResetEmailInput!) {
        sendPasswordResetEmail(input: $input) {
            success
            errors
        }
    }
`;

export const PASSWORD_RESET = gql`
    mutation PASSWORD_RESET($input: PasswordResetInput!) {
        passwordReset(input: $input) {
            success
            errors
        }
    }
`;
