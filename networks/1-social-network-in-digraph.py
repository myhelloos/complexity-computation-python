#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/20/21 11:26 PM
@desc:
"""
import matplotlib.pyplot as plt
import networkx as nx

from utils import savefig


def generate_social_network():
    G = nx.DiGraph()
    G.add_node('Alice')
    G.add_node('Bob')
    G.add_node('Chuck')
    print(list(G.nodes()))
    G.add_edge('Alice', 'Bob')
    G.add_edge('Alice', 'Chuck')
    G.add_edge('Bob', 'Alice')
    G.add_edge('Bob', 'Chuck')
    print(list(G.edges()))

    return G


def draw_graph(filename):
    nx.draw_circular(G, node_color='C0', node_size=2000, with_labels=True)
    plt.axis('equal')
    savefig(filename)


if __name__ == '__main__':
    G = generate_social_network()

    draw_graph('../out/figs/chap02-1')
