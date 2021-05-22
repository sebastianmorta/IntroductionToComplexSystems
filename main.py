from random import randint


class Graph:
    def __init__(self, amount_of_nodes, list_of_edges):
        self.list_of_nodes = [Node(list_of_edges[i], i) for i in range(amount_of_nodes)]

    def assignEdgesToNodes(self):
        tmp_list = list.copy(self.list_of_nodes)
        for node in self.list_of_nodes:
            for i in range(node.amount_of_edges):
                node.assignEdges(self.chooseConnection())

    def chooseConnection(self):
        return randint(0, len(self.list_of_nodes))


class Node:
    def __init__(self, amount_of_edges, node_number):
        self.number_of_node = node_number
        self.amount_of_edges = amount_of_edges
        self.edges = []

    def assignEdges(self, other):
        self.edges.append(Edge(self, other))


class Edge:
    def __init__(self, edge_from, edge_to):
        self.edge_from = edge_from
        self.edge_to = edge_to
