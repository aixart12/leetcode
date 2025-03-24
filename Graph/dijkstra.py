import heapq
import sys

# Function to add an edge to the adjacency list
def addEdge(adj, u, v, wt):
    adj[u].append((v, wt))
    adj[v].append((u, wt))

# Dijkstra's Algorithm using a priority queue
def shortestPath(adj, V, src):
    pq = []
    dist = [float('inf')] * V  # Initialize distances as infinite
    
    heapq.heappush(pq, (0, src))
    dist[src] = 0

    while pq:
        distance, u = heapq.heappop(pq)

        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    # Print shortest distances stored in dist[]
    print("Vertex Distance from Source")
    for i in range(V):
        print(i, "   ", dist[i])

# Class for Graph representation and Dijkstra's Algorithm using adjacency matrix
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize
        min_index = -1

        # Find the vertex with the minimum distance value
        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u
        
        return min_index
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V # (Shortest Path Tree Set) is used to keep track of the vertices that have been included in the shortest path tree.

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            if x == -1:
                break  # If no valid node is found, break

            sptSet[x] = True  # Include x in the shortest path tree

            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        
        self.printSolution(dist)

# Main function
def main():
    V = 9
    adj = [[] for _ in range(V)]

    # Adding edges to the adjacency list
    addEdge(adj, 0, 1, 4)
    addEdge(adj, 0, 7, 8)
    addEdge(adj, 1, 2, 8)
    addEdge(adj, 1, 7, 11)
    addEdge(adj, 2, 3, 7)
    addEdge(adj, 2, 8, 2)
    addEdge(adj, 2, 5, 4)
    addEdge(adj, 3, 4, 9)
    addEdge(adj, 3, 5, 14)
    addEdge(adj, 4, 5, 10)
    addEdge(adj, 5, 6, 2)
    addEdge(adj, 6, 7, 1)
    addEdge(adj, 6, 8, 6)
    addEdge(adj, 7, 8, 7)
    
    # Finding shortest paths from source vertex 0
    shortestPath(adj, V, 0)

if __name__ == "__main__":
    main()
