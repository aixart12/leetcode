from collections import deque

# BFS from the given source s

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. This is because BFS explores each vertex and edge exactly once.
# Auxiliary Space: O(V), The queue used in BFS, which can hold up to V vertices and The color array (or map), which stores the color for each vertex

def bfs(adj, s):
    q = deque

    # Initlaise the visited array
    visited = [False] * len(adj)

    visited[s] = True
    q.append(s)

    # Irrateate

    while q:
        curr = q.popleft()

        print(curr , end=" ")

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
            
def add_edge(adj , u  , v):
    adj[u].append(v)
    adj[v].append(u)


# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)

# BFS of the whole Graph which Maybe Disconnected

def bfs_new(adj, s , visited):
    q = deque()

    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        print(curr , end="")

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


# Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj) # Not visited

    for i in range(len(adj)):
        if not visited[i]:
            bfs_new(adj, i, visited)