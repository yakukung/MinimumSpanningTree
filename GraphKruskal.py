import networkx as nx
import matplotlib.pyplot as plt

# สร้างกราฟจากข้อมูลที่กำหนด
graph = {
    'A': {'B': 5, 'C': 10},  
    'B': {'A': 5, 'C': 4, 'D': 8}, 
    'C': {'A': 10, 'B': 4, 'D': 1, 'E':2},  
    'D': {'B': 8, 'C': 1, 'E': 3}, 
    'E': {'D': 3, 'C':2}, 
}

# สร้างกราฟแบบไม่มีทิศทาง
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# กำหนดตำแหน่งของโหนดในกราฟแบบคงที่ตามภาพใหม่
pos = {
    'A': (0, 0),
    'B': (2, 1),
    'C': (2, -1),
    'D': (4, 2),
    'E': (4, 0),
    'F': (4, -2)
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