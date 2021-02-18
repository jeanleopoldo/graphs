
class EulerianPath:
    def __init__(self, graph):
        self.graph = graph


def all_nodes_have_odd_degree(self):
    nodes = self.graph.get_nodes()

    if len(nodes) == 0:
        return False

    for node in nodes:
        edges = node.get_edges()
        if len(edges) % 2 != 0:
            return False
    return True

def get_not_visited_edge(self, edges):

    for edge in edges:
        has_been_visited = edge.get_has_been_visited()
        if not has_been_visited:
            return edge
    raise Exception("This graph does not have a Eulerian Path.")


def search(self):
    if not all_nodes_have_odd_degree():
        return []

    nodes = self.graph.get_nodes()
    eulerian_path = []

    while len(nodes)>0:
        node = nodes.pop()

        try:
            edges = node.get_edges()
        except:
            return []

        edge = get_not_visited_edge(edges)

    raise Exception("not implemented yet")
