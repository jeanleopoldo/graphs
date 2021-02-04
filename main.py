from core.graph import graph
from input.input_reader import read_raw_input
import sys

if __name__ == '__main__':
    g = graph()
    g.func()
    file_name = sys.argv[1]
    read_raw_input(file_name)