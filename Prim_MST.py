import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph = {
    'A': {'B': 5, 'C': 10},  
    'B': {'A': 5, 'C': 3, 'D': 8}, 
    'C': {'A': 10, 'B': 3, 'D': 2, 'F': 12},  
    'D': {'B': 8, 'C': 2, 'E': 4, 'F':7}, 
    'E': {'D': 4, 'F': 6}, 
    'F': {'C': 12, 'E': 6, 'D':7},  
}

# สร้างกราฟแบบไม่มีทิศทางด้วย NetworkX
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# ฟังก์ชัน Prim's Algorithm สำหรับหา Minimum Spanning Tree (MST)
def prim_mst(G, start):
    mst = nx.Graph()
    visited = set([start])
    # สร้างลิสต์ของ edges เริ่มต้น โดยเก็บน้ำหนักและโหนดที่เชื่อมโยงกันจากโหนด 'start'
    edges = [(data['weight'], start, neighbor) for neighbor, data in G[start].items()]
    # แปลงลิสต์ edges ให้เป็น heap เพื่อใช้ในการดึงข้อมูลที่มีน้ำหนักน้อยที่สุด
    heapq.heapify(edges)
    while edges:
        # ดึง edge ที่มีน้ำหนักน้อยที่สุดจาก heap
        weight, u, v = heapq.heappop(edges)
        
        # ถ้าโหนด v ยังไม่ได้ถูกเยี่ยมชม
        if v not in visited:
            visited.add(v) # เพิ่มโหนด v ลงในชุด visited
            mst.add_edge(u, v, weight=weight) # เพิ่ม edge ที่เชื่อมระหว่าง u และ v ลงใน MST
            
            # สำหรับโหนด neighbors ที่เชื่อมโยงกับ v
            for neighbor, data in G[v].items():
                # ถ้า neighbor ยังไม่ได้ถูกเยี่ยมชม
                if neighbor not in visited:
                    # เพิ่ม edge ใหม่ลงใน heap สำหรับการพิจารณาในรอบถัดไป
                    heapq.heappush(edges, (data['weight'], v, neighbor))
    
    # ส่งคืนกราฟ MST ที่ได้
    return mst

# หา MST ด้วยอัลกอริธึม Prim
start = 'A'
mst = prim_mst(G, start)

# กำหนดตำแหน่งโหนดแบบคงที่
pos = {
    'A': (0, 0), 'B': (0, 2), 'C': (2, 0),
    'D': (2, 2), 'E': (4, 2), 'F': (4, 0)
}

# วาดกราฟ
plt.figure(figsize=(15, 8))

# ไฮไลท์โหนดเริ่มต้น
node_color = ['lightgreen' if node == start else 'lightblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=3000)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# วาดเส้นเชื่อมทั้งหมดในกราฟ
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

# วาดเส้นเชื่อมของ MST
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แสดงน้ำหนักของ edges
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

# แสดงกราฟ
plt.title("Minimum Spanning Tree (Prim's Algorithm)", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# แสดงผลลัพธ์ MST
print("Minimum Spanning Tree (Prim)")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")