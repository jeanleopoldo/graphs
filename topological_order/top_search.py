class top_search:
    def __init__(self, graph):
        self.graph = graph
        self.init_time =  0
        self.top_list = []

    def search_top(self):
        nodes = self.graph.get_nodes()
        for node in nodes:
            if not node.get_has_been_visited():
                self.DFS(node)
        
        for node in self.top_list:
            print(node.get_rotulo(), "--> ")
        return self.top_list

    def DFS(self, node):
        node.set_has_been_visited(True)
        self.init_time = self.init_time + 1
        node.set_start_time(self.init_time)

        edges = self.graph.get_node_edges(node)

        for edge in edges:
            next_node = self.graph.get_node_by_sequence(edge.get_end())
            if not next_node.get_has_been_visited():
                self.DFS(next_node)
        self.init_time = self.init_time + 1
        node.set_end_time(self.init_time)
        self.top_list.insert(0,node)