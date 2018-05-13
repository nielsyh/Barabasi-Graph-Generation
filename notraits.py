import collections
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import *
#import traits.api as trapi
#import traitsui.api as trui


def generateModelA(N, m):
    G = nx.Graph()
    # fill this graph according to model A
    # HINTS: look at the documentation of
    # NetworkX: https://networkx.github.io/documentation/stable/tutorial.html
    # Numpy (random): https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html

    for i in range(0, m):
        G.add_node(i)
        print('add node: ' + str(i))

    for i in range(0, m):
        for n in range(0, m):
            if(i == n):
                continue
            else:
                print('Edge: ' + str(i) + ', ' + str(n))
                G.add_edge(i,n)

    #construct N-m new nodes
    for r in range(0,N-m):
        current_size = len(G.nodes)
        new_node = r
        G.add_node(new_node)
        #link new node to m random nodes
        for i in range(0, m):
            random_node = randint(0,current_size)
            G.add_edge(new_node, random_node)

    nx.draw(G)
    print(str(G.graph))
    return G


def generateModelBA(N, m):
    G = nx.Graph()
    # fill this graph according to model A
    # HINTS: look at the documentation of
    # NetworkX: https://networkx.github.io/documentation/stable/tutorial.html
    # Numpy (random): https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html
    return G


def plotCompare(N, m, scale='log'):
    # generate a plot that compares the different functions
    # use N*m as max_degree
    # look at the plotFrequencies method below for inspiration
    fig, ax = plt.subplots()


def plotExercise():
    # to do the exercise, first adapt the generateModelBA method to allow it to restart
    pass  # do nothing; remove before editing further


# this function draws the frequencies of the degrees; don't modify
def plotFrequencies(deg, freq, max_degree, name='', scale='linear'):
    fig, ax = plt.subplots()
    ax.set_xscale(scale)
    ax.set_yscale(scale)
    plt.plot(deg, freq, 'o')

    plt.title("Degree Frequencies " + name)
    plt.ylabel("Freq.")
    plt.xlabel("k")
    ax.set_xticks(np.arange(0, max_degree + 10, step=10))
    ax.set_yticks(np.arange(0, 1.1, step=0.1))


# this function counts the frequencies of the degrees; don't modify
def frequencies(G):
    N = G.number_of_nodes()
    if N == 0:
        return [], [], 0
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degree_count = collections.Counter(degree_sequence)
    deg, cnt = zip(*degree_count.items())
    max_degree = max(deg)
    freq = map(lambda x: float(x) / N, cnt)
    return deg, freq, max_degree


# this function computes the approximation for model A; don't modify
def plotApproxModelA(N, m, max_degree):
    x = np.linspace(1.0, max_degree + 5)
    y = np.multiply(np.exp(1 - x / m), 1 / float(m))
    plt.plot(x, y)


# this function computes the approximation for model B-A; don't modify
def plotApproxModelBA(N, m, max_degree):
    x = np.linspace(float(m), max_degree + 10)
    y = np.multiply(2 * (m * 2), x * -3)
    plt.plot(x, y)


# this function computes the exact form of model B-A; don't modify
def plotApproxModelBA2(N, m, max_degree):
    x = np.linspace(m + 0.4, max_degree + 10)
    y = np.divide(2 * m * (m + 1), x * (x + 1) * (x + 2))
    plt.plot(x, y)


# this function plots models BA for N and m using a particular scale; don't modify
def plotNmBA(N, m, scale='linear'):
    # using model BA
    G = generateModelBA(N, m)
    (deg, freq, max_degree) = frequencies(G)
    plotFrequencies(deg, freq, max_degree, 'Model Barabasi-Albert (m=' + str(m) + ')', scale)
    plotApproxModelBA(N, m, max_degree)
    plotApproxModelBA2(N, m, max_degree)

# this function plots models BA for N and m using a particular scale; don't modify
def plotNmA(N, m, scale='linear'):
    # using model A
    G = generateModelA(N, m)
    (deg, freq, max_degree) = frequencies(G)
    plotFrequencies(deg, freq, max_degree, 'Model A (m=' + str(m) + ')', scale)
    plotApproxModelA(N, m, max_degree)


# don't modify this class or anything below it
# class Conf(trapi.HasTraits):
#     N = trapi.Int(100, label='N')
#     m = trapi.Int(5, label='m')
#     goA = trui.Action(name='Generate Model A', action='compModelA')
#     goBA = trui.Action(name='Generate Model B-A', action='compModelBA')
#     comp = trui.Action(name='Compare approximations', action='compApprox')
#     ex = trui.Action(name='Do exercise', action='doExercise')
#     scale = trapi.Enum('Linear', 'Log-log')
#
#     view = trui.View(
#         'N', 'm', 'scale',
#         buttons=[goA, goBA, comp, ex]
#     )
#
#     def getScale(self):
#         if self.scale == 'Log-log':
#             return 'log'
#         else:
#             return 'linear'
#
#     def doExercise(self, info):
#         plotExercise()
#         plt.show()
#         exit()
#
#     def compModelA(self, info):
#         plotNmA(self.N, self.m, self.getScale())
#         plt.show()
#         exit()
#
#     def compModelBA(self, info):
#         plotNmBA(self.N, self.m, self.getScale())
#         plt.show()
#         exit()
#
#     def compApprox(self, info):
#         plotCompare(self.N, self.m, self.getScale())
#         plt.show()
#         exit()
#
#     def display(self):
#         self.configure_traits()


#conf = Conf()
#conf.display()
#a = generateModelA(50,5)
plotNmBA(100,3)
plt.show()