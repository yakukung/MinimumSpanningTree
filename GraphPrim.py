import networkx as nx
import matplotlib.pyplot as plt

# สร้างกราฟจากข้อมูลที่กำหนด
graph = {
    'A': {'B': 5, 'C': 10},  
    'B': {'A': 5, 'C': 3, 'D': 8}, 
    'C': {'A': 10, 'B': 3, 'D': 2, 'F': 12},  
    'D': {'B': 8, 'C': 2, 'E': 4}, 
    'E': {'D': 4, 'F': 6}, 
    'F': {'C': 12, 'E': 6},  
}

# สร้างกราฟแบบไม่มีทิศทาง
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# กำหนดตำแหน่งของโหนดในกราฟแบบคงที่ตามภาพใหม่
pos = {
    'A': (0, 0),
    'B': (0, 2),
    'C': (2, 0),
    'D': (2, 2),
    'E': (4, 2),
    'F': (4, 0)
}

# วาดกราฟ
plt.figure(figsize=(15, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=16, font_weight='bold', edge_color='gray')

# วาดน้ำหนักของเส้นเชื่อม
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)

plt.title("Undirected Graph with Updated Fixed Node Positions", fontsize=16)
plt.axis('off')  # ปิดการแสดงแกน
plt.tight_layout()
plt.show()