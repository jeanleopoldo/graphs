from typing import Union


class Kruskal:
    def __init__(self, graph):
        self.graph       = graph
        self.agm         = []
        self.graph.sort_edges_by_weight()

    
    def algorithm(self):
        edges = self.graph.get_edges()
        for edge in edges:
            u = self.graph.get_node_by_sequence(edge.get_start())
            v = self.graph.get_node_by_sequence(edge.get_end())
            u_reachable = u.get_reachable_nodes()
            v_reachable = v.get_reachable_nodes()
            if u_reachable is not v_reachable:
                self.agm.append(edge)
                x = u_reachable.union(v_reachable)
                for y in x:
                    y.set_reachable_nodes(x)
        weight = 0
        for edge in self.agm:
            weight = edge.get_weight() + weight
        print(weight)
        for edge in self.agm:
            print("{} - {}".format(edge.get_start(), edge.get_end()))
        return self.agm
