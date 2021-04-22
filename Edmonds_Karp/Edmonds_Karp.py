class Edmonds_Karp:
    def _init_(self, graph):
        self.graph = graph
        self.queue = []

    def fluxo_maximo(self):
        
        maximum_flux = []
        while True:
            try:
                path = self.edmonds_karp(self)
                

                for edge in path:
                    residual_edge = self.graph.get_residual_edge(edge)
                    residual_value = residual_edge.get_weight()
                    residual_value = residual_value+edge.get_weight()
                    residual_edge.set_weight(residual_value)
                maximum_flux.append(path)
            except:
                break
        

    def edmonds_karp(self):
        root = self.graph.get_root()
        root.set_has_been_visited(True)
        path = []
        self.queue.append(root)
        while len(self.queue) > 0:
            node = self.queue.pop(0)
            edges = self.graph.get_node_edges(node)

            for edge in edges:
                neighbour = self.graph.get_node_by_sequence(edge.get_start())

                residual_edge = self.graph.get_residual_edge(edge)
                if not neighbour.get_has_been_visited() and ((edge.get_weight() - residual_edge.get_weight()) > 0):
                    neighbour.set_has_visited(True)
                    neighbour.set_ancestral(node)
                    end_point = self.graph.get_drain()
                    if neighbour == end_point:
                        path.append(end_point)

                    
                    self.queue.append(neighbour)
        
        raise Exception