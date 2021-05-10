import math
class LawlerColouringGraphAlgorithm:
    def __init__(self, graph):
        self.graph = graph
    
    def colour(self):
        power_set = self.power_set()
        X = self.index_values(power_set)

        print("not implemented yet")
    
    def index_values(self, set):
        index_values = []

        for i in range(len(set)):

            indexed_values = self.set_to_zero(len(self.graph.get_nodes()))
            for j in set[i]:
                to_int = int(j)
                indexed_values[to_int] = 1
            index_values.append(indexed_values)
        return index_values
        
    def set_to_zero(self,size):
        array = []
        for i in range(size):
            array.append(0)
        return array
    def power_set(self):
        nodes = self.graph.get_nodes()
        pow_set_size = (int) (math.pow(2, len(nodes)))
        counter = 0
        j = 0
        power_set = []

        for counter in range(0, pow_set_size):
            partition = []
            for j in range(0, len(nodes)):
                if((counter & (1 << j)) > 0):
                    partition.append(nodes[j].get_sequence())
            power_set.append(partition)
        return power_set
    def find_independend_set(self):
        independent_sets = []

        nodes  = self.graph.get_nodes()
        for node in nodes:
            node_edges = self.graph.get_node_edges(node)
            

