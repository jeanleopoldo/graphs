
from constants.constants import INFINITY


class Edmonds_Karp:
    def __init__(self, graph):
        self.graph        = graph
        self.queue        = []
        self.maximum_flux = []
        self.flow         = 0

    def find_maximum_flow(self):
        
        while True:
            try:
                path = self.bfs()

                self.calculate_flow(path)
                for edge in path:
                    residual_edge  = self.graph.get_residual_edge(edge)
                    residual_value = residual_edge.get_weight()
                    residual_value = residual_value+edge.get_weight()
                    edge_value     = residual_value-edge.get_weight()
                    edge.set_weight(edge_value)
                    residual_edge.set_weight(residual_value)
                self.maximum_flux.append(path)
                self.graph.set_all_nodes_to_not_visited()
                self.queue.clear()
            except: 
                break
        
        print(self.flow)
    
    def calculate_flow(self, path):

        value = INFINITY
        for edge in path:
            if edge.get_weight() < value:
                value = edge.get_weight()

        self.flow = self.flow+value

    def bfs(self):
        root = self.graph.get_root()
        root.set_has_been_visited(True)
        path = []
        self.queue.append(root)
        while len(self.queue) > 0:
            node  = self.queue.pop(0)
            edges = self.graph.get_node_edges(node)

            for edge in edges:
                neighbour = self.graph.get_node_by_sequence(edge.get_end())

                residual_edge = self.graph.get_residual_edge(edge)
                if not neighbour.get_has_been_visited() and ((edge.get_weight() - residual_edge.get_weight()) > 0):
                    neighbour.set_has_been_visited(True)
                    neighbour.set_ancestral(node)
                    end_point = self.graph.get_destination()
                    path.append(edge)
                    if neighbour == end_point:
                        return self.get_path(path)
                self.queue.append(neighbour)
        
        raise Exception

    def get_path(self, path):
        
        minimum_path = []
        index        = len(path)-1
        current_edge = path[index]
        minimum_path.append(current_edge)
        while index>-1:
            index = index-1
            for edge in path:
                if current_edge.get_start() == edge.get_end():
                    minimum_path.append(edge)
                    current_edge = edge
                    break
        return minimum_path