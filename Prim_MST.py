import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph = {
    'A': {'B': 5, 'C': 10},  
    'B': {'A': 5, 'C': 3, 'D': 8}, 
    'C': {'A': 10, 'B': 3, 'D': 2, 'F': 12},  
    'D': {'B': 8, 'C': 2, 'E': 4}, 
    'E': {'D': 4, 'F': 6}, 
    'F': {'C': 12, 'E': 6},  
}

# สร้างกราฟแบบไม่มีทิศทางด้วย NetworkX
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# ใช้อัลกอริธึม Prim เพื่อหา Minimum Spanning Tree (MST)
def prim_mst(G, start):
    mst = nx.Graph()  # โครงสร้างเก็บ MST
    visited = set([start])  # เก็บโหนดที่เยี่ยมแล้ว
    edges = [(data['weight'], start, neighbor) for neighbor, data in G[start].items()]  # เริ่มต้นจากโหนดแรก
    heapq.heapify(edges)  # ใช้ heap เพื่อจัดการลำดับเส้นทาง

    while edges:
        weight, u, v = heapq.heappop(edges)  # นำเส้นทางที่น้ำหนักน้อยที่สุดออก
        if v not in visited:
            visited.add(v)  # เพิ่มโหนดที่ยังไม่เยี่ยม
            mst.add_edge(u, v, weight=weight)  # เพิ่มเส้นทางเข้า MST

            # เพิ่มเส้นทางใหม่จากโหนดที่เพิ่งเยี่ยมไปยังโหนดที่ยังไม่ได้เยี่ยม
            for neighbor, data in G[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (data['weight'], v, neighbor))

    return mst

# หา MST ด้วยอัลกอริธึม Prim
start = ('A')
mst = prim_mst(G, start)

# ตำแหน่งโหนดสำหรับวาดกราฟ
pos = nx.spring_layout(G)

# วาดกราฟ
plt.figure(figsize=(10, 6))
# ไฮไลท์โหนดเริ่มต้น
node_color = ['lightgreen' if node == start else 'lightblue' for node in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=500)
nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# วาดเส้นเชื่อมทั้งหมดในกราฟ
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, arrows=False)

# วาดเส้นเชื่อมของ MST
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r', width=2, arrows=False)

# แสดงน้ำหนักของ edges
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_weight='bold')

# แสดงกราฟ
plt.title("Minimum Spanning Tree (Prim's Algorithm)", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

# แสดงผลลัพธ์ MST
print("เส้นทางใน Minimum Spanning Tree (Prim):")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")
