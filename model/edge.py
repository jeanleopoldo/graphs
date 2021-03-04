
class Edge:
    def __init__(self, start, end, weight):
        self.start  = start
        self.end    = end
        self.weight = weight
        self.visited = False

    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_weight(self):
        return float(self.weight)
    def get_has_been_visited(self):
        return self.visited
    def set_has_been_visited(self, visited):
        self.visited = visited
    def print_start_and_end(self):
        print("start:", self.start)
        print("end:", self.end)