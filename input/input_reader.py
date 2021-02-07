

def read_raw_input(file_name):
    graph    = []
    nodes    = []
    edges    = []
    is_nodes = False
    is_edges = False
    file = open(file_name, "r")
    for line in file.readlines():
        if line is '\n':
            continue
        if "*vertices" in line:
            is_nodes = True
            is_edges = False
            continue
        if "*edges" in line:
            is_nodes = False
            is_edges = True
            continue
        
        if is_nodes is True:
            line = line.replace('\n', '')
            nodes.append(line)
        elif is_edges is True:
            line = line.replace('\n', '')
            aux  = line.split()
            edge = []
            edge.append(aux[0])
            edge.append(aux[1])
            edge.append(aux[2])
            edges.append(edge)
    graph.append(nodes)
    graph.append(edges)
    file.close()
    return graph