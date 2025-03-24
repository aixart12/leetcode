# Kosaraju’s Algorithm is used to find Strongly Connected Components (SCCs) in a 
# directed graph. A SCC is a subgraph in which every vertex is reachable from every 
# other vertex within the same component.
# Kosaraju's algorithm runs in O(V + E) time, where:


from collections import defaultdict

class Kosaraju:
    def __init__(self , V):
        """
        Initializes the graph with V vertices.
        """
        self.V = V  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list representation

    def add_edge(self , x , y):
        """
        Adds a directed edge from x to y.
        """
        self.graph[x].append(y)

    def dfs(self , stack , visited , s):
        """
        Performs DFS and stores the vertices in a stack based on their finish time.
        """
        visited[s] = True
        for n in self.graph[s]:
            if not visited[n]:
                self.dfs(stack , visited , n)
        stack.append(s)  # Push vertex to stack after visiting all neighbors

    def tra_transpose(self , visited , scc , transpose , s):
        """
        Performs DFS on the transposed graph to find SCCs.
        """
        visited[s] = True
        scc.append(s)  # Add node to the current SCC
        for n in transpose[s]:
            if not visited[n]:
                self.tra_transpose(visited , scc , transpose , n)

    def find_sccs(self):
        """
        Finds and returns all Strongly Connected Components (SCCs) using Kosaraju's algorithm.
        """
        # Step 1: Fill the stack with vertices based on their finishing time
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.dfs(stack , visited ,i)

        # Step 2: Create the transpose graph (reverse all edges)
        transpose = defaultdict(list)
        for i in range(self.V):
            for j in self.graph[i]:
                transpose[j].append(i)

        # Step 3: Perform DFS on the transposed graph in the order of the stack
        visited = [False] * self.V
        sccs = []  # List to store SCCs

        while stack:
            node = stack.pop()
            scc = []
            if not visited[node]:
                self.tra_transpose(visited , scc , transpose , node)
                sccs.append(scc)  # Add the SCC to the result

        return sccs  # Return all SCCs
    
# Example Usage
g = Kosaraju(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(5, 6)

# Finding and printing the SCCs
sccs = g.find_sccs()
print("Strongly Connected Components:", sccs)
