# What is toplogical Sort 
# It is a linear ordering of vertices in the Directed Acyclic Graph (DAG ) such that for 
# every directed edge u ---> v , vertex u comes before vertex v in the ordering . 

# Application of Topological Sort 
#  Task scheduling ( e.g . dependencies between task in a project)
#  Compilation Order of Code Modules ( eg. resolving dependencies in programming)
#  Precedence Constraints ( eg. course prerequequisite problems in universities)
#  Resolving Depeondencies in Package Manager ( eg. Installing software packages)


# DFS T = (V + E) , space = O(v)
def topologicalSortUtil(adj , s , visited , st):
    visited[s]  = True

    for x in adj[s]:
        if not visited[x]:
            topologicalSortUtil(adj , x , visited , st)
    
    st.append(s)

def topologicalSort(adj):
    V = len(adj)

    st = []
    visited = [False] * V

    for i in range(V):
        if not visited:
            topologicalSort(adj , i , visited , st)

    return st[::-1]



if __name__ == "__main__":
    
    # Graph represented as an adjacency list
    adj = [[1], [2], [], [1, 2]]

    ans = topologicalSort(adj)
    print(" ".join(map(str, ans)))


from collections import deque

def toplogical_sort_bfs(V , adj):
    indegree = [0] * V # Step 1: Calculate indegree of each node
    for i in range(V):
        for j in adj[i]:
            indegree[j] +=1
    
    queue = deque() # Step 2: Add all nodes with indegree 0 to queue
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
    
    topo_sort = []

    while queue:
        node = queue.popleft()
        topo_sort.append(node)

        for neighbour in adj[node]: # Reduce indegree of neighbour 
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0 : 
                queue.append(neighbour)
    
    if len(topo_sort) != V: 
        return " Graph is Cyclic , topological sorting not possilbe"
    
    return topo_sort



