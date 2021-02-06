class graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def qtdVertices(self):
        return len(self.nodes)
