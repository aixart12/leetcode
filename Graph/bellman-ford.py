# Best Case: O(E), when distance array after 1st and 2nd relaxation are same , we can simply stop further processing.
# Average Case: O(V*E)
# Worst Case: O(V*E)

def bellmanFord(V , edges , src):
    dist = [100000000] * V
    dist[src]= 0

    for i in range(V):
        for edge in edges:
            u, v, wt = edge # take out u , v and wt for edge
            if dist[u] != 100000000 and dist[v] > dist[u] + wt : # check if the next node v a graterer currenlty in dist list 
                 # If this is the Vth relaxation, then there 
                # is a negative cycle
                if i == V - 1:
                    return [-1]
                # Update shortest distance to node v
                dist[v] = dist[u] + wt

    return dist


if __name__ == '__main__':
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]

    src = 0
    ans = bellmanFord(V, edges, src)
    print(' '.join(map(str, ans)))