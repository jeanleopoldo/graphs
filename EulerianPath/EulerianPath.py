
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
        current_node_index = 0
        while not self.graph.all_edges_have_been_visited():
            try:
                sub_path = self.find_sub_eulerian_path(current_node)
            except Exception:
                print("Not possible to find a euleria path from this node as a start")
                return

            found_edge_to_visit = False
            for node in sub_path:

                if self.graph.has_edge_not_visited(node) and not found_edge_to_visit:
                    found_edge_to_visit = True
                    next_node = node

            if len(self.eulerian_path) !=0:
                current_node_index = self.eulerian_path.index(next_node)
                index              = -1
                aux                = []
                for node in self.eulerian_path:
                    index = index+1
                    if index <= current_node_index or index == len(self.eulerian_path):
                        continue
                    if node is not current_node:
                        aux.append(node)
                
                del self.eulerian_path[current_node_index]
                index = len(self.eulerian_path)-1
                for node in self.eulerian_path:
                    if index >= current_node_index:
                        self.eulerian_path.pop(index)
                        index = index-1
                    else:
                        break

                for node in sub_path:
                    self.eulerian_path.append(node)
                
                for left_node in aux:
                    self.eulerian_path.append(left_node)
            else:
                for node in sub_path:
                    self.eulerian_path.append(node)
            current_node = next_node

    def find_sub_eulerian_path(self,node):
        sub_path     = []
        current_node = node
        found_path   = False
        sub_path.append(current_node)
        
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
    
    def print_path(self):
        for node in self.eulerian_path:
            print("-->", node.get_sequence(), node.get_rotulo())