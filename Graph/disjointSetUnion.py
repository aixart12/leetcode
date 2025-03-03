class DisjointSetUnion:
    def __init__(self , V):
        self.rank = [0] * V
        self.parent = list(range(V))

    def find(self , x):
        if self.parent[x] != x : 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self , x , y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else :

                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self , x , y):
        return self.find(x) == self.find(y)  # compare the ulitmate parenet 
                   


dsu = DisjointSetUnion(5)  # Create DSU for 5 elements (0 to 4)

dsu.union(0, 1)
dsu.union(1, 2)
dsu.union(3, 4)

print(dsu.connected(0, 2))  # True (0 and 2 are connected)
print(dsu.connected(0, 4))  # False (0 and 4 are not connected)


# Dis joint set union by size 

class DisjointSetUninoBySize:
    def __init__(self , n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self , x):
        if self.parent[x] != x:
            self.parent[x]  = self.find(self.parent[x])
        return self.parent[x]

    def union(self , x ,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size(rootY):
                self.parent[rootY] = rootX
                self.size[rootX] +=  self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] +=  self.size[rootY]  
    
    def connected(self , x , y):
        return self.find(x) == self.find(y)  # compare the ulitmate parenet 

        