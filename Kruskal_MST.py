import networkx as nx
import matplotlib.pyplot as plt
from heapq import heapify, heappop

graph = {
    'A': {'B': 7, 'C': 6, 'D': 15, 'E':15},  
    'B': {'A': 7, 'C': 13, 'D': 8 ,'F':12}, 
    'C': {'A': 6, 'B': 13, 'E': 9, 'H': 1},  
    'D': {'A': 10, 'B': 8, 'E': 19, 'F':16, 'G':17}, 
    'E': {'A': 15, 'C':9, 'D':19, 'G':11, 'H':5}, 
    'F': {'B': 12, 'D': 16, 'G':14, 'I':18}, 
    'G': {'D':17, 'E':11, 'F':14, 'H':3, 'I':2},
    'H': {'C':1, 'E':5, 'G':3, 'I':4},
    'I': {'F':18, 'G':2, 'H':4}
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
            print(f'น้ำหนักของ {u} ไป {v} =', weight)
            print('==========================')
    # ส่งคืน Minimum Spanning Tree ที่สร้างเสร็จแล้ว
    return mst

G = nx.Graph(graph)
mst = kruskal_mst_pq(graph)

pos = {
    'A': (6, 2),    # ระหว่าง D และ C
    'B': (8, 4),    # ด้านบนขวา
    'C': (8, 0),    # ด้านขวาล่าง
    'D': (4, 3),    # ตรงกลางค่อนขวา
    'E': (4, 1),    # ตรงกลางค่อนซ้าย
    'F': (2, 4),    # ด้านซ้ายบน
    'G': (2, 2),    # ระหว่าง F และ I
    'H': (2, 0),    # ด้านล่าง
    'I': (0, 2)     # ด้านซ้ายล่าง
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