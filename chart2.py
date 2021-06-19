from copy import deepcopy

from classes import Graph, Node, Edge
import numpy as np


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


def getAvg(list):
    return sum(list) / len(list)


def checkStability(g):
    count_mutatns = 1
    count_not_mutatns = 1
    for node in g.nodes:
        if node.is_mutant:
            count_mutatns += 1
        else:
            count_not_mutatns += 1
    return count_mutatns


def equality(a, N):
    values_base = np.linspace(1, 14, N)

    edge_list = [int(((v + 1.5) ** (-a)) * N) if int((v ** (-a)) * N) > 1 else 1 for v in values_base]

    return len(edge_list), edge_list


def setAllNotMutatn(g):
    for node in g.nodes:
        node.is_mutant = False


def initMutatnsChart2(g, level):
    for node in g.nodes:
        if level - 5 < node.amount_of_edges < level + 5:
            node.is_mutant = True
            break


a, b = equality(2.5, 1000)
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
# main.initMutatnsChart2(g1)
# main.initMutatnsChart2(g2)
# main.initMutatnsChart2(g3)
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

s_VM = [0.01, 0.02, 0.08]
s_IP = [0.004, 0.008, 0.016]
K = [1, 3, 7, 10, 30, 50, 70, 100, 170, 200]
#
# print("g1")
# drawGraph(g1)
# for i in range(10000):
#     data_for_g1 = np.append(data_for_g1, np.array([getAmoutnOfMutatns(g1)]), axis=0)
#     for j in range(1000):
#         g1.linkBiasedDynamiks(0.4, j)
# saveToCSV(data_for_g1, "datachart2 g1")
# drawGraph(g1)
models, s, k, stab = 2, 3, 18, 1000

matrix_for_probability = np.zeros((3, int(len(K))+1))
print("g2")

for sv_idx, sv in enumerate(s_VM):
    for idx_k, k in enumerate(K):
        setAllNotMutatn(g2)  # ustawienie wszystkich na niemutanty
        initMutatnsChart2(g2, k)  # inicjalizacja pierwszego mutanta
        mut_amount = checkStability(g2)  # przypisanie aktualnej liczby mutantów

        list_of_changes = []  # lista zawierająca zmiany
        ilosc_prob_i_stabilizacja = 0
        setAllNotMutatn(g2)
        for t in range(1000):  # ilość iteracji dla jednego stopnia
            if t==0:
                for st in range(11000):
                    # list_of_changes.append(checkStability(g2))  # dodajemy aktualną liczbę mutantów
                    g2.voterModel(sv)  # mutujemy
            for st in range(1100):
                list_of_changes.append(checkStability(g2))  # dodajemy aktualną liczbę mutantów
                g2.voterModel(sv)  # mutujemy
            if getAvg(list_of_changes[(len(list_of_changes) - 1000):]) > (mut_amount + 1) or getAvg(
                    list_of_changes[
                    (len(list_of_changes) - 1000):]) < mut_amount - 1:  # sprawdzamy czy liczba mutków sie zmieniła
                mut_amount = checkStability(g2)  # aktualizujemy liczbe mutantów
                print(mut_amount)
                print("dupa")
            else:
                print("lipa")
                ilosc_prob_i_stabilizacja += 1
                break
        matrix_for_probability[sv_idx, idx_k] = ilosc_prob_i_stabilizacja/1000

print(matrix_for_probability)


# liczba_stabilnych = []
# for sv in s_VM:
#     list_of_changes = []
#     ilosc_prob_i_stabilizacja = 0
#     # main.drawGraph(g2)
#     for _ in range(1000):
#         setAllNotMutatn(g2)
#         main.initMutatnsChart2(g2)
#         mut_amount = checkStability(g2)
#         for i in range(1000):
#             for j in range(100):
#                 # data_for_g2 = np.append(data_for_g2, np.array([getAmoutnOfMutatns(g2)]), axis=0)
#                 list_of_changes.append(checkStability(g2))
#                 g2.voterModel(sv, j)
#             if getAvg(list_of_changes[(len(list_of_changes) - 10):]) > mut_amount + 1 or getAvg(
#                     list_of_changes[(len(list_of_changes) - 10):]) < mut_amount - 1:
#                 mut_amount = checkStability(g2)
#             else:
#                 ilosc_prob_i_stabilizacja += 1
#                 break
#     liczba_stabilnych.append(ilosc_prob_i_stabilizacja / 1000)

# main.saveToCSV(data_for_g2, "datachart2 g2")
# main.drawGraph(g2)
# print("g3")
# drawGraph(g3)
# for i in range(100000):
#     data_for_g3 = np.append(data_for_g3, np.array([getAmoutnOfMutatns(g3)]), axis=0)
#     for j in range(1000):
#         g3.invasionModel(0.004)
# saveToCSV(data_for_g3, "datachart2 g3")
# drawGraph(g3)
