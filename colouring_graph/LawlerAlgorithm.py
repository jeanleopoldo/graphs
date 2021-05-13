from core.graph import Graph
from constants.constants import INFINITY


class LawlerColouringGraphAlgorithm:
    def __init__(self, graph):
        self.graph = graph
    
    def colour(self):
        power_set = self.graph.power_set()
        X = self.init_colour_array(power_set)

        for s in power_set:
            if s == 0:
                continue
            Xs = INFINITY
            
            nodes = self.get_nodes_in_set(power_set[s])
            edges = self.get_nodes_edges(nodes)
            g = Graph(nodes[0], nodes[len(nodes)-1], nodes, edges, False)
            I = g.maximal_independent_sets()
            

            for independent_set in I:
                i = self.find_index(power_set, nodes, independent_set)
                Xi = X[i]+1
                if Xi < Xs:
                    X[s] = Xi

        print("Número minimo de colorações: {}".format(X[len(X)-1]))
    
    def find_index(self, power_set, s, independent_set):
        s_minus_I = []

        for node in s:
            has = False
            for independent in independent_set:
                if node.get_sequence() == independent.get_sequence():
                    has = True
                    break
            if not has:
                s_minus_I.append(node)



        for index in power_set:
            indexed_list = power_set[index]
            if indexed_list == s_minus_I:
                return index

    def get_nodes_edges(self, nodes):
        edges = []
        for node in nodes:
            node_edges = self.graph.get_node_edges(node)
            for node_edge in node_edges:
                if self.edge_belong_to_graph(nodes, node_edge):
                    edges.append(node_edge)
        return edges

    def edge_belong_to_graph(self,nodes, edge):
        
        for node in nodes:
            if edge.get_end() == node.get_sequence():
                return True
        return False
        
    def get_nodes_in_set(self, set):
        nodes = []
        for node in set:
            nodes.append(self.graph.get_node_by_sequence(node.get_sequence()))
        return nodes

    def init_colour_array(self, power_set):
        colour_array = []
        colour_array.append(0)
        for i in range(len(power_set)-1):
            colour_array.append(INFINITY)
        return colour_array