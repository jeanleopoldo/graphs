
class Edge:
    def __init__(self, start, end, weight):
        self.start  = start
        self.end    = end
        self.weight = weight

    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_weight(self):
        return self.weight