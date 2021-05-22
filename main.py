class Graph:
    def __init__(self):
        self.list_of_nodes = []


class Node:
    def __init__(self, amount_of_edges):
        self.amount_of_edges = amount_of_edges


class Edge:
    def __init__(self, edge_from, edge_to):
        self.edge_from = edge_from
        self.edge_to = edge_to
