def dfs(adj_matrix, node = 0):
    visited = []
    # A stack makes this an iterative depth-first traversal.
    stack = [node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            # Record each node once so cycles cannot cause repeated visits.
            visited.append(current_node)
            # Connected columns in this row are the current node's neighbors.
            neighbors = [i for i, is_connected in enumerate(adj_matrix[current_node]) if is_connected]
            # Add them to the stack; the most recently added is explored next.
            stack.extend(neighbors)

    # Return nodes in the order they were visited.
    return visited


    