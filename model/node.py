from constants.constants import INFINITY


class Node:
    def __init__(self, label):
        self.sequence           = label.split()[0]
        self.label              = label[2:-1]
        self.has_been_visited   = False
        self.distances_to_nodes = {}
        self.ancestral          = None
        self.start_time         = INFINITY
        self.end_time          = INFINITY
    
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
    def get_distance_to_root(self):
        return self.distance_to_root
    def get_start_time(self):
        self.start_time
    def get_end_time(self):
        return self.end_time
    # ######### |get|
    def set_has_been_visited(self, b):
        self.has_been_visited = b
    def set_ancestral(self, ancestral):
        self.ancestral = ancestral
    def set_distance_to_node(self, node, distance):
        self.distances_to_nodes[node.get_sequence()] = distance
    def set_distance_to_root(self, distance):
        self.distance_to_root = distance
    def set_start_time(self,start_time):
        self.start_time = start_time
    
    def set_end_time(self,end_time):
        self.end_time = end_time



    def exist_key_in_map_distances(self, node):
        if node.get_sequence() in self.distances_to_nodes:
            return True
        return False