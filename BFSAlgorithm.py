def gen_parentheses(pairs):
    # Reject invalid input before starting the search.
    if not isinstance(pairs, int):
        return f'The number of pairs should be an integer'
    if pairs < 1:
        return f'The number of pairs should be at least 1' 
    
    # Each state stores the string built so far and the opening/closing counts.
    queue = [('', 0, 0)] 

    # Process states in FIFO order, exploring combinations by length.
    while queue:
        #print(queue)
        current, opens_used, closes_used = queue.pop(0)
        # A string with 2 * pairs characters is a complete combination.
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            # Add an opening parenthesis while pairs remain to be opened.
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            # A closing parenthesis is valid only after an unmatched opening one.
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))


    result = []    
    return result

print(gen_parentheses(2))
print(gen_parentheses(3))