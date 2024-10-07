import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 4, 'D': 8},
    'C': {'A': 10, 'B': 4, 'D': 1, 'E': 2},
    'D': {'B': 8, 'C': 1, 'E': 3},
    'E': {'D': 3, 'C': 2},
}

# สร้างกราฟแบบไม่มีทิศทางด้วย NetworkX
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# ใช้อัลกอริธึม Kruskal เพื่อหา Minimum Spanning Tree (MST)
# 1. เรียงลำดับเส้นทางตามน้ำหนักจากน้อยไปมาก
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# 2. สร้างโครงสร้างเก็บ MST
mst = nx.Graph()

def bfs(start, goal, graph):
    # ตรวจสอบว่าโหนดต้นทางและโหนดปลายทางมีอยู่ในกราฟหรือไม่
    if start not in graph or goal not in graph:
        return False
    
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        if node == goal:  # นำโหนดแรกออกจากคิว
            return True
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

# 4. เพิ่มเส้นทางเข้า MST ทีละเส้นถ้าไม่ก่อให้เกิด cycle
for u, v, data in sorted_edges:
    if not bfs(u, v, mst):
        mst.add_edge(u, v, weight=data['weight'])

# กำหนดตำแหน่งโหนดแบบคงที่
pos = {
    'A': (0, 0), 'B': (2, 1), 'C': (2, -1),
    'D': (4, 2), 'E': (4, 0),
}

# วาดกราฟ
plt.figure(figsize=(15, 8))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# วาดเส้นเชื่อมทั้งหมดในกราฟ
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

# วาดเส้นเชื่อมของ MST
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แสดงน้ำหนักของ edges
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

# แสดงกราฟ
plt.title("Minimum Spanning Tree (Kruskal's Algorithm with BFS)", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# แสดงผลลัพธ์ MST
print("เส้นทางใน Minimum Spanning Tree (Kruskal):")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")

# คำนวณน้ำหนักรวมของเส้นเชื่อมใน MST
total_weight = sum(data['weight'] for u, v, data in mst.edges(data=True))
print(f"น้ำหนักรวมทั้งหมด: {total_weight}")
