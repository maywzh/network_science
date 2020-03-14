import networkx as nx
import matplotlib.pyplot as plt
import math

ER = nx.random_graphs.erdos_renyi_graph(100, 0.03)
pos = nx.spring_layout(ER)
nx.draw(ER, pos, with_labels=False, node_size=30)
plt.show()