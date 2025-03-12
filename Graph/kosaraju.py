from collections import defaultdict

class Kosaraju:
    def __init__(self , V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self , x , y):
        self.graph[x].append(y)

    def dfs(self , stack , visited , s):
        visited[s] = True
        for n in self.graph[s]:
            if visited[n] == False:
                self.dfs(stack , visited , n)
        stack.append(s)

    def tra_transpose(self , visited , scc ,  transpose , s):
        visited[s] = True
        scc.append(s)
        for n in transpose[s]:
            if visited[n] == False:
                self.tra_transpose(visited , scc , transpose , n)


    def find_sccs(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.dfs(stack , visited ,i)

        transpose = defaultdict(list)

        for i in range(self.V):
            for j in self.graph[i] :
                transpose[j].append(i)

        visited = [False] * self.V
        sccs = []

        while stack :
            node = stack.pop()
            scc = []
            if visited[node] == False:
                self.tra_transpose(visited , scc , transpose , node)
                sccs.append(scc)

        return sccs
    
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

sccs = g.find_sccs()
print("Strongly Connected Components:", sccs)