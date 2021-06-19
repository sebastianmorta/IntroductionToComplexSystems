import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ploter(name):
    # data = pd.DataFrame(pd.read_csv(r"data g1.csv", sep=',', header=None, engine='python'))
    #
    # y = data[2]
    # x = np.linspace(0, 5, len(y))
    # fig, ax = plt.subplots(figsize=(12, 6))
    # ax.plot(x, y, 'r-', label="State 1")
    # plt.ylabel(r"ilosc mutantow", size=16)
    # plt.xlabel("t", size=16)
    # plt.legend(prop={'size': 12})
    # plt.grid(1, 'major')
    # # plt.savefig("plt1.png")
    # plt.show()
    data = pd.DataFrame(pd.read_csv(r"dataw g1.csv", sep=',', header=None, engine='python'))
    data2 = pd.DataFrame(pd.read_csv(r"dataw g2.csv", sep=',', header=None, engine='python'))
    data3 = pd.DataFrame(pd.read_csv(r"dataw g3.csv", sep=',', header=None, engine='python'))
    y = data[3]
    x = np.linspace(0, 5, len(y))
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y, 'r--', label="State 1")
    plt.ylabel(r"ilosc mutantow", size=16)
    plt.xlabel("t", size=16)
    plt.legend(prop={'size': 12})
    plt.grid(1, 'major')
    # plt.savefig("plt1.png")
    # plt.show()



    y1 = data2[3]
    x = np.linspace(0, 5, len(y1))
    # fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y1, 'b--', label="VM")
    plt.ylabel(r"ilosc mutantow", size=16)
    plt.xlabel("t", size=16)
    plt.legend(prop={'size': 12})
    plt.grid(1, 'major')
    # plt.savefig("plt1.png")
    # plt.show()
    #
    # data3 = pd.DataFrame(pd.read_csv(r"data g3.csv", sep=',', header=None, engine='python'))
    #
    y2 = data3[3]
    x = np.linspace(0, 5, len(y2))
    # fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y2, 'g--', label="IP")
    plt.ylabel(r"ilosc mutantow", size=16)
    plt.xlabel("t", size=16)
    plt.legend(prop={'size': 12})
    plt.grid(1, 'major')
    # plt.savefig("plt1.png")
    plt.show()


ploter("data g1")
# ploter("data g2")
# ploter("data g3")
