import networkx as nx
import matplotlib.pyplot as plt
import math

# 10000个节点 任意两个不同的节点之间的连边概率是p
ER = nx.random_graphs.erdos_renyi_graph(1000, 0.03)
degree = nx.degree_histogram(ER)
print(degree)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
k = range(30)

pk = [(15**i) * (math.exp(-15)) / math.factorial(i) for i in k]

plt.plot(k, pk, color="red", linewidth=0.6)
plt.scatter(x, y, color="blue", alpha=0.4, s=25)
plt.xlabel('k')
plt.ylabel('p(k)')
plt.xlim(0, 35)
plt.ylim(0, 0.12)
plt.show()