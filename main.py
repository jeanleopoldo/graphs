from core.Graph import Graph
from model.edge import Edge
from model.node import Node
from breadth_first_search.BFS import bfs
from input.input_reader import read_raw_input
import sys

def populate_edges(edges_representation):
    edges = []
    for representation in edges_representation:
        start  = representation[0]
        end    = representation[1]
        weight = representation[2]
        edge   = Edge(start,end,weight)
        edges.append(edge)
    return edges

def populate_nodes(nodes_representation, edges):
    nodes = []
    for representation in nodes_representation:
        aux            = representation.split()
        number         = aux[0]
        edges_for_node = []
        for edge in edges:
            edge_start = edge.get_start()
            if number == edge_start:
                edges_for_node.append(edge)
            
        node = Node(representation, edges_for_node)
        nodes.append(node)
    return nodes

if __name__ == '__main__':
    file_name = sys.argv[1]
    graph_representation = read_raw_input(file_name)
    nodes_representation = graph_representation[0]
    edges_representation = graph_representation[1]

    edges = populate_edges(edges_representation)
    nodes = populate_nodes(nodes_representation, edges)

    # running with every node as a root
    for node in nodes:
        root  = node
        graph = Graph(root, nodes)
        breadth_search = bfs(graph)
        breadth_search.search()
