# Using Depth First Search - O(v+e) time and O(v) space


# def isCycleUtil(adj , s , visited , parent):
#     visited[s] = True 
#     for i in adj[s]:
#         if not visited[i]:
#             if isCycleUtil(adj  ,i , visited , s):
#                 return True
        
#         elif i != parent:
#             return True
#     return False

# def isCycle(adj):
#     V = len(adj)

#     visited = [False] * V

#     for u in range(V):
#         if not visited[u]:
#             if isCycleUtil(adj ,u , visited , -1):
#                 return True
            
#     return False

# if __name__ == "__main__":
#     V = 3 
#     adj = [[] for _ in range(V)]

#     adj[1].append(0)
#     adj[0].extend([1, 2])
#     adj[2].extend([0, 1])
#     adj[1].append(2)

#     if isCycle(adj):
#         print("Yes")
#     else:
#         print("No")


# Breadth First Search or BFS for a Graph

from collections import deque

def bfs(adj , s):
    q = deque()
    visited = [False] *len(adj)

    # Mark the source as visited and enqueue it 
    visited[s] = True
    q.append((s , -1))

    while q:
        curr , parent = q.popleft()
        print(curr , end="")

        for n in adj[curr]:
            if not visited[n]:
                visited[n] = True
                q.append(n , curr)
            
            elif n != parent:
                return True
    
    return False

def isCycle(adj):
    n = len(adj)
    visited = [False] * n

    for i in range(n):
        
        # If node is not visited,
        # start BFS from this node.
        if not visited[i]:
            
            # If cycle is found in this 
            # component.
            if bfs(i, adj, visited):
                return True
    
    # If no cycle is found
    return False


if __name__ == "__main__":
    adj = [
        [1, 2, 3],
        [0, 2],
        [0, 1],
        [0, 4],
        [3]
    ]

    if isCycle(adj):
        print("True")
    else:
        print("False")