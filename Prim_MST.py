import networkx as nx
import matplotlib.pyplot as plt
import heapq

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

start = 'A'

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
mst = prim_mst(G, start)

# กำหนดตำแหน่งโหนดแบบคงที่
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
plt.show()

# แสดงผลลัพธ์ MST
print("Minimum Spanning Tree (Prim)")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")