import matplotlib.pyplot as plt 
import networkx as nx

# Criando um grafo
G = nx.Graph()

# Adicionando nós com rótulos
nodes = ["ES", "MG", "RJ", "SP"]
for node in nodes:
    G.add_node(node, label=node)

# Adicionando arestas com rótulos
edges = [
    ("ES", "MG", "524"),
    ("ES", "RJ", "521"),
    ("ES", "SP", "882"),
    ("MG", "RJ", "434"),
    ("MG", "SP", "586"),
    ("RJ", "SP", "429")
]

for source, target, label in edges:
    G.add_edge(source, target, label=label)

# Definindo o layout dos nós
pos = nx.shell_layout(G) # Layout pré-definido 'shell'

# Desenhando os nós
nx.draw_networkx_nodes(G, pos, node_color='#00A0FF', node_size=500, alpha=1.0)

# Desenhando as arestas
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.6)

# Colocando os rótulos nos nós
nx.draw_networkx_labels(G, pos, font_size=10)

# Colocando os rótulos nas arestas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.axis('off')
plt.show()