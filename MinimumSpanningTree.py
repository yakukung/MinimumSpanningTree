import networkx as nx
import matplotlib.pyplot as plt

# สร้างกราฟแบบมีทิศทาง
graph = {
    'A': {'B': 2, 'C': 6},
    'B': {'A': 2, 'C': 1, 'D': 5},
    'C': {'A': 6, 'B': 1, 'D': 4},
    'D': {'B': 5, 'C': 4}
}

# สร้างกราฟแบบไม่มีทิศทางด้วย NetworkX
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# ตรวจสอบว่ากราฟมี cycle หรือไม่
if nx.is_connected(G):
    print("กราฟไม่มี cycle")
else:
    print("กราฟมี cycle อยู่!")

# หา Minimum Spanning Tree (MST) สำหรับกราฟแบบไม่มีทิศทาง
mst = nx.minimum_spanning_tree(G)

# ตำแหน่งโหนดสำหรับวาดกราฟ
pos = nx.spring_layout(G)

# วาดกราฟ
plt.figure(figsize=(15, 7))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# วาดเส้นเชื่อมทั้งหมดในกราฟโดยไม่มีหัวลูกศร
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

# วาดเส้นเชื่อมของ MST โดยไม่มีหัวลูกศร
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แสดงน้ำหนักของ edges
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

# แสดงกราฟ
plt.title("Minimum Spanning Tree", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# แสดงผลลัพธ์ MST
print("เส้นทางใน Minimum Spanning Tree:")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")
