
from core.tools import reset

class StronglyConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.stack.append(self.graph.get_root())
        self.path  = []
        
    def search(self):

        self.dfs(self.graph)

        transposed_graph = self.graph.get_transpose_graph()
        reset(transposed_graph.get_nodes(), transposed_graph.get_edges())
        components = self.dfs(transposed_graph)

        index = 1
        for component in components:
            print("{}-component {}".format(index,component))
            index = index+1

    def dfs(self, graph):
        self.time = 0
        all_components = []
        for node in graph.get_nodes():
            if not node.get_has_been_visited():
                component = []
                self.recursive_dfs(node, component)
                all_components.append(component)
        return all_components

    def recursive_dfs(self, node, component):
        node.set_start_time(self.time)
        self.time = self.time+1
        node_edges = self.graph.get_node_edges(node)
        
        for edge in node_edges:
            neighbour = self.graph.get_node_by_sequence(edge.get_end())
            if not neighbour.get_has_been_visited():
                neighbour.set_ancestral(node)
                neighbour.set_has_been_visited(True)
                self.recursive_dfs(neighbour, component)
                component.append(node.get_rotulo())
        self.time = self.time+1
        node.set_end_time(self.time)