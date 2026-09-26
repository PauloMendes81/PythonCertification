# Infinity value used to represent an unreachable connection
INF = float('inf')

# Weighted graph represented as an adjacency matrix:
# row = current node, column = neighbor, value = distance
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

# Step 1: Define a function to find the shortest path from a start node
# to one target node or all nodes
def shortest_path(matrix, start_node, target_node=None):
    # Step 2: Get the number of nodes in the graph
    n = len(matrix)

    # Step 3: Initialize all distances to infinity
    # so we know a node is not reached yet
    distances = [INF] * n

    # Step 4: Set the starting node distance to 0
    distances[start_node] = 0

    # Step 5: Create a path list where each node stores the path to reach it
    # Example: paths[3] = [0, 2, 3]
    paths = [[node_no] for node_no in range(n)]

    # Step 6: Track which nodes have already been visited
    visited = [False] * n

    # Step 7: Repeat until all nodes have been processed
    for _ in range(n):
        # Step 8: Find the unvisited node with the smallest current distance
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # Step 9: If no reachable node is found, stop the algorithm
        if current == -1:
            break

        # Step 10: Mark the chosen node as visited
        visited[current] = True

        # Step 11: Check all possible neighbors of the current node
        for node_no in range(n):
            distance = matrix[current][node_no]

            # Ignore unreachable edges and already-visited nodes
            if distance != INF and not visited[node_no]:
                # Step 12: Calculate a potential shorter route
                new_distance = distances[current] + distance

                # Step 13: If this is a shorter path, update the distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance

                    # Step 14: Save the best path to this node
                    paths[node_no] = paths[current] + [node_no]

    # Step 15: Decide which target nodes to print
    targets = [target_node] if target_node is not None else range(n)

    # Step 16: Loop through the desired destinations
    for node_no in targets:
        # Skip the start node and any unreachable nodes
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Step 17: Convert the path list into a readable string
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)

        # Step 18: Print the shortest distance and path
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    # Step 19: Return the final distances and paths
    return distances, paths

# Step 20: Call the function to find the shortest path from node 0 to node 5
shortest_path(adj_matrix, 0, 5)