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
from topological_order.top_search import top_search
from kruskal_msf.kruskal import Kruskal

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

def strongly_connected_component(nodes, edges):
    root = nodes[0]
    graph = Graph(root, nodes, edges, True)
    dfs = StronglyConnectedComponent(graph)
    dfs.search()

def topological_algorithm(nodes, edges):
    root = nodes[0]
    graph = Graph(root, nodes, edges, True)
    topological_search = top_search(graph)
    result = topological_search.search_top()

def kruskal_algorithm(nodes,edges):
    root = nodes[0]
    graph = Graph(root, nodes, edges, False)
    algorithm = Kruskal(graph)
    algorithm.algorithm()

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
    
    algorithm = sys.argv[1]
    file_name = sys.argv[2]
    graph_representation = read_raw_input(file_name)
    nodes_representation = graph_representation[0]
    edges_representation = graph_representation[1]

    edges = populate_edges(edges_representation)
    nodes = populate_nodes(nodes_representation)

    # Exercicio 1
    if algorithm == "1":
        breadth_first_search(nodes, edges)
    # Exercicio 2
    elif algorithm == "2":
        eulerian_path_finder(nodes, edges)
    # Exercicio 3
    elif algorithm == "3":
        djikstra(nodes,edges)
    # Exercicio 4
    elif algorithm == "4":
        floyd_warshall(nodes,edges)
    # Exercicio 5
    elif algorithm == "5":
        strongly_connected_component(nodes, edges)
    # Exercicio 6
    elif algorithm == "6":
        topological_algorithm(nodes,edges)
    # Exercicio 7
    elif algorithm == "7":
        kruskal_algorithm(nodes,edges)
    
