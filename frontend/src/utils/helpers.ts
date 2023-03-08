
export function convertEdgeToList(edges: [record: { node: any}]){
    return edges.map(record => record.node)
}