from core.Graph import Graph

class bfs:
    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        self.queue.append(self.graph.get_root())

    def search(self):
        index = 0
        visited_nodes = []
        while len(self.queue) != 0:
            current_node       = self.queue.pop()
            current_node_edges = current_node.get_edges()
            print("{} : {}".format(index, current_node.get_sequence()))

            index = index+1
            graph_nodes = self.graph.get_nodes()
            for edge in current_node_edges:
                for node in graph_nodes:
                    if node.get_sequence() == current_node.get_sequence():
                        continue
                    if node.get_sequence() == edge.get_end() and node.get_sequence() not in visited_nodes:
                        self.queue.append(node)
                        visited_nodes.append(node.get_sequence())