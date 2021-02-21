from model.TypesOfEdge import LEAVING
from model.edge import Edge
class Graph:
    def __init__(self, root, nodes, edges):
        self.nodes                     = nodes
        self.root                      = root
        self.edges                     = edges
        self.root.set_has_been_visited = False
        self.node_to_edges             = {}
        self.nodes_map                 = {}
        self.edges_map                 = {}
        self.root.set_distance_to_root(0)
        self.init_graph()


    def init_graph(self):
        self.populate_map_with_nodes()
        self.populate_map_with_edges()
        
    def populate_map_with_nodes(self):
        for node in self.nodes:
            self.node_to_edges[node.get_sequence()] = {}
            self.node_to_edges[node.get_sequence()][LEAVING]  = []
            self.nodes_map[node.get_sequence()]               = node
    def populate_map_with_edges(self):
            for from_edge in self.edges:
                self.node_to_edges[from_edge.get_start()][LEAVING].append(from_edge)

                to_edge = Edge(from_edge.get_end(), from_edge.get_start(), from_edge.get_weight())
                self.node_to_edges[to_edge.get_start()][LEAVING].append(to_edge)
                self.edges_map[from_edge] = to_edge
                self.edges_map[to_edge] = from_edge
                

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
        edges = self.node_to_edges[node.get_sequence()][LEAVING]
        for edge in edges:
            edge_has_been_visited = edge.get_has_been_visited()
            if not edge_has_been_visited:
                return True
        return False

    def update_visited_edges(self, edge):
        edge.set_has_been_visited(True)
        self.edges_map[edge].set_has_been_visited(True)
    def get_node_edges(self, node):
        return self.node_to_edges[node.get_sequence()][LEAVING]
    
    def all_edges_have_been_visited(self):
        for edge in self.edges:
            if not edge.get_has_been_visited():
                return False
        return True
    
