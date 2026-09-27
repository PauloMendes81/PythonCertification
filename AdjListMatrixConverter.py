a_list = {
    0: [2], 
    1: [2, 3], 
    2: [0, 1, 3], 
    3: [1, 2]
    }

def adjacency_list_to_matrix(adj_list):
    """
    Convert an adjacency list to an adjacency matrix.

    Parameters:
    adj_list (dict): A dictionary representing the adjacency list of a graph.

    Returns:
    list: A 2D list representing the adjacency matrix of the graph.
    """
    # Get the number of vertices in the graph
    num_vertices = len(adj_list)
    
    # Initialize a num_vertices x num_vertices matrix with zeros
    adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    # Fill the adjacency matrix based on the adjacency list
    for vertex, neighbors in adj_list.items():
        for neighbor in neighbors:
            adj_matrix[vertex][neighbor] = 1  # Assuming an unweighted graph
    
    for row in adj_matrix:
        print(row)

    return adj_matrix

adjacency_list_to_matrix(a_list)