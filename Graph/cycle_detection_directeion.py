def is_cyclic_util(adj ,u , visited , rec_stack):

    if rec_stack[u]:
        return True
    
    visited[u] = True
    rec_stack[u] = True

    for v in adj[u]:
        if not visited[v] and is_cyclic_util(adj , v , visited , rec_stack):
            return True
        elif rec_stack[v]:
            return True
    rec_stack[u] = False

    return False



def is_cyclic(adj):
    V = len(adj)
    visited = [False] * V
    rec_stack = [False] * V

    for i in range(V):
        if not visited[i] and  is_cyclic_util(adj, i , visited , rec_stack):
            return True
    return False


if __name__ == "__main__":
    V = 4
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(3)

    # Function call
    if is_cyclic(adj):
        print("Contains Cycle")
    else:
        print("No Cycle")


from collections import deque

def is_cyclic_using_topological_sort(adj):
    V = len(adj)
    in_degree = [0] * V

    for i in range(V):
        for j in adj[i]:
            in_degree[j]+=1
    
    q = deque()

    for i in range(V):
         if in_degree[i] == 0:
             q.append(i)

    count = 0

    while q:
        curr = q.popleft()
        count+=1

        for i in adj[curr]:
            in_degree[i]-=1
            if in_degree[i] == 0:
                q.append(in_degree[i])

    return count != V


