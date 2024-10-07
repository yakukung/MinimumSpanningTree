import networkx as nx
import matplotlib.pyplot as plt

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

        # Visualization part
        self.visualize_graph(result)

    def visualize_graph(self, result):
        G = nx.Graph()
        for u, v, w in self.graph:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): w for u, v, w in self.graph}

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight MST edges
        mst_edges = [(u, v) for u, v, w in result]
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color='r')

        plt.title("Graph and Minimum Spanning Tree")
        plt.show()


# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    g.KruskalMST()
