import csv
import random
from copy import deepcopy
from random import randint, choice, random
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
        self.average_amount_of_edges = int(sum(list_of_edges) / len(list_of_edges))

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
                    rand = choice(tmp_list)
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

    # def printer(self):
    #     for node in self.nodes:
    #         print("node number: ", node.number_of_node)
    #         print("amount of edges: ", node.amount_of_edges)
    #         for edge in node.edges:
    #             print("edge from: ", edge.edge_from, "edge to: ", edge.edge_to)
    #             self.edges.append(edge)
    #         print("===================================================================")
    #     print("edges", self.edges)
    #     print("len edges", len(self.edges))
    #     self.edges = removeDuplicates(self.edges)
    #     print("edges after rmv", self.edges)
    #     print(" len edges after rmv", len(self.edges))
    #     self.mutating()
    #
    # def saveToCSV(self):
    #     with open("results.csv", 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["SN", "from", ])
    #         e_data = np.array([[i for i in range(len(self.edges))],
    #                            [self.edges[i].edge_to for i in range(len(self.edges))],
    #                            [self.edges[i].edge_from for i in range(len(self.edges))]]).T
    #         writer.writerows(e_data)

    def check(self):
        return [node.amount_of_edges - len(node.edges) for node in self.nodes]

    def mutating(self):
        for node in self.nodes:
            if random() > 0.8:
                node.is_mutant = True

    def linkBiasedDynamiks(self, s, n):
        mother = choice(self.nodes[:(10*n)])

        father = self.nodes[choice(mother.edges).edge_to]
        if mother.is_mutant != father.is_mutant:
            if mother.is_mutant:
                father.is_mutant = True
            else:
                if random() < s:
                    father.is_mutant = False

            # print(mother.number_of_node, father.number_of_node)

    def voterModel(self, s,n):
        mother = choice(self.nodes[:(10*n)])
        father = self.nodes[choice(mother.edges).edge_to]
        if mother.is_mutant != father.is_mutant:
            if father.is_mutant:
                mother.is_mutant = True
            else:
                if random() < (1 - s):
                    mother.is_mutant = False

            # if father.is_mutant:
            #     father.is_mutant = True
            # else:
            #     if random() < s:
            #         father.is_mutant = False

    def invasionModel(self, s):
        mother = choice(self.nodes[:1500])
        father = self.nodes[choice(mother.edges).edge_to]
        if mother.is_mutant != father.is_mutant:
            if mother.is_mutant:
                father.is_mutant = True
            else:
                if random() < s:
                    father.is_mutant = False


class Node:
    def __init__(self, amount_of_edges, node_number):
        self.number_of_node = node_number
        self.amount_of_edges = amount_of_edges
        self.edges = []
        self.is_mutant = False

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

# def equality(a):
#     l = int((a / 10) ** (-a)) + 10
#     tmp = [x * 0.1 + a / 10 for x in range(0, l)]
#     t = [x for x in tmp if x <= 1.01]
#     edge_list = [int(t[i] ** (-a)) if t[i] ** (-a) >= 1 else 1 for i in range(len(t)) for _ in range(i * 2)]
#     return len(edge_list), edge_list
def equality(a, N):
    values_base = np.linspace(1, 40, N)
    # print("valvas", values_base)
    edge_list = [int((v ** (-a)) * N) if int((v ** (-a)) * N) > 1 else 1 for v in values_base]

    # l = int((a / 10) ** (-a)) + 10
    # tmp = [x * 0.1 + a / 10 for x in range(0, l)]
    # t = [x for x in tmp if x <= 1.01]
    # edge_list = [int(t[i] ** (-a)) if t[i] ** (-a) >= 1 else 1 for i in range(len(t)) for _ in range(i * 280)]
    return len(edge_list), edge_list


def initMutatnsChart1(g):
    for node in g.nodes:
        if node.amount_of_edges > g.average_amount_of_edges:
            node.is_mutant = True


def drawGraph(g):
    df = pd.read_csv("innovators.csv")
    df1 = df[['from', 'to']]
    color_map = []
    count_mutatns = 0
    count_not_mutatns = 0
    # G = nx.Graph()
    # G = nx.from_pandas_edgelist(df1, 'from', 'to')
    for node in g.nodes:
        if node.is_mutant:
            color_map.append('red')
            count_mutatns += 1
        else:
            color_map.append('green')
            count_not_mutatns += 1
    # nx.draw(G, node_color=color_map, with_labels=True)
    # plt.show()
    print("color", color_map)
    print("mutants amount", count_mutatns, "---", count_mutatns / (count_not_mutatns + count_mutatns) * 100, "%")
    print("not mutants amount", count_not_mutatns, "---", count_not_mutatns / (count_not_mutatns + count_mutatns) * 100,
          "%")


def saveToCSV(data, name):
    with open(name + ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["mutants", "notmutants", ])

        writer.writerows(data)


def getAmoutnOfMutatns(g):
    count_mutatns = 0
    count_not_mutatns = 0
    for node in g.nodes:
        if node.is_mutant:
            count_mutatns += 1
        else:
            count_not_mutatns += 1
    return [count_mutatns, count_not_mutatns, count_mutatns / (count_mutatns + count_not_mutatns), count_mutatns/count_not_mutatns]


a, b = equality(2.5, 10000)
# g = Graph(10, [7, 4, 3, 2, 2, 2, 1, 1, 1, 1])
g1 = Graph(a, b)

print("avg ", g1.average_amount_of_edges)
g1.assignEdgesToNodes()
g2 = deepcopy(g1)
g3 = deepcopy(g1)
# g.printer()
# g.saveToCSV()
print("sum", sum(b))
print("b", b)
print("len", len(b))
print(sum(g1.check()))
initMutatnsChart1(g1)
initMutatnsChart1(g2)
initMutatnsChart1(g3)
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


data_for_g1 = np.empty((0, 3), int)
data_for_g2 = np.empty((0, 3), int)
data_for_g3 = np.empty((0, 3), int)

print("g1")
drawGraph(g1)
for i in range(10000):
    data_for_g1 = np.append(data_for_g1, np.array([getAmoutnOfMutatns(g1)]), axis=0)
    for j in range(1000):
        g1.linkBiasedDynamiks(0.4)
saveToCSV(data_for_g1, "data g1")
drawGraph(g1)
print("g2")
drawGraph(g2)
for i in range(10000):
    data_for_g2 = np.append(data_for_g2, np.array([getAmoutnOfMutatns(g2)]), axis=0)
    for j in range(1000):
        g2.voterModel(0.4)
saveToCSV(data_for_g2, "data g2")
drawGraph(g2)
print("g3")
drawGraph(g3)
for i in range(10000):
    data_for_g3 = np.append(data_for_g3, np.array([getAmoutnOfMutatns(g3)]), axis=0)
    for j in range(1000):
        g3.invasionModel(0.4)
saveToCSV(data_for_g3, "data g3")
drawGraph(g3)


def ploter(name):
    data = pd.DataFrame(
        pd.read_csv(name + r".csv", sep=',', skiprows=1, engine='python'))

    y = data[2]
    x = np.linspace(0, 5, len(y))
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y, 'r-', label="State 1")
    plt.ylabel(r"ilosc mutantow", size=16)
    plt.xlabel("t", size=16)
    plt.legend(prop={'size': 12})
    plt.grid(1, 'major')
    # plt.savefig("plt1.png")
    plt.show()
