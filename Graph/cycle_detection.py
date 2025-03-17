# Cycle Detection in an Undirected Graph using Depth First Search (DFS)

def isCycleUtil(adj, node, visited, parent):
    """
    Utility function to detect cycle using DFS.
    :param adj: Adjacency list of the graph
    :param node: Current node being visited
    :param visited: List to track visited nodes
    :param parent: Parent node of the current node
    :return: True if cycle is detected, False otherwise
    """
    visited[node] = True  # Mark the current node as visited
    
    for neighbor in adj[node]:
        if not visited[neighbor]:  # If neighbor is not visited, recursively check
            if isCycleUtil(adj, neighbor, visited, node):
                return True
        elif neighbor != parent:  # If neighbor is visited and not the parent, a cycle is found
            return True
    
    return False

def isCycleDFS(adj):
    """
    Function to check if a cycle exists in an undirected graph using DFS.
    :param adj: Adjacency list of the graph
    :return: True if cycle is detected, False otherwise
    """
    V = len(adj)  # Number of vertices
    visited = [False] * V  # Initialize visited array
    
    for u in range(V):  # Check each component of the graph
        if not visited[u]:
            if isCycleUtil(adj, u, visited, -1):  # Start DFS traversal
                return True
    
    return False

# Cycle Detection in an Undirected Graph using Breadth First Search (BFS)
from collections import deque

def bfs(adj, s, visited):
    """
    Utility function to detect cycle using BFS.
    :param adj: Adjacency list of the graph
    :param s: Source node
    :param visited: List to track visited nodes
    :return: True if cycle is detected, False otherwise
    """
    queue = deque()
    queue.append((s, -1))  # Store the node and its parent
    visited[s] = True  # Mark source as visited
    
    while queue:
        node, parent = queue.popleft()
        
        for neighbor in adj[node]:
            if not visited[neighbor]:  # If the neighbor is not visited, mark and enqueue it
                visited[neighbor] = True
                queue.append((neighbor, node))
            elif neighbor != parent:  # If the visited neighbor is not the parent, a cycle exists
                return True
    
    return False

def isCycleBFS(adj):
    """
    Function to check if a cycle exists in an undirected graph using BFS.
    :param adj: Adjacency list of the graph
    :return: True if cycle is detected, False otherwise
    """
    V = len(adj)  # Number of vertices
    visited = [False] * V  # Initialize visited array
    
    for i in range(V):  # Check each component of the graph
        if not visited[i]:
            if bfs(adj, i, visited):  # Start BFS traversal
                return True
    
    return False

# Example Usage
if __name__ == "__main__":
    # Example graph represented as adjacency list
    adj = [
        [1, 2, 3],  # Node 0 is connected to 1, 2, 3
        [0, 2],     # Node 1 is connected to 0, 2
        [0, 1],     # Node 2 is connected to 0, 1
        [0, 4],     # Node 3 is connected to 0, 4
        [3]         # Node 4 is connected to 3
    ]
    
    print("Cycle Detected using DFS:", isCycleDFS(adj))  # Check using DFS
    print("Cycle Detected using BFS:", isCycleBFS(adj))  # Check using BFS