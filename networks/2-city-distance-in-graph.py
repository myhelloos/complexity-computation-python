#!/usr/bin/env python
# encoding: utf-8
"""
@author: alfred
@license: (C) Copyright 2019-2021, Alfred Yuan Limited.
@time: 8/22/21 12:21 AM
@desc:
"""
import matplotlib.pyplot as plt
import networkx as nx

from utils import savefig


def generate_drive_city_graph(positions, drive_times):
    G = nx.Graph()
    G.add_nodes_from(positions)
    G.add_edges_from(drive_times)

    print(G.nodes)
    print(G.edges)

    return G


def draw_graph_with_label(filename, G, positions, drive_times):
    nx.draw(
        G, positions,
        node_color='C1',
        node_shape='s',
        node_size=2500,
        with_labels=True
    )
    nx.draw_networkx_edge_labels(G, positions, edge_labels=drive_times)
    plt.axis('equal')
    savefig(filename)


if __name__ == '__main__':
    positions = dict(
        Albany=(-74, 43),
        Boston=(-71, 42),
        NYC=(-74, 41),
        Philly=(-75, 40)
    )
    drive_times = {
        ('Albany', 'Boston'): 3,
        ('Albany', 'NYC'): 4,
        ('Boston', 'NYC'): 4,
        ('NYC', 'Philly'): 2
    }
    G = generate_drive_city_graph(positions, drive_times)
    draw_graph_with_label('../out/figs/chap02-2', G, positions, drive_times)
