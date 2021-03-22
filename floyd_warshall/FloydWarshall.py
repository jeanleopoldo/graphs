
class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        

    def search(self):
        for k in self.graph.get_nodes():
            for i in self.graph.get_nodes():
                for j in self.graph.get_nodes():
                    distance_ij = self.graph.get_distances_between_nodes(i,j)
                    distance_ik = self.graph.get_distances_between_nodes(i,k)
                    distance_kj = self.graph.get_distances_between_nodes(k,j)
                    
                    shortest_route = distance_ij > distance_ik + distance_kj
                    if shortest_route:
                        updated_distance = distance_ik + distance_kj
                        self.graph.set_distances_between_nodes(i,j, updated_distance)
                        
        print("a")