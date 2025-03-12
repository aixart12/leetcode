from collections import defaultdict

class TarjanArticulation:
    def __init__(self , V):
        self.V = V
        self.graph = defaultdict(list)
        self.time = 0 

    def add_edge(self , u , v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def articulation_util(self , u , parent , visited , disc , low , ap ):
        pass
    
    def find_articulation_points(self):
        visited = [False]* self.V
        disc = [-1] * self.V
        low = [-1] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.articulation_util(i , -1 , visited , disc , low , ap)
        
        return [i for i in range(self.V) if ap[i]]

# Example Usage
g = TarjanArticulation(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(5, 6)

print("Articulation Points:", g.find_articulation_points())