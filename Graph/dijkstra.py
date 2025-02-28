# Shortest Paths from Source to all Vertices using Dijkstra’s Algorithm
# Time Complexity: O(E * logV), Where E is the number of edges and V is the number of vertices. 
# Auxiliary Space: O(V) 
import heapq

def addEdge(adj , u , v , wt):
    adj[u].append((v, wt))
    adj[v].append((u, wt))

def shortestPath(adj, V , src):
    pq = []
    dist = [float('inf')] * V # make a array of infinte 

    heapq.heappush(pq, (0 , src))

    dist[src] = 0

    while pq:
        distance , u  = heapq.heappop(pq)

        for v , weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq , (dist[v] , v )) 
        
    # Print shortest distances stored in dist[]
    print("Vertex Distance from Source")
    for i in range(V):
        print(i,"   ",dist[i])


# Main function
if __name__ == "__main__":
    V = 9
    adj = [[] for _ in range(V)]

    # Making the graph
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


import sys

class Graph():
    def __init__(self , vertices):
        self.V = vertices 
        self.graph = [[0] for coulmn in range(vertices) for row in range(vertices)]

    def printSolution(self , dist):
        print("Vertex \tDisatnce from the Source")
        for node in range(self.V):
            print(node , "\t" , dist[node])

    def minDistance(self , dist , sptSet):
        min = sys.maxsize # Initialize minium distance for next node

        # Search for nearest vertex not in the shortest parth tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min  = dist[u]
                min_index = u
        
        return min_index
    
    def dijkstra(self , src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):

            x = self.minDistance(dist , sptSet)

            sptSet[x] = True # Put the minimum distance vertex in the shortest path tree

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        
    
        self.printSolution(dist)