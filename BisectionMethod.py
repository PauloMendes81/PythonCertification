def square_root_bisection(number, tolerance=1e-10, max_number=1000):

    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)

    for _ in range(max_number):

        root = (low + high) / 2

        if high - low <= tolerance:
            print(f"The square root of {number} is approximately {root}")
            return root

        if root ** 2 < number:
            low = root
        else:
            high = root

    print(f"Failed to converge within {max_number} iterations")
    return None