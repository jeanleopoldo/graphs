class Node:
    def __init__(self, label, edges):
        self.label    = label
        self.sequence = label.split()[0]
        self.edges    = edges
        self.has_been_visited = False
    
    def get_edges(self):
        return self.edges
    def get_sequence(self):
        return self.sequence
    def get_ancestral(self):
        return self.ancestral
    def get_distance_to_root(self):
        return self.distance_to_root
    def get_has_been_visited(self):
        return self.has_been_visited
    
    def set_has_been_visited(self, has):
        self.has_been_visited = has
    def set_ancestral(self, ancestral):
        self.ancestral = ancestral
    def set_distance_to_root(self, distance_to_root):
        self.distance_to_root = distance_to_root