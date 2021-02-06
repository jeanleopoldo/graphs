class Graph:
    def __init__(self, root, nodes):
        self.nodes = nodes
        self.root  = root

    def get_root(self):
        return self.root
    def qtdVertices(self):
        return len(self.nodes)
    def get_nodes(self):
        return self.nodes
