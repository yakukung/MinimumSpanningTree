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

# ฟังก์ชัน Prim's Algorithm สำหรับหา MST
def prim_mst(G, start):
    mst = nx.Graph()
    visited = set([start])
    edges = [(data['weight'], start, neighbor) for neighbor, data in G[start].items()]
    heapq.heapify(edges)
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.add_edge(u, v, weight=weight)
            
            for neighbor, data in G[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (data['weight'], v, neighbor))
    
    return mst

# หา MST ด้วยอัลกอริธึม Prim
start = 'A'
mst = prim_mst(G, start)

# กำหนดตำแหน่งโหนดแบบคงที่
pos = {
    'A': (0, 0),
    'B': (0, 2),
    'C': (2, 0),
    'D': (2, 2),
    'E': (4, 2),
    'F': (4, 0)
}

# วาดกราฟ
plt.figure(figsize=(12, 8))

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
print("เส้นทางใน Minimum Spanning Tree (Prim):")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} : น้ำหนัก {data['weight']}")
print(f"น้ำหนักรวมทั้งหมด: {sum(data['weight'] for u, v, data in mst.edges(data=True))}")