#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/22/21 12:54 AM
@desc:
"""
import networkx as nx

from utils import savefig


def all_pairs(nodes):
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i > j:
                yield u, v


def make_complete_graph(n):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(all_pairs(nodes))
    return G


if __name__ == '__main__':
    complete_graph = make_complete_graph(10)
    nx.draw_circular(
        complete_graph,
        node_color='C2',
        node_size=1000,
        with_labels=True
    )
    savefig('../out/figs/chap02-3')
