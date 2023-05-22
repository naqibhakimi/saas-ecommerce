import gql from 'graphql-tag';

export const _KNOWLEDGE_GRAPH = gql`
    query _KNOWLEDGE_GRAPH {
        KnowledgeGraphs {
            edges {
                node {
                    id
                    nodes
                    edges
                }
            }
        }
    }
`;
