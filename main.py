from input.input_reader import read_raw_input
from core.tools import reset
from core.graph import Graph
from model.edge import Edge
from model.node import Node
from breadth_first_search.BFS import bfs
from eulerian_path.EulerianPath import EulerianPath
from dijkstra_spf.spf import SPF
from floyd_warshall.FloydWarshall import FloydWarshall
from strongly_connected_component.SCC import StronglyConnectedComponent

import sys

def breadth_first_search(nodes, edges):
    for node in nodes:
        root  = node
        graph = Graph(root, nodes, edges, False)
        breadth_search = bfs(graph)
        breadth_search.search()
        reset(nodes, edges)

def eulerian_path_finder(nodes,edges):
    for node in nodes:
        root  = node
        graph = Graph(root, nodes, edges, True)
        eulerian_path_search = EulerianPath(graph)
        eulerian_path_search.search()
        reset(nodes, edges)

        print("#####")

def djikstra(nodes, edges):
    for node in nodes:
        print("root-> {} {}".format(node.get_sequence(), node.get_rotulo()))
        root = node
        graph = Graph(root, nodes, edges, True)
        spf = SPF(graph)
        spf.search_shortest_path()
        reset(nodes, edges)

def floyd_warshall(nodes, edges):
    for node in nodes:
        print("root-> {} {}".format(node.get_sequence(), node.get_rotulo()))
        root = node
        graph = Graph(root, nodes, edges, True)
        floyd_warshall = FloydWarshall(graph)
        floyd_warshall.search()
        reset(nodes, edges)

def depth_first_search(nodes, edges):
    root = nodes[0]
    graph = Graph(root, nodes, edges, True)
    dfs = StronglyConnectedComponent(graph)
    dfs.search()


def populate_edges(edges_representation):
    edges = []
    for representation in edges_representation:
        start  = representation[0]
        end    = representation[1]
        weight = representation[2]
        edge   = Edge(start,end,weight)
        edges.append(edge)
    return edges

def populate_nodes(nodes_representation):
    nodes = []
    for representation in nodes_representation:
        node = Node(representation)
        nodes.append(node)
    return nodes

if __name__ == '__main__':
    # TODO get it from file properly
    # file_name = sys.argv[1]
    file_name = 'connected_graph.net'
    graph_representation = read_raw_input(file_name)
    nodes_representation = graph_representation[0]
    edges_representation = graph_representation[1]

    edges = populate_edges(edges_representation)
    nodes = populate_nodes(nodes_representation)

    # running with every node as a root

    # Exercicio 2
    #breadth_first_search(nodes, edges)

    # Exercicio 3
    #eulerian_path_finder(nodes, edges)

    # Exercicio 4
    #djikstra(nodes,edges)

    # Exercicio 5
    #floyd_warshall(nodes,edges)

    depth_first_search(nodes, edges)
    
