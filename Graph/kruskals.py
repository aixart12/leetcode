from functools import cmp_to_key

def comparator(a,b):
    return a[2] - b[2]

def kruskals_mst(V , edges):
    
    # sort all edges 
    edges = sorted(edges , key=cmp_to_key(comparator))

    # Traverse edges in sorted order

    dsu = DisjointSetUnion(V)

    cost = 0
    count = 0
    for x , y , w in edges:
        if dsu.find(x) != dsu.find(y): # the they are connected
            dsu.union(x , y)
            cost +=w
            count +=1
            if count == V -1:
                break
    return cost

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

if __name__ == '__main__':
    
    # An edge contains, weight, source and destination
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print(kruskals_mst(4, edges))