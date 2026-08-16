def hanoi_solver(total_disks):
    """Return a string showing the full Tower of Hanoi solution trace.

    The output includes the starting arrangement and each subsequent state
    after a legal move. Each rod is represented as a list of integers, where
    the smallest disk is 1 and the largest disk is total_disks.
    """
    if not isinstance(total_disks, int):
        raise TypeError("total_disks must be an integer.")
    if total_disks < 0:
        raise ValueError("total_disks must be greater than or equal to 0.")

    rods = {
        "A": list(range(total_disks, 0, -1)),
        "B": [],
        "C": [],
    }

    def format_rods():
        return f"{rods['A']} {rods['B']} {rods['C']}"

    moves = [format_rods()]

    def move(n, source, target, auxiliary):
        if n == 0:
            return

        move(n - 1, source, auxiliary, target)
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(format_rods())
        move(n - 1, auxiliary, target, source)

    move(total_disks, "A", "C", "B")
    return "\n".join(moves)

print(hanoi_solver(2))
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))