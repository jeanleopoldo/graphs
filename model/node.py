class Node:
    def __init__(self, label):
        self.sequence           = label.split()[0]
        self.label              = label[2:-1]
        self.has_been_visited   = False
        self.distances_to_nodes = {}
        self.ancestral          = None
    
    def get_rotulo(self):
        return self.label
    def get_sequence(self):
        return self.sequence
    def get_ancestral(self):
        return self.ancestral
    def get_has_been_visited(self):
        return self.has_been_visited
    def get_distance_to_node(self, node):
        return self.distances_to_nodes[node.get_sequence()]

    def exist_key_in_map_distances(self, node):
        if node.get_sequence() in self.distances_to_nodes:
            return True
        return False
    def get_distance_to_root(self):
        return self.distance_to_root

    def set_has_been_visited(self, b):
        self.has_been_visited = b
    def set_ancestral(self, ancestral):
        self.ancestral = ancestral
    def set_distance_to_node(self, node, distance):
        self.distances_to_nodes[node.get_sequence()] = distance
    def set_distance_to_root(self, distance):
        self.distance_to_root = distance
    