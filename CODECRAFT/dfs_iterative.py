 # Function to perform DFS traversal iteratively
def dfs_iterative(graph, start_vertex):
    # Stack to hold vertices for processing
    stack = [start_vertex]
    # Set to track visited vertices
    visited = set()
    
    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()
        
        # Process the vertex if it hasn't been visited
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            
            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }
    
    # Perform DFS starting from vertex 0
    print("Iterative DFS traversal starting from vertex 0:")
    dfs_iterative(graph, 0)