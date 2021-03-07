from constants.constants import INFINITY
class SPF:
    def __init__(self, graph):
        self.graph = graph
        self.shortes_path = []
        self.nodes = self.graph.get_nodes().copy()
    
    def search_shortest_path(self):

        path = []
        current_node = self.graph.get_root()
        current_node.set_distance_to_root(0)
        self.refresh_structures(current_node)
        
        while self.has_node_not_visited():
            path.append(current_node)
            current_node.set_has_been_visited(True)
            try:
                current_node = self.get_node_min_distance(current_node)
            except Exception:
                break
            self.refresh_structures(current_node)

        for i in range(len(path)):
            print(path[i].get_rotulo())

    def get_node_min_distance(self, current_node):
        distance = INFINITY
        for edge in self.graph.get_node_edges(current_node):
            node = self.graph.get_node_by_sequence(edge.get_end())
            if not node.get_has_been_visited():
                aux = node.get_distance_to_root()
                if aux < distance:
                    node_to_return = node
                    distance = aux
        if node_to_return == None:
            raise Exception
        node_to_return.set_ancestral(current_node)
        return node_to_return

    def has_node_not_visited(self):
        for node in self.nodes:
            if not node.get_has_been_visited():
                return True
        return False

    def refresh_structures(self, current_node):
        for edge in self.graph.get_node_edges(current_node):
            node = self.graph.get_node_by_sequence(edge.get_end())
            aux = edge.get_weight()+current_node.get_distance_to_root()

            if aux < node.get_distance_to_root():
                node.set_distance_to_root(aux)