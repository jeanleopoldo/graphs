from model.edge import Edge
from constants.constants import INFINITY
class Graph:
    def __init__(self, root,nodes, edges, is_directed):
        self.nodes         = nodes
        self.root          = root
        self.edges         = edges
        self.is_directed   = is_directed
        self.node_to_edges = {}
        self.nodes_map     = {}
        self.init_graph()
        self.root.set_distance_to_root(0)


    def init_graph(self):
        self.populate_map_with_nodes()
        self.populate_map_with_edges()
        self.populate_distances_to_nodes()

    def populate_distances_to_nodes(self):

        self.root.set_distance_to_node(self.root,0)
        for from_node in self.nodes:
            from_node.set_distance_to_root(INFINITY)
            for to_node in self.nodes:
                if from_node.get_sequence() == to_node.get_sequence():
                    continue
                else:
                    from_node.set_distance_to_node(to_node, INFINITY)
        
    def populate_map_with_nodes(self):
        for node in self.nodes:
            self.node_to_edges[node.get_sequence()] = {}
            self.node_to_edges[node.get_sequence()] = []
            self.nodes_map[node.get_sequence()]     = node
    def populate_map_with_edges(self):
            for from_edge in self.edges:
                self.node_to_edges[from_edge.get_start()].append(from_edge)

                if not self.is_directed:
                    to_edge = Edge(from_edge.get_end(), from_edge.get_start(), from_edge.get_weight())
                    self.node_to_edges[to_edge.get_start()].append(to_edge)

                
    def get_nodes_and_edges(self):
        return self.node_to_edges
    def qtdVertices(self):
        return len(self.nodes)
    def qtdArestas(self):
        return len(self.edges)
    def grau(self,node):
        node_edges = self.node_to_edges[node.get_sequence()]
        return len(node_edges)

    def get_node_by_sequence(self, sequence):
        return self.nodes_map[sequence]
    
    def get_root(self):
        return self.root
    def get_nodes(self):
        return self.nodes
    def has_edge_not_visited(self,node):
        edges = self.node_to_edges[node.get_sequence()]
        for edge in edges:
            edge_has_been_visited = edge.get_has_been_visited()
            if not edge_has_been_visited:
                return True
        return False

    def get_node_edges(self, node):
        return self.node_to_edges[node.get_sequence()]
    
    def all_edges_have_been_visited(self):
        for edge in self.edges:
            if not edge.get_has_been_visited():
                return False
        return True
    
    def set_all_edges_to_not_visited(self):
        for edge in self.edges:
            edge.set_has_been_visited(False)

    # for tests purpose only
    def get_root(self):
        return self.root
    
