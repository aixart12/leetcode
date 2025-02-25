from collections import deque

def isBipartite(V , adj):

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


def dfs(u , color , colors, adj):
    #Assign the color to the current u 
    colors[u] = color

    for v in adj[u]:
        if color[v] == -1:
            if not dfs(v , 1 - color , colors , adj):
                return False
        elif colors[v] == color:
            return False
    return True

def isBipartiteDfs(V , adj):
    colors = [-1] * V

    # Check each componenet of the graph

    for i in range(V):
        # If the vertex is uncolored
        if colors[i] == -1:
            if not dfs(i , 0 , colors , adj):
                return False
    return True




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

    if isBipartite(V, adj):
        print("true")
    else:
        print("false")