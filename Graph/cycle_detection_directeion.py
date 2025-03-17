def is_cyclic_util(adj, u, visited, rec_stack):
    """
    A utility function to check if a cycle exists in the directed graph using DFS traversal.
    
    Parameters:
    adj (list): Adjacency list representation of the graph.
    u (int): The current node being visited.
    visited (list): List to track visited nodes.
    rec_stack (list): Recursion stack to track nodes in the current DFS path.
    
    Returns:
    bool: True if a cycle is found, otherwise False.
    """
    if rec_stack[u]:  # If the node is already in the recursion stack, a cycle is detected
        return True
    
    visited[u] = True  # Mark the node as visited
    rec_stack[u] = True  # Add it to the recursion stack

    # Recur for all adjacent vertices
    for v in adj[u]:
        if not visited[v] and is_cyclic_util(adj, v, visited, rec_stack):
            return True  # Cycle detected
        elif rec_stack[v]:
            return True  # Cycle detected
    
    rec_stack[u] = False  # Remove the node from the recursion stack before returning
    return False


def is_cyclic(adj):
    """
    Function to check if the given directed graph contains a cycle.
    
    Parameters:
    adj (list): Adjacency list representation of the graph.
    
    Returns:
    bool: True if a cycle is found, otherwise False.
    """
    V = len(adj)  # Number of vertices in the graph
    visited = [False] * V  # List to track visited nodes
    rec_stack = [False] * V  # Recursion stack

    # Perform DFS from each unvisited node
    for i in range(V):
        if not visited[i] and is_cyclic_util(adj, i, visited, rec_stack):
            return True  # Cycle detected
    return False  # No cycle found


if __name__ == "__main__":
    V = 4  # Number of vertices in the graph
    adj = [[] for _ in range(V)]  # Initialize adjacency list

    # Adding directed edges to the graph
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)  # Cycle edge
    adj[2].append(3)
    adj[3].append(3)  # Self-loop cycle

    # Function call to check for a cycle
    if is_cyclic(adj):
        print("Contains Cycle")
    else:
        print("No Cycle")


from collections import deque

def is_cyclic_using_topological_sort(adj):
    """
    Function to check if a directed graph contains a cycle using Kahn's algorithm (Topological Sort).
    
    Parameters:
    adj (list): Adjacency list representation of the graph.
    
    Returns:
    bool: True if a cycle is found, otherwise False.
    """
    V = len(adj)  # Number of vertices
    in_degree = [0] * V  # List to store in-degree of each vertex

    # Compute in-degree of each vertex
    for i in range(V):
        for j in adj[i]:
            in_degree[j] += 1  # Increment in-degree for destination vertex
    
    q = deque()  # Queue to process nodes with in-degree 0

    # Add all vertices with in-degree 0 to the queue
    for i in range(V):
        if in_degree[i] == 0:
            q.append(i)

    count = 0  # Count of visited nodes

    while q:
        curr = q.popleft()  # Remove a vertex from queue
        count += 1  # Increment count of processed nodes

        # Reduce in-degree for all adjacent nodes
        for i in adj[curr]:
            in_degree[i] -= 1  # Decrease in-degree by 1
            if in_degree[i] == 0:
                q.append(i)  # If in-degree becomes 0, add it to queue

    # If count of processed nodes is not equal to V, there is a cycle
    return count != V
