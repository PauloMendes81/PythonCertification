# Tower of Hanoi Solver
# The Tower of Hanoi is a classic algorithm puzzle where the goal is to move all disks
# from rod A to rod C, following the rules:
# 1. Only one disk can be moved at a time
# 2. A larger disk cannot be placed on a smaller disk
# 3. All disks must end up on rod C

def hanoi_solver(total_disks):
    """Return a string showing the full Tower of Hanoi solution trace.

    The output includes the starting arrangement and each subsequent state
    after a legal move. Each rod is represented as a list of integers, where
    the smallest disk is 1 and the largest disk is total_disks.
    
    Args:
        total_disks (int): The number of disks to move. Must be non-negative.
    
    Returns:
        str: A multi-line string showing each step of the solution.
    
    Raises:
        TypeError: If total_disks is not an integer.
        ValueError: If total_disks is negative.
    """
    # Validate that total_disks is an integer
    if not isinstance(total_disks, int):
        raise TypeError("total_disks must be an integer.")
    # Validate that total_disks is non-negative
    if total_disks < 0:
        raise ValueError("total_disks must be greater than or equal to 0.")

    # Initialize three rods (A, B, C) with all disks starting on rod A
    # Disks are represented as integers from largest (total_disks) to smallest (1)
    rods = {
        "A": list(range(total_disks, 0, -1)),  # Rod A starts with all disks (largest to smallest)
        "B": [],  # Rod B starts empty
        "C": [],  # Rod C starts empty
    }

    def format_rods():
        """Helper function to format the current state of all rods as a string."""
        return f"{rods['A']} {rods['B']} {rods['C']}"

    # List to store all states of the puzzle (starting state plus all moves)
    moves = [format_rods()]

    def move(n, source, target, auxiliary):
        """Recursive function to solve Tower of Hanoi.
        
        Args:
            n (int): Number of disks to move.
            source (str): The rod to move disks from (A, B, or C).
            target (str): The rod to move disks to (A, B, or C).
            auxiliary (str): The auxiliary rod used for temporary storage (A, B, or C).
        """
        # Base case: if there are no disks to move, return
        if n == 0:
            return

        # Step 1: Move n-1 disks from source to auxiliary using target as temporary storage
        move(n - 1, source, auxiliary, target)
        
        # Step 2: Move the largest disk from source to target
        disk = rods[source].pop()
        rods[target].append(disk)
        # Record the current state after the move
        moves.append(format_rods())
        
        # Step 3: Move n-1 disks from auxiliary to target using source as temporary storage
        move(n - 1, auxiliary, target, source)

    # Call the recursive move function to solve the puzzle: move all disks from A to C using B as auxiliary
    move(total_disks, "A", "C", "B")
    # Return all states as a multi-line string
    return "\n".join(moves)

# Test the hanoi_solver function with different numbers of disks
print(hanoi_solver(2))  # Solve with 2 disks (3 moves total)
print(hanoi_solver(3))  # Solve with 3 disks (7 moves total)
print(hanoi_solver(4))  # Solve with 4 disks (15 moves total)
print(hanoi_solver(5))  # Solve with 5 disks (31 moves total)