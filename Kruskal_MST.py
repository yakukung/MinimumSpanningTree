import networkx as nx
import matplotlib.pyplot as plt
from heapq import heapify, heappop

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 4, 'D': 8},
    'C': {'A': 10, 'B': 4, 'D': 1, 'E': 2},
    'D': {'B': 8, 'C': 1, 'E': 3},
    'E': {'D': 3, 'C': 2},
}
def kruskal_mst_pq(graph):
    # สร้างกราฟเปล่าสำหรับเก็บ Minimum Spanning Tree (MST)
    mst = nx.Graph()
    # สร้างรายการของเส้นเชื่อมทั้งหมดในรูปแบบ (น้ำหนัก, โหนดต้นทาง, โหนดปลายทาง)
    edges = [(weight, u, v) for u in graph for v, weight in graph[u].items()]
    # แปลงรายการ edges เป็น min-heap
    heapify(edges)
    connected = set()    # สร้าง set เพื่อเก็บโหนดที่เชื่อมต่อแล้วใน MST
    # วนลูปจนกว่าจะไม่มีเส้นเชื่อมเหลือใน heap
    while edges:
        # ดึงเส้นเชื่อมที่มีน้ำหนักน้อยที่สุดออกจาก heap
        weight, u, v = heappop(edges)
        # ตรวจสอบว่าการเพิ่มเส้นเชื่อมนี้จะไม่ทำให้เกิด cycle
        if u not in connected or v not in connected or not nx.has_path(mst, u, v):
            # เพิ่มเส้นเชื่อมเข้าไปใน MST
            mst.add_edge(u, v, weight=weight)
            # เพิ่มโหนดทั้งสองเข้าไปใน set ของโหนดที่เชื่อมต่อแล้ว
            connected.add(u)
            connected.add(v)
            print('ต้นทาง',u)
            print('ปลายทาง',v)
            print('น้ำหนักของ {u}',weight)
    # ส่งคืน Minimum Spanning Tree ที่สร้างเสร็จแล้ว
    return mst

G = nx.Graph(graph)
mst = kruskal_mst_pq(graph)

pos = {
    'A': (0, 0), 'B': (2, 1), 'C': (2, -1),
    'D': (4, 2), 'E': (4, 0),
}

plt.figure(figsize=(15, 8))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แก้ไขส่วนนี้เพื่อแสดงน้ำหนักของ edges ให้ถูกต้อง
edge_labels = {(u, v): graph[u][v] for u in graph for v in graph[u]}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

print("เส้นทางใน Minimum Spanning Tree (Kruskal's Algorithm")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")

total_weight = sum(data['weight'] for u, v, data in mst.edges(data=True))
print(f"น้ำหนักรวมทั้งหมด: {total_weight}")

plt.title("Minimum Spanning Tree (Kruskal's Algorithm)", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()