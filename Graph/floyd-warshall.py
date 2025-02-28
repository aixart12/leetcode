# Time Complexity: O(V3), where V is the number of vertices in the graph and we run three nested loops each of size V.
# Auxiliary Space: O(V2), to create a 2-D matrix in order to store the shortest distance for each pair of nodes.


def floydWarshall(graph):
    V = len(graph)
    # Add all vertices one by one to the set of intermediate vertices.

    for k in range(V):
        
        # Pick all the vertices as source one by one

        for i in range(V):

            # Pick all the vetices as destination 
            for j in range(V):


                if ((graph[i][j] == -1 or                               # If there is no direct edge between ii and jj (i.e., it's currently unreachable).
                    graph[i][j] > (graph[i][k] + graph[k][j]))          # If going through kk gives a shorter path than the current known shortest path.
                    and (graph[k][j] != -1 and graph[i][k] != -1)):     # Ensure that both ii to kk and kk to jj exist (to avoid adding non-existent edges).
                    graph[i][j] = graph[i][k] + graph[k][j]             # If the conditions are met, update the shortest distance from ii to jj by passing through kk.
                    

    # **Step to Detect Negative Cycle**
    # If any graph[i][i] becomes negative, then there is a negative cycle. , we only chekc after geeting the shorted path 
    for i in range(V):
        if graph[i][i] < 0:
            print("Negative cycle detected!")
            return  # Stop further execution

    # Print the shortest distance matrix
    for i in range(V):
        for j in range(V):
            print(graph[i][j], end=" ")
        print()

# Example graph
if __name__ == "__main__":
    graph = [
        [0, 4, -1, 5, -1],
        [-1, 0, 1, -1, 6],
        [2, -1, 0, 3, -1],
        [-1, -1, 1, 0, 2],
        [1, -1, -1, 4, 0]
    ]
    
    floydWarshall(graph)