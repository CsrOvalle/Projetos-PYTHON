import matplotlib.pyplot as plt
import networkx as nx
G=nx.read_adjlist("adj.txt", create_using=nx.DiGraph())
pos=nx.shell_layout(G) # layout pré-definido
# nós
nx.draw_networkx_nodes(G,pos,
 node_color='#FF9090',
 node_size=500,
 alpha=0.8)
# arestas
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
# colocando rótulos
labels=nx.draw_networkx_labels(G,pos,font_size=14)
plt.axis('off')
plt.show() # display