import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()    #O método Graph cria um grafo não-orientado
G.add_nodes_from([1,2,3,4]) #Definição dos nós
G.add_edges_from([(1,2),(1,3),(2,4),(3,4),(2,3)])   #Definição das arestas
nx.draw_random(G)   #Desenha os nós em posições aleatórias
plt.show()
