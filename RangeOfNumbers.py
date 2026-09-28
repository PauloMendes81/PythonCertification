def range_of_numbers(start_num, end_num):
    """
    Generate a list of numbers from start to end (inclusive).

    Parameters:
    start_num (int): The starting number of the range.
    end_num (int): The ending number of the range.

    Returns:
    list: A list containing numbers from start to end.
    """
    # Stop when there are no numbers left to add.
    if start_num > end_num:
        return []
    # Add the current number, then recurse with the next one.
    return [start_num] + range_of_numbers(start_num + 1, end_num)