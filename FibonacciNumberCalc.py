def fibonacci(n):
    # Seed the sequence with the first two Fibonacci numbers.
    sequence = [0, 1]
    # Negative indices are not supported.
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    # The first two values are already known.
    if n <= 1:
        return n
    # Append values through the requested index.
    for _ in range(2, n + 1):
        # Each value is the sum of the two preceding values.
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[n]