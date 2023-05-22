import gql from 'graphql-tag';

export const _CREATE_MEETING = gql`
    mutation _CREATE_MEETING($input: CreateMeetingInput!) {
        createMeeting(input: $input) {
            success
            errors
            meeting {
                id
                uid
                title
                date
            }
        }
    }
`;

export const _UPDATE_MEETINGS = gql`
    mutation _UPDATE_MEETINGS($input: UpdateMeetingInput!) {
        updateMeeting(input: $input) {
            success
            errors
        }
    }
`;

export const _MEETING = gql`
    query _MEETING($id: ID!) {
        Meeting(id: $id) {
            id
            uid
            createdAt
            updatedAt
            notes
        }
    }
`;

export const _MEETINGS = gql`
    query _MEETINGS {
        Meetings {
            edges {
                node {
                    id
                    uid
                    createdAt
                    title
                    jsonSummary
                    aiSummary
                    topicSet(last: 4) {
                        edges {
                            node {
                                id
                                name
                            }
                        }
                    }
                }
            }
        }
    }
`;
