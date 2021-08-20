#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/20/21 11:26 PM
@desc:
"""
import networkx as nx
import matplotlib.pyplot as plt
from utils import savefig

if __name__ == '__main__':
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

    nx.draw_circular(G, node_color='C0', node_size=2000, with_labels=True)
    plt.axis('equal')
    savefig('../out/figs/chap02-1')
