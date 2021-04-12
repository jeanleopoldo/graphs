
from core.tools import reset

class StronglyConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        self.all_components = []
        self.component      = []
        
    def search(self):
        
        transposed_graph = self.graph.get_transpose_graph()
        self.dfs(transposed_graph)
        reset(self.graph.get_nodes(), self.graph.get_edges())
        self.component      = []
        self.all_components = []
        self.graph.sort_nodes_by_end_time()
        self.dfs(self.graph)

        index = 1
        for component in self.all_components:
            print("component", index)
            for element in component:
                print(element.get_sequence())
            index = index+1


    def dfs(self, graph):

        nodes = graph.get_nodes()
        
        for node in nodes:
            self.component = []
            if not node.get_has_been_visited():
                self.recursive_dfs(graph, node)
            if len(self.component)>0:
                self.all_components.append(self.component)

    def recursive_dfs(self, graph, node):
        node.set_has_been_visited(True)
        self.time = self.time+1
        node.set_start_time(self.time)

        self.component.append(node)

        node_edges = graph.get_node_edges(node)

        for edge in node_edges:
            neighbour = graph.get_node_by_sequence(edge.get_end())

            if not neighbour.get_has_been_visited():
                neighbour.set_ancestral(node)
                self.recursive_dfs(graph, neighbour)
        
        self.time = self.time+1
        node.set_end_time(self.time)