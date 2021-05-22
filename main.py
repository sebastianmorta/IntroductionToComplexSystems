class Graph:
    def __init__(self, amount_of_nodes, list_of_edges):
        self.list_of_nodes = [Node(list_of_edges[i], i) for i in range(amount_of_nodes)]


class Node:
    def __init__(self, amount_of_edges, node_number):
        self.number_of_node = node_number
        self.amount_of_edges = amount_of_edges


class Edge:
    def __init__(self, edge_from, edge_to):
        self.edge_from = edge_from
        self.edge_to = edge_to
