import csv
import random
from copy import deepcopy
from random import randint, choice, random
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from classes import Graph, Node, Edge


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


def initMutatnsChart2(g, level):
    for node in g.nodes:
        if node.amount_of_edges == level:
            node.is_mutant = True
            break


def drawGraph(g):
    df = pd.read_csv("innovators.csv")
    df1 = df[['from', 'to']]
    color_map = []
    count_mutatns = 1
    count_not_mutatns = 1
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
        writer.writerows(data)


def getAmoutnOfMutatns(g):
    count_mutatns = 1
    count_not_mutatns = 1
    for node in g.nodes:
        if node.is_mutant:
            count_mutatns += 1
        else:
            count_not_mutatns += 1
    return [count_mutatns, count_not_mutatns, count_mutatns / (count_mutatns + count_not_mutatns),
            count_not_mutatns / (count_mutatns + count_not_mutatns), count_mutatns / count_not_mutatns]


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


data_for_g1 = np.empty((0, 5), int)
data_for_g2 = np.empty((0, 5), int)
data_for_g3 = np.empty((0, 5), int)
#
# print("g1")
# drawGraph(g1)
# for i in range(10000):
#     data_for_g1 = np.append(data_for_g1, np.array([getAmoutnOfMutatns(g1)]), axis=0)
#     for j in range(1000):
#         g1.linkBiasedDynamiks(0.4, j)
# saveToCSV(data_for_g1, "dataw g1")
# drawGraph(g1)
# print("g2")
# drawGraph(g2)
# for i in range(10000):
#     data_for_g2 = np.append(data_for_g2, np.array([getAmoutnOfMutatns(g2)]), axis=0)
#     for j in range(100):
#         g2.voterModel(0.0009, j)
# saveToCSV(data_for_g2, "dataw g2")
# drawGraph(g2)
print("g3")
drawGraph(g3)
for i in range(10000):
    data_for_g3 = np.append(data_for_g3, np.array([getAmoutnOfMutatns(g3)]), axis=0)
    for j in range(1000):
        g3.invasionModel(0.5)
saveToCSV(data_for_g3, "dataww g3")
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


