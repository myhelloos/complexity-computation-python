#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/22/21 1:02 AM
@desc:
"""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from utils import savefig, decorate


def reachable_nodes(G, start):
    seen = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))
    return seen


def is_connected(G):
    start = next(iter(G))
    reachable = reachable_nodes(G, start)
    return len(reachable) == len(G)


def all_pairs(nodes):
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i > j:
                yield u, v


def flip(p):
    return np.random.random() < p


def random_pairs(nodes, p):
    for edge in all_pairs(nodes):
        if flip(p):
            yield edge


def make_random_graph(n, p):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(random_pairs(nodes, p))
    return G


def prob_connected(n, p, iters=100):
    tf = [is_connected(make_random_graph(n, p)) for i in range(iters)]
    return np.mean(tf)


if __name__ == '__main__':
    n = 10
    pstar = np.log(n) / n
    ps = np.logspace(-1.3, 0, 11)
    print(ps)
    ys = [prob_connected(n, p, 1000) for p in ps]
    print(ys)

    plt.axvline(pstar, color='gray')
    plt.plot(ps, ys, color='green')
    decorate(
        xlabel='Prob of edge(p)',
        ylabel='Prob Connected',
        xscale='log'
    )
    savefig('../out/figs/chap02-5')
