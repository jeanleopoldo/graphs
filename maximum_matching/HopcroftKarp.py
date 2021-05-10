from constants.constants import INFINITY
from model.node import Node


class HopcroftKarp:
    def __init__(self, graph):
        self.graph               = graph
        self.maximum_matching    = []
        self.left                = {}
        self.right               = {}
        self.dist                = {}
        self.number_of_matchings = 0
        self.init_structures()

    def init_structures(self):
        edges = self.graph.get_edges()
        for edge in edges:
            self.left[edge.get_start()] = None
            self.right[edge.get_end()]  = None
            self.dist[edge.get_start()] = INFINITY
            self.dist[edge.get_end()]   = INFINITY
        self.left[None]  = None
        self.right[None] = None
        self.dist[None]  = 0


    def find(self):
        while self.bfs():
            matchings = []
            for node in self.left:
                if self.left[node] == None and self.dfs(node, matchings):
                    self.number_of_matchings = self.number_of_matchings+1

        print("Maximum matchings ->", len(self.maximum_matching))
        for edge in self.maximum_matching:
            print("x:{}-y:{}".format(edge.get_start(), edge.get_end()))

    
    def bfs(self):
        queue = []
        for node in self.left:
            if self.left[node] == None:
                self.dist[node] = 0
                queue.append(node)
            else:
                self.dist[node] = INFINITY

        self.dist[None] = INFINITY
        while not len(queue) == 0:
            node = queue.pop(0)
            if self.dist[node] < self.dist[None]:
                node_obj = self.graph.get_node_by_sequence(node)
                edges = self.graph.get_node_edges(node_obj)
                for edge in edges:
                    mate = self.right[edge.get_end()]
                    distance = self.dist[mate]
                    if distance == INFINITY:
                        self.dist[mate] = self.dist[edge.get_start()]+1
                        queue.append(edge.get_end())
        
        finished = self.dist[None] is not INFINITY
        return finished


    def dfs(self, key, matchings):
        if key is not None:
            node  = self.graph.get_node_by_sequence(key)
            edges = self.graph.get_node_edges(node) 
            for edge in edges:
                mate_y = self.right[edge.get_end()]
                if self.dist[mate_y] == self.dist[edge.get_start()]+1:
                    if self.dfs(mate_y, matchings) == True:                        
                        self.left[edge.get_start()] = edge.get_end()
                        self.right[edge.get_end()]  = edge.get_start()
                        self.maximum_matching.append(edge)
                        return True

            self.dist[key] = INFINITY
            return False
        return True