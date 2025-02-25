
# DFS T = (V + E) , space = O(v)
def topologicalSortUtil(adj , s , visited , st):
    visited[s]  = True

    for x in adj[s]:
        if not visited[x]:
            topologicalSort(adj , x , visited , st)
    
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