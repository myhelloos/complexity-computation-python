#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/22/21 1:02 AM
@desc:
"""
import networkx as nx
import numpy as np

from utils import savefig


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


if __name__ == '__main__':
    random_graph = make_random_graph(10, 0.3)
    nx.draw_circular(random_graph,
                     node_color='C3',
                     node_size=1000,
                     with_labels=True)
    savefig('../out/figs/chap02-4')
    print(is_connected(random_graph))
