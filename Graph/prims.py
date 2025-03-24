# Prim's algorithm is a Greedy alogrithm . This algorithm always starts with a single node and moves
# through serveral adjacent nodes , in order to explore all of the connected edges along the way

        # We transform the adjacency matrix into adjacency list using ArrayList<ArrayList<Integer>>. in Java, list of list in Python  
        # and array of  vectors in C++.
        # Then we create a Pair class to store the vertex and its weight .
        # We sort the list on the basis of lowest weight.
        # We create priority queue and push the first vertex and its weight in the queue
        # Then we just traverse through its edges and store the least weight in a variable called ans.
        # At last after all the vertex we return the ans.

# for finding the mst -> minimum spanning tree => if n = 5 then e = 5 - 1 = 4 , whose edge sum in least

import heapq

def tree(V, E, edges):
    # Create an adjacency list representation of the graph
    adj = [[] for _ in range(V)]
    # Fill the adjacency list with edges and their weights
    for i in range(E):
        u, v, wt = edges[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    # Create a priority queue to store edges with their weights
    pq = []
    # Create a visited array to keep track of visited vertices
    visited = [False] * V
    # Variable to store the result (sum of edge weights)
    res = 0
    # Start with vertex 0
    heapq.heappush(pq, (0, 0))
    # Perform Prim's algorithm to find the Minimum Spanning Tree
    while pq:
        wt, u = heapq.heappop(pq)
        if visited[u]:
            continue  
            # Skip if the vertex is already visited
        res += wt  
        # Add the edge weight to the result
        visited[u] = True  
        # Mark the vertex as visited
        # Explore the adjacent vertices
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))  
                # Add the adjacent edge to the priority queue
    return res  
  # Return the sum of edge weights of the Minimum Spanning Tree
if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(tree(3, 3, graph))
