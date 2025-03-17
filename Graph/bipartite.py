# Bipartite Graph Check 
# A bipartite graph is a graph whose vertieces can be divided into two independent sets ,
# such that no two adjacent vertices share the set . 

# Mathematically , a graph is bipartite if and only if it does not contain an odd-length cycle 

# How to Check if a Graph is Bipartite?
# We can check if a graph is bipartite using:

# BFS (Breadth-First Search) - Preferred for disconnected graphs
# DFS (Depth-First Search) - Simpler implementation

from collections import deque

def isBipartiteBfs(V , adj):

    color = [-1] * V

    for i in range(V): # For disconnected graph 
        
        if color[i] == -1: # only if not visisted

            color[i] = 0  # mark first one visited by 0 
            q = deque([i])

            while q:
                curr = q.popleft()

                for v in adj[curr]:
                    if color[v] == -1: # only if not visited
                        color[v] = 1 - color[curr] # color are 0 an 1 
                        q.append(v)

                    elif color[v]  == color[curr]:
                        return False
    return True


def dfs(node, color, adj):
    for neighbor in adj[node]:
        if color[neighbor] == -1:  # If uncolored, color it opposite
            color[neighbor] = 1 - color[node]
            if not dfs(neighbor, color, adj):
                return False
        elif color[neighbor] == color[node]:  # Conflict found
            return False
    return True

def is_bipartite_dfs(V, adj):
    color = [-1] * V  # -1 means uncolored

    for start in range(V):  # Handles disconnected graphs
        if color[start] == -1:
            color[start] = 0  # Start coloring with 0
            if not dfs(start, color, adj):
                return False

    return True  # No conflicts found

# Example Usage
print("DFS Bipartite Check:", is_bipartite_dfs(V, adj))




if __name__ == "__main__":
    # Graph Structure:
    # 0 - 1
    # |   |
    # 3 - 2
    V = 4
    adj = [[] for _ in range(V)]

    # Adding edges (undirected)
    adj[0].append(1)
    adj[1].append(0)
    adj[1].append(2)
    adj[2].append(1)
    adj[2].append(3)
    adj[3].append(2)
    adj[3].append(0)
    adj[0].append(3)

    if isBipartiteBfs(V, adj):
        print("true")
    else:
        print("false")