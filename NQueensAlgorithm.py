def dfs_n_queens(n):
    # A board with no rows cannot contain a queen placement.
    if n < 1:
        return []

    # Each solution stores the queen's column for each row.
    solutions = []
    placement = []
    # These sets make conflict checks constant-time.
    used_columns = set()
    used_diagonals = set()
    used_antidiagonals = set()

    def search(row):
        # One safe position in every row forms a complete solution.
        if row == n:
            # Save a copy because placement is reused during backtracking.
            solutions.append(placement.copy())
            return

        # Place one queen in this row, then recursively solve the next row.
        for column in range(n):
            # Queens share a diagonal when row-column or row+column matches.
            diagonal = row - column
            antidiagonal = row + column
            if (
                column in used_columns
                or diagonal in used_diagonals
                or antidiagonal in used_antidiagonals
            ):
                continue

            placement.append(column)
            used_columns.add(column)
            used_diagonals.add(diagonal)
            used_antidiagonals.add(antidiagonal)

            search(row + 1)

            # Undo this placement before trying the next column.
            placement.pop()
            used_columns.remove(column)
            used_diagonals.remove(diagonal)
            used_antidiagonals.remove(antidiagonal)

    search(0)
    return solutions