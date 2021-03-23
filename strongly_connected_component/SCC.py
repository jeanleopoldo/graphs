
from core.tools import reset

class StronglyConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        
    def search(self):
        self.dfs(self.graph)
        transposed_graph = self.graph.get_transpose_graph()
        transposed_graph.sort_nodes_by_end_time()
        reset(transposed_graph.get_nodes(), transposed_graph.get_edges())
        components = self.dfs(transposed_graph)

        index = 1
        for component in components:
            print("{}-component {}".format(index,component))
            index = index+1

    def dfs(self, graph):

        all_components = []
        nodes = graph.get_nodes()
        
        for node in nodes:
            component = []
            if not node.get_has_been_visited():
                self.recursive_dfs(graph, node, component)
            if len(component)>0:
                all_components.append(component)
        return all_components

    def recursive_dfs(self, graph, node, component):
        node.set_has_been_visited(True)
        self.time = self.time+1
        node.set_start_time(self.time)
        component.append(node.get_sequence())

        node_edges = graph.get_node_edges(node)

        for edge in node_edges:
            neighbour = graph.get_node_by_sequence(edge.get_end())

            if not neighbour.get_has_been_visited():
                neighbour.set_ancestral(node)
                self.recursive_dfs(graph, neighbour, component)
        
        self.time = self.time+1
        node.set_end_time(self.time)