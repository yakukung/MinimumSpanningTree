import networkx as nx
import matplotlib.pyplot as plt

def create_custom_graph():
    G = nx.Graph()
    edges = [
        ('A', 'B', 5), ('A', 'C', 10),
        ('B', 'C', 4), ('B', 'D', 8),
        ('C', 'D', 1), ('C', 'E', 2),
        ('D', 'E', 3)
    ]
    G.add_weighted_edges_from(edges)
    return G

def dfs_spanning_tree(G, start):
    visited = set()
    spanning_tree = []

    def dfs(node):
        visited.add(node)
        for neighbor in G[node]:
            if neighbor not in visited:
                spanning_tree.append((node, neighbor))
                dfs(neighbor)

    dfs(start)
    return spanning_tree

def draw_graph_and_spanning_tree(G, spanning_tree):
    pos = {
        'A': (0, 0), 'B': (1, 1), 'C': (1, -1),
        'D': (2, 1), 'E': (2, -1)
    }
    
    plt.figure(figsize=(12, 8))
    
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                           node_size=3000, alpha=0.8)
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)
    
    nx.draw_networkx_edges(G, pos, edgelist=spanning_tree, edge_color='r', width=2)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)
    
    plt.title("Custom Graph and DFS Spanning Tree", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

G = create_custom_graph()
spanning_tree = dfs_spanning_tree(G, 'A')
print("DFS Spanning Tree edges:")
print(spanning_tree)

draw_graph_and_spanning_tree(G, spanning_tree)

total_weight = sum(G[u][v]['weight'] for u, v in spanning_tree)
print(f"น้ำหนักรวมของ DFS Spanning Tree: {total_weight}")