from core.graph import graph
from input.input_reader import read_raw_input
import sys

if __name__ == '__main__':
    file_name = sys.argv[1]
    graph_representation = read_raw_input(file_name)
    nodes = graph_representation[0]
    edges = graph_representation[1]