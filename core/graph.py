from model.edge import Edge
from constants.constants import INFINITY
from operator import attrgetter
class Graph:
    def __init__(self, root, destination, nodes, edges, is_directed):
        self.nodes              = nodes
        self.root               = root
        self.destination        = destination
        self.edges              = edges
        self.is_directed        = is_directed
        self.node_to_edges      = {}
        self.nodes_map          = {}
        self.floyd_warshall_map = {}
        self.residual_network   = {}
        self.init_graph()
        self.root.set_distance_to_root(0)


    def init_graph(self):
        self.populate_map_with_nodes()
        self.populate_map_with_edges()
        self.populate_distances_to_nodes()

    def populate_distances_to_nodes(self):

        for from_node in self.nodes:
            for to_node in self.nodes:
                if from_node.get_sequence() == to_node.get_sequence():
                    self.floyd_warshall_map[from_node.get_sequence()][to_node.get_sequence()] = 0
                elif not to_node.get_sequence() in self.floyd_warshall_map[from_node.get_sequence()]:
                    self.floyd_warshall_map[from_node.get_sequence()][to_node.get_sequence()] = INFINITY

        
    def populate_map_with_nodes(self):
        for node in self.nodes:
            self.node_to_edges[node.get_sequence()]    = {}
            self.residual_network[node.get_sequence()] = {}
            self.node_to_edges[node.get_sequence()]    = []
            self.nodes_map[node.get_sequence()]        = node
            

    def populate_map_with_edges(self):
        for from_edge in self.edges:
            from_node_sequence = from_edge.get_start()
            vertex = self.nodes_map[from_node_sequence]
            self.node_to_edges[vertex.get_sequence()].append(from_edge)
            residual_edge = Edge(from_edge.get_end(), from_edge.get_start(), 0)
            self.residual_network[vertex.get_sequence()].append(residual_edge)

            if not from_edge.get_start() in self.floyd_warshall_map:
                self.floyd_warshall_map[from_edge.get_start()] = {}
            self.floyd_warshall_map[from_edge.get_start()][from_edge.get_end()] = from_edge.get_weight()


            if not self.is_directed:
                to_edge = Edge(from_edge.get_end(), from_edge.get_start(), from_edge.get_weight())
                self.node_to_edges[to_edge.get_start()].append(to_edge)
                #TODO fill map when not directed

        for node in self.get_nodes():
            if not node.get_sequence() in self.floyd_warshall_map:
                self.floyd_warshall_map[node.get_sequence()] = {}

                
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
    def get_residual_edge(self, edge):
        edges = self.destination[edge.get_start()]
        for r in edges:
            if r.same_edge(edge):
                return r
    
    def get_destination(self):
        return self.destination
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
    def get_distances_between_nodes(self, from_node, to_node):
        return self.floyd_warshall_map[from_node.get_sequence()][to_node.get_sequence()]

    def set_distances_between_nodes(self, from_node, to_node, distance):
        self.floyd_warshall_map[from_node.get_sequence()][to_node.get_sequence()] = distance
    # for tests purpose only
    def get_root(self):
        return self.root
    
    def get_transpose_graph(self):

        edges = []
        for edge in self.edges:
            transposed_edge = Edge(edge.get_end(), edge.get_start(), edge.get_weight())
            edges.append(transposed_edge)

        transposed_graph = Graph(self.root, self.nodes, edges, self.is_directed)
        return transposed_graph

    def sort_nodes_by_end_time(self):
        self.nodes.sort(key = attrgetter('end_time'), reverse = True)

    def sort_edges_by_weight(self):
        self.edges.sort(key = attrgetter('weight'), reverse = False)

    def get_edges(self):
        return self.edges
