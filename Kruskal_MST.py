import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': {'B': 5, 'C': 10},  
    'B': {'A': 5, 'C': 4, 'D': 8}, 
    'C': {'A': 10, 'B': 4, 'D': 1, 'E':2},  
    'D': {'B': 8, 'C': 1, 'E': 3}, 
    'E': {'D': 3, 'C':2}, 
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

# 3. ใช้ union-find เพื่อตรวจสอบ cycle
# สร้าง dictionary เพื่อเก็บ parent ของแต่ละ node
uf = {node: node for node in G.nodes()}

# ฟังก์ชันสำหรับค้นหา root ของ node
def find(node):
    # ตรวจสอบว่า node มี parent ที่ไม่ใช่ตัวมันเองหรือไม่
    if uf[node] != node:
        # ถ้ามีให้เรียก find ซ้ำเพื่อค้นหา root ที่แท้จริง
        uf[node] = find(uf[node])  # Path compression เพื่อทำให้การค้นหาเร็วขึ้น
    # คืนค่า root ของ node
    return uf[node]

# ฟังก์ชันสำหรับรวมสอง set ที่มี node1 และ node2 อยู่
def union(node1, node2):
    # ค้นหา root ของ node1
    root1 = find(node1)
    # ค้นหา root ของ node2
    root2 = find(node2)
    # ถ้า root ของทั้งสองแตกต่างกัน หมายความว่าอยู่ในกลุ่มที่ต่างกัน
    if root1 != root2:
        # รวมสอง set โดยให้ root ของ node1 ชี้ไปที่ root ของ node2
        uf[root1] = root2  # ทำให้ node1 เป็นลูกของ node2


# 4. เพิ่มเส้นทางเข้า MST ทีละเส้นถ้าไม่ก่อให้เกิด cycle
for u, v, data in sorted_edges:
    if find(u) != find(v):
        mst.add_edge(u, v, weight=data['weight'])
        union(u, v)


# กำหนดตำแหน่งโหนดแบบคงที่
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
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# วาดเส้นเชื่อมทั้งหมดในกราฟ
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

# วาดเส้นเชื่อมของ MST
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แสดงน้ำหนักของ edges
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

# แสดงกราฟ
plt.title("Minimum Spanning Tree (Kruskal's Algorithm)", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# แสดงผลลัพธ์ MST
print("เส้นทางใน Minimum Spanning Tree (Kruskal):")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")
