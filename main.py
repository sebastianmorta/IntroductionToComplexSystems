import csv
import random
from random import randint
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def removeDuplicates(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


class Graph:
    def __init__(self, amount_of_nodes, list_of_edges):
        self.nodes = [Node(list_of_edges[i], i) for i in range(amount_of_nodes)]
        self.edges = []

    def checkFree(self, data):
        result = []
        for node in data:
            if node.amount_of_edges - len(node.edges) > 0:
                result.append(node)
        return result

    def assignEdgesToNodes(self):
        iter = 1
        for node in self.nodes:
            tmp_list = self.checkFree(self.nodes[iter:])
            for i in range(node.amount_of_edges - len(node.edges)):
                if tmp_list:
                    rand = random.choice(tmp_list)
                    if rand.amount_of_edges - len(rand.edges):
                        self.chooseConnection(node, rand)
                    tmp_list.remove(rand)
            iter += 1

    #     def assignEdgesToNodes(self):
    #         iter = 1
    #         for node in self.nodes:
    #             tmp_list = self.nodes[iter:]
    #             tmp_list = self.checkFree(tmp_list)
    #             print("$$$$$$$$$$$$$$$$$$$$new$$$$$$$$$$$$$$$$$$$$$$$$")
    #             for i in range(node.amount_of_edges - len(node.edges)):
    #                 if tmp_list:
    #                     print("nodes  ", len(self.nodes))
    #                     print("tmp  ", len(tmp_list))
    #                     print("iter  ", iter)
    #                     print("tmplist", tmp_list)
    #                     rand = random.choice(tmp_list)
    #                     print("rand  ", rand.number_of_node)
    #                     print("-----------------------------")
    #                     if rand.amount_of_edges - len(rand.edges):
    #                         self.chooseConnection(node, rand)
    #                     tmp_list.remove(rand)
    #             iter += 1

    def chooseConnection(self, current_node, other_node):
        current_node.assignEdges(other_node)
        other_node.assignEdges(current_node)

    def printer(self):
        for node in self.nodes:
            print("node number: ", node.number_of_node)
            print("amount of edges: ", node.amount_of_edges)
            for edge in node.edges:
                print("edge from: ", edge.edge_from, "edge to: ", edge.edge_to)
                self.edges.append(edge)
            print("===================================================================")
        print(self.edges)
        print(len(self.edges))
        self.edges = removeDuplicates(self.edges)
        print(self.edges)
        print(len(self.edges))

    def saveToSCV(self):
        with open('innovators.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["SN", "from", "to", "color"])
            for i in range(len(self.edges)):
                writer.writerow([i, self.edges[i].edge_from, self.edges[i].edge_to])
        self.mutating()

    def check(self):
        return [node.amount_of_edges - len(node.edges) for node in self.nodes]

    def mutating(self):
        for node in self.nodes:
            if random.random() > 0.5:
                node.im_mutant = True


class Node:
    def __init__(self, amount_of_edges, node_number):
        self.number_of_node = node_number
        self.amount_of_edges = amount_of_edges
        self.edges = []
        self.im_mutant = False

    def assignEdges(self, other):
        self.edges.append(Edge(self.number_of_node, other.number_of_node))


class Edge:
    def __init__(self, edge_from, edge_to):
        self.edge_from = edge_from
        self.edge_to = edge_to

    def __eq__(self, other):
        return True if (self.edge_from == other.edge_from and self.edge_to == other.edge_to) or (
                self.edge_from == other.edge_to and self.edge_to == other.edge_from) else False


# def equality(a):
#     edge_list = []
#     l = int((a / 10) ** (-a)) + 10
#     tmp = [x * 0.1 + a / 10 for x in range(0, l)]
#     for i in tmp:
#         # edge_list.append(int(i ** (-a))+5)
#         edge_list.append(int(i ** (-a)) if i ** (-a) >= 1 else 1)
#     return len(edge_list), edge_list

def equality(a):
    l = int((a / 10) ** (-a)) + 10
    tmp = [x * 0.1 + a / 10 for x in range(0, l)]
    t = [x for x in tmp if x <= 1.01]
    edge_list = [int(t[i] ** (-a)) if t[i] ** (-a) >= 1 else 1 for i in range(len(t)) for _ in range(i*2)]
    return len(edge_list), edge_list


a, b = equality(2.5)
# g = Graph(10, [7, 4, 3, 2, 2, 2, 1, 1, 1, 1])
g = Graph(a, b)
g.assignEdgesToNodes()
g.printer()
print("sum", sum(b))
print("b", b)
print("len", len(b))
print(sum(g.check()))
# a, b = equality(2.5)
# print(a)
# g=[1,2,3,4,5,6,7,8,9]
# print(g[1:])
# df = pd.read_csv("book1.csv")
# print(df)
# df = df.loc[df['weight'] > 10, :]
# print(df)
# df1 = df[['Source', 'Target']]
# print(df1)
g.saveToSCV()

df = pd.read_csv("innovators.csv")
df1 = df[['from', 'to']]
color_map = []
G = nx.Graph()
G = nx.from_pandas_edgelist(df1, 'from', 'to')
for node in g.nodes:
    if node.im_mutant:
        color_map.append('red')
    else:
        color_map.append('green')
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()
