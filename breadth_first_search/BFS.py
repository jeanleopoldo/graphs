from core.Graph import Graph
from model.node import Node
class bfs:
    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        self.queue.append(self.graph.get_root())

    def search(self):

        while len(self.queue) != 0:
            current_node       = self.queue.pop()
            current_node_edges = current_node.get_edges()
            graph_nodes        = self.graph.get_nodes()

            for edge in current_node_edges:
                for node in graph_nodes:
                    if node.get_sequence() == current_node.get_sequence():
                        continue

                    if node.get_sequence() == edge.get_end() and not node.get_has_been_visited():
                        distance_to_root    = current_node.get_distance_to_root()+1
                        node.set_has_been_visited(True)
                        node.set_ancestral(current_node)
                        node.set_distance_to_root(distance_to_root)
                        self.queue.append(node)
                        print(distance_to_root)