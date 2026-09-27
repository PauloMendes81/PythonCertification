def countup(number):
    # Base case: if the number is 0 or less, there are no values to count.
    if number < 1:
        return []

    # Recursively build the list for the smaller numbers, then add the current one.
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list

print(countup(5))  # Output: [1, 2, 3, 4, 5]