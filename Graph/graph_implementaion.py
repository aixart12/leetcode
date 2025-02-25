def add_edge(mat , i, j):
    # Add on the edge between two vertices

    mat[i][j] = 1
    mat[j][i] = 1

def display_matrix(mat):

    # Dispaly the adjecent matrix
    for row in mat:
        print(" ".join(map(str , row)))


if __name__ == "__main__":
    V = 4
    mat = [[0]*V for _ in range(V)]

     # Add edges to the graph
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

# Graph using list 

def add_edge(adj, i , j ):
    adj[i].append(j)
    adj[j].append(i)

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j , end=' ')
        print()

V = 4
adj = [[] for _ in range(V)]

# Now add edges one by one
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)

print("Adjacency List Representation:")
display_adj_list(adj)