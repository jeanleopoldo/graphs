
class EulerianPath:
    def __init__(self, graph):
        self.graph         = graph
        self.eulerian_path = []


    def get_not_visited_edge(self, node):
        edges = self.graph.get_node_edges(node)
        for edge in edges:
            has_been_visited = edge.get_has_been_visited()
            if not has_been_visited:
                return edge
        raise Exception("This graph does not have a Eulerian Path.")


    def search(self):
        current_node       = self.graph.get_root()
        keep_searching = True
        while keep_searching:
            try:
                sub_path = self.find_sub_eulerian_path(current_node)
            except Exception:
                print("Not possible to find a eulerian path for this graph")
                return

            try:
                next_node = self.find_next_node_as_root(sub_path)
            except Exception:
                keep_searching = False
                if not self.graph.all_edges_have_been_visited():
                    print("Not possible to find a eulerian path for this graph")
                    return

            if len(self.eulerian_path) == 0:
                self.add_sub_path_to_list(sub_path)
            else:
                self.add_nodes_to_path(sub_path, next_node)
                
            
            if keep_searching:
                current_node = next_node
        
        self.print_path()

    def add_sub_path_to_list(self, sub_path):
        for node in sub_path:
            self.eulerian_path.append(node)

    def add_nodes_to_path(self, sub_path, next_node):
        
        current_node_index = self.eulerian_path.index(next_node)
        nodes_to_shift = self.get_nodes_to_shift(current_node_index)

        for node in sub_path:
            self.eulerian_path.append(node)
        
        index = len(nodes_to_shift)-1
        for i in range(len(nodes_to_shift)):
            shifted_node = nodes_to_shift.pop(index)
            self.eulerian_path.append(shifted_node)
            index=index-1

    def find_next_node_as_root(self, sub_path):
        for node in sub_path:
            if self.graph.has_edge_not_visited(node):
                return node
        raise Exception("There are no nodes with edges not visited in sub_path")

    def find_sub_eulerian_path(self,node):
        sub_path     = []
        current_node = node
        found_path   = False
        sub_path.append(current_node)
        
        # TODO this may cause inifinite loop
        while not found_path:
            edge      = self.get_not_visited_edge(current_node)
            self.graph.update_visited_edges(edge)
            next_node = self.graph.get_node_by_sequence(edge.get_end())
            current_node = next_node
            sub_path.append(current_node)
            if next_node.get_sequence() == sub_path[0].get_sequence():
                found_path = True
        
        if not found_path:
            raise Exception
        else:
            return sub_path
    
    def get_nodes_to_shift(self, current_node_index):
        index          = len(self.eulerian_path)-1
        nodes_to_shift = []
        while index>=current_node_index:
            node = self.eulerian_path.pop(index)
            nodes_to_shift.append(node)
            index = index-1
        nodes_to_shift.pop(len(nodes_to_shift)-1)
        return nodes_to_shift
    
    def print_path(self):
        for node in self.eulerian_path:
            print("-->", node.get_sequence(), node.get_rotulo())