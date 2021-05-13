from typing import no_type_check
from model.edge import Edge
from constants.constants import INFINITY
from operator import attrgetter
import math
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
            self.residual_network[node.get_sequence()] = []
            self.node_to_edges[node.get_sequence()]    = []
            self.nodes_map[node.get_sequence()]        = node
            

    def populate_map_with_edges(self):
        for from_edge in self.edges:
            from_node_sequence = from_edge.get_start()
            vertex = self.nodes_map[from_node_sequence]
            has = has = self.has_in_list(from_edge)
            if not has:
                self.node_to_edges[vertex.get_sequence()].append(from_edge)
            residual_edge = Edge(from_edge.get_end(), from_edge.get_start(), 0)
            self.residual_network[from_edge.get_end()].append(residual_edge)

            if not from_edge.get_start() in self.floyd_warshall_map:
                self.floyd_warshall_map[from_edge.get_start()] = {}
            self.floyd_warshall_map[from_edge.get_start()][from_edge.get_end()] = from_edge.get_weight()


            if not self.is_directed:
                to_edge = Edge(from_edge.get_end(), from_edge.get_start(), from_edge.get_weight())
                
                has = self.has_in_list(to_edge)

                if not has:
                    self.node_to_edges[to_edge.get_start()].append(to_edge)
                #TODO fill map when not directed

        for node in self.get_nodes():
            if not node.get_sequence() in self.floyd_warshall_map:
                self.floyd_warshall_map[node.get_sequence()] = {}

    def has_in_list(self, to_edge):
        l = self.node_to_edges[to_edge.get_start()]
        has = False
        for j in l:
            if j.get_start()==to_edge.get_start() and j.get_end()==to_edge.get_end():
                has = True
                break
        return has

                
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
        edges = self.residual_network[edge.get_end()]
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
    def set_all_nodes_to_not_visited(self):
        for node in self.nodes:
            node.set_has_been_visited(False)
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
    
    def power_set(self):
        power_set_size = (int) (math.pow(2, len(self.nodes)))
        counter = 0
        j = 0
        power_set = {}
        for counter in range(0, power_set_size):
            partition = []
            for j in range(0, len(self.nodes)):
                if((counter & (1 << j)) > 0):
                    partition.append(self.get_node_by_sequence(str(j)))
            power_set[counter]= partition
        # TODO check if its ordered by key
        return power_set

    def remove_set_with_adjacent_nodes(self,independent_sets):

        to_remove = []
        if len(independent_sets) ==1:
            return independent_sets
        for set in independent_sets:
            for node in independent_sets[set]:
                edges = self.node_to_edges[node.get_sequence()]
                for edge in edges:
                    if self.get_node_by_sequence(edge.get_end()) in independent_sets[set] and set not in to_remove:
                        to_remove.append(set)
        
        for remove in to_remove:
            del independent_sets[remove]
        
        return independent_sets


    def maximal_independent_sets(self):
        independent_sets = {}
        for node in self.nodes:
            not_adjacent_nodes = self.not_adjacent_nodes(node)
            independent_sets[node.get_sequence()] = not_adjacent_nodes
            if node.get_sequence() not in independent_sets or len(independent_sets[node.get_sequence()])==0:
                independent_sets[node.get_sequence()] = [node]
        independent_sets = self.remove_set_with_adjacent_nodes(independent_sets)
        
        max = 0
        for set in independent_sets:
            set_size = len(independent_sets[set])
            if set_size>max:
                max = set_size
        
        max_independent_sets = []
        for set in independent_sets:
            set_size = len(independent_sets[set])
            if set_size == max and self.is_not_contained_in_max_set(max_independent_sets, set):
                max_independent_sets.append(independent_sets[set])
        
        return max_independent_sets


    def is_not_contained_in_max_set(self,max_independent_sets,set):
        for auxiliar_set in max_independent_sets:
            if auxiliar_set is set:
                return False
        return True

    def not_adjacent_nodes(self, node):
        edges = self.get_node_edges(node)

        not_adjacent_nodes = []

        if len(edges)==0:
            not_adjacent_nodes = not_adjacent_nodes+self.nodes
            return not_adjacent_nodes

        nodes_to_remove = []
        for edge in edges:
            for node in self.nodes:
                if edge.get_start()==node.get_sequence():
                    continue
                if edge.get_end()==node.get_sequence():
                    nodes_to_remove.append(edge.get_end())
                    break
        
        

        for adjacent in nodes_to_remove:
            for all in self.nodes:
                found = False
                if all.get_sequence()==adjacent:
                    found = True
                    break
            if not found:
                not_adjacent_nodes.append(all)

        return not_adjacent_nodes
