import { _KNOWLEDGE_GRAPH } from '@/services/core';
import { useQuery } from '@apollo/client';
import VisNetwork from '@/components/network';


export default function KnowledgeGraph() {
    const { data, error, loading } = useQuery(_KNOWLEDGE_GRAPH);
    if (loading) {
        return <></>;
    }

    if (error) {
        return <></>;
    }

    return (
        <VisNetwork
            edges={data?.KnowledgeGraphs?.edges[0].node.edges}
            nodes={data?.KnowledgeGraphs?.edges[0].node.nodes}
        />
    );
}
