import matplotlib.pyplot as plt
import os
import networkx as nx
import pandas as pd
import numpy as np

from networkx.algorithms.community import k_clique_communities
filename = "physicians.txt"
G = nx.DiGraph()
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head, tail)
pr = nx.pagerank(G, alpha=0.85)

layout = nx.spring_layout(G)
plt.figure(1)
nx.draw(G, pos=layout, node_color='y', node_size=30)
plt.show()
plt.figure(2)
nx.draw(G, pos=layout, node_size=[i * 6000 for i in pr.values()], node_color='g', with_labels=True)
plt.show()
