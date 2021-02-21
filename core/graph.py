
class Graph:
    def __init__(self, root, nodes, edges):
        self.nodes                     = nodes
        self.root                      = root
        self.edges                     = edges
        self.root.set_has_been_visited = False
        self.nodes_map                 = {}
        self.root.set_distance_to_root(0)
        self.init_graph()


    def init_graph(self):
        self.populate_map_with_nodes()
        self.populate_map_with_edges()
        
    def populate_map_with_nodes(self):
        for node in self.nodes:
            self.nodes_map[node.get_sequence()]           = {}
    def populate_map_with_edges(self):
            for edge in self.edges:
                node_edges = self.nodes_map[edge.get_start()]
                node_edges.append(edge)

    def qtdVertices(self):
        return len(self.nodes)
    def qtdArestas(self):
        return len(self.edges)
    def grau(self,node):
        node_edges = self.nodes_map[node.get_sequence()]
        return len(node_edges)
    
    def get_root(self):
        return self.root
    def get_nodes(self):
        return self.nodes
    
