# Tarjan’s Algorithm for Bridges (in Undirected Graphs)

from collections import defaultdict
class Graph:

    def __init__(self , V):
        self.V = V
        self.graph = defaultdict(list)
        self.time = 0 

    def add_edge(self , u , v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def tarjan_bridges_util(self , u , parent , low , disc , bridges):
        disc[u] = low[u] = self.time
        self.time +=1 

        for v in self.graph[u]:
            if disc[v] ==  -1 :
                self.tarjan_bridges_util(v , u , low , disc , bridges)
                low[u] = min(low[u] , low[v])

                if low[v] > disc[u]:
                    bridges.append((u , v))
            
            elif v != parent:
                low[u] = min(low[u] , disc[v])

    def tarjan_bridges(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        bridges= []

        for i in range(self.V):
            if disc[i] == -1:
                self.tarjan_bridges_util( i , -1 , low , disc , bridges)
        return bridge



# Create a graph and add edges
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Bridges in the graph:")
for bridge in g.tarjan_bridges():
    print(bridge)