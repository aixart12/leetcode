# for finding the mst -> minimum spanning tree => if n = 5 then e = 5 - 1 = 4 , whose edge sum in least

import heapq

def tree(V , E , graph):
    adj = [[] for _ in range(V)]

    for edge in graph:
        u , v , wt = edge
        adj[u].append((v , wt))
        adj[v].append((u , wt))

    pq = []
    res  = 0
    visited = [False] * V

    # initalise with root ( wt , v)
    heapq.heappush(pq , (0 ,0))

    while pq:
        wt , curr = heapq.heappop(pq)

        if visited[curr]:
            continue

        visited[curr] = True # make ture only when pop form the stack 
        res += wt

        for u , w in adj[curr]:      
            if not visited[u]:
                heapq.heappush(w , u )

    return res
    
if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(tree(3, 3, graph))