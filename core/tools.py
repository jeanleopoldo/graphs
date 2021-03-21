def reset_nodes_to_not_visited(nodes):
    for node in nodes:
        node.set_has_been_visited(False)

def reset_edges_to_not_visited(edges):
    for edge in edges:
        edge.set_has_been_visited(False)


def reset(nodes, edges):
    reset_nodes_to_not_visited(nodes)
    reset_edges_to_not_visited(edges)