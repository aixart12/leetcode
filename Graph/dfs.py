# Time complexity : O(v + e) , v is the number of verties and e is the number is edges in the graph
# Auxiliary Space : 0(v + e) , since the an extra visited array of size V is required , And stack size for the recursive 
# calls to DFSRec Fucntion 


def dfs_rec(adj , visited , s):
    #  Mark the current vertex as visisted 
    visited[s] = True

    print(s , end=" ")

    # Recursively vist all adjacent vertices
    # that are not visited yet

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj , visited , i)


def dfs(adj , s):
    visited = [False] * len(adj)
    dfs_rec(adj ,visited , s)

def add_edge(adj , s , t):
    adj[s].append(t)
    adj[t].append(s)


if __name__ == "__main__":
    v = 5

    # Create an adjecency list for the graph 
    adj = [[] for _ in range(v)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges 
    for e in edges:
        add_edge(adj , e[0] , e[1])
    
    souce = 1

    print("DFS from the source " , souce)

    dfs(adj, souce)


# DFS for Complete Traversal of Disconnected Undirected Graph 

# Time complexity: O(V + E). Note that the time complexity is same here because we visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
# Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to DFSRec function. 
class Graph : 
    def __init__(self , v):
        self.adj = [[] for _ in range(v)]
    
    def add_edges(self, s , t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def dfs_rec(self , visited , s):
        visited[s] = True

        # Recursively visit al the adjacent vertices 
        # that are not visited yet

        for i in range(len(self.adj[s])):
            if not visited[i]:
                self.dfs_rec(visited , i)
    
    def dfs(self):
        visited = [False] * len(self.adj) 

        # Loop through all vertices to handle disconnected
        # graph
        for i in range(len(self.adj)):
            if not visited[i]:
                  # Perform DFS from unvisited vertex
                self.dfs_rec(visited, i)
    
# if __name__ == "__main__":
#     V = 6  # Number of vertices
#     graph = Graph(V)

#     # Define the edges of the graph
#     edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

#     # Populate the adjacency list with edges
#     for edge in edges:
#         graph.add_edge(edge[0], edge[1])

#     print("Complete DFS of the graph:")
#     graph.dfs()  # Perform DFS