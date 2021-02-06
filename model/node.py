class Node:
    def __init__(self, label, edges):
        self.label = label
        self.sequence = label.split()[0]
        self.edges = edges
    
    def get_edges(self):
        return self.edges

    def get_sequence(self):
        return self.sequence