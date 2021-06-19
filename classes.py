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
        # print(n+1)
        mother = choice(self.nodes[:7000])

        father = self.nodes[choice(mother.edges).edge_to]
        if mother.is_mutant != father.is_mutant:
            if mother.is_mutant:
                father.is_mutant = True
            else:
                if random() < s:
                    father.is_mutant = False

            # print(mother.number_of_node, father.number_of_node)

    def voterModel(self, s):
        mother = choice(self.nodes)
        father = self.nodes[choice(mother.edges).edge_to]
        if mother.is_mutant != father.is_mutant:
            if father.is_mutant:
                mother.is_mutant = True
            else:
                if random() < (1-s):
                    mother.is_mutant = False

            # if father.is_mutant:
            #     father.is_mutant = True
            # else:
            #     if random() < s:
            #         father.is_mutant = False

    def invasionModel(self, s):
        mother = choice(self.nodes[:7500])
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
