import random
from random import randint


class Graph:
    def __init__(self, amount_of_nodes, list_of_edges):
        self.list_of_nodes = [Node(list_of_edges[i], i) for i in range(amount_of_nodes)]

    def assignEdgesToNodes(self):
        tmp_list = list.copy(self.list_of_nodes)
        for node in self.list_of_nodes:
            tmp_list.remove(node)
            for i in range(node.amount_of_edges):
                # node.assignEdges(random.choice(tmp_list))
                node.assignEdges(self.chooseConnection(tmp_list))
    def chooseConnection(self,list):

        return randint(0, len(self.list_of_nodes))

    def printer(self):
        for node in self.list_of_nodes:
            print("node number: ", node.number_of_node)
            print("amount of edges: ", node.amount_of_edges)
            for edge in node.edges:
                print("edge from: ", edge.edge_from, "edge to: ", edge.edge_to)
            print("===================================================================")


class Node:
    def __init__(self, amount_of_edges, node_number):
        self.number_of_node = node_number
        self.amount_of_edges = amount_of_edges
        self.edges = []

    def assignEdges(self, other):
        self.edges.append(Edge(self.number_of_node, other.number_of_node))


class Edge:
    def __init__(self, edge_from, edge_to):
        self.edge_from = edge_from
        self.edge_to = edge_to


def equality(a):
    edge_list = []
    l = int((a/10) ** (-a))
    tmp = [x * 0.1 + a/10 for x in range(0, l)]
    for i in tmp:
        edge_list.append(int(i ** (-a)) if i ** (-a) >= 1 else 1)
    return edge_list, len(edge_list)


# g = Graph(10, [7, 4, 3, 2, 2, 2, 1, 1, 1, 1])
# g.assignEdgesToNodes()
# g.printer()

a, b = equality(2.5)
print(a)
