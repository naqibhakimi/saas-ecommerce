import gql from 'graphql-tag';
import Index from '../pages/topic/[topicId]';

export const TOPIC_EVENTS = gql`
    subscription TOPIC_EVENTS($id: String) {
        topicEvents(id: $id)
    }
`;
export const _TOPIC = gql`
    query _TOPIC($id: ID!) {
        topic(id: $id) {
            id
            uid
            createdAt
            updatedAt
            name
            about
            aboutTrancated
            jsonPainPointsAndChallenges
            jsonCustomerPreferences
            jsonDesiredFeaturesAndCapabilities
            jsonOpenQuestions
            jsonKnowledgeGaps
            maturity
            jsonTags
            network
            subTopics(first: 4) {
                edges {
                    node {
                        id
                        name
                    }
                }
            }
            meetings {
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
    }
`;

export const _TOPICS = gql`
    query _TOPICS {
        me {
            id
        }
        topics {
            edges {
                node {
                    id
                    uid
                    createdAt
                    updatedAt
                    name
                    maturity
                    about
                    aboutTrancated
                    totalFiles
                    jsonTags
                    subTopics(first: 4) {
                        edges {
                            node {
                                id
                                uid
                                name
                            }
                        }
                    }
                    meetings {
                        edges {
                            node {
                                id
                                uid
                                aiSummary
                            }
                        }
                    }
                }
            }
        }
    }
`;
