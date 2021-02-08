
class Graph:
    def __init__(self, root, nodes):
        self.nodes                     = nodes
        self.root                      = root
        self.root.set_has_been_visited = True
        self.root.set_distance_to_root(0)
        

    def get_root(self):
        return self.root
    def qtdVertices(self):
        return len(self.nodes)
    def get_nodes(self):
        return self.nodes
