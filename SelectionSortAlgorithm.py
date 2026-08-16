# Selection Sort Algorithm
# Time Complexity: O(n²)
# Space Complexity: O(1)
# Description: Sorts an array by repeatedly finding the minimum element 
# and placing it at the beginning of the unsorted portion

def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    
    Args:
        arr (list): The array to be sorted
        
    Returns:
        list: The sorted array
    """
    n = len(arr)
    
    # Iterate through each position in the array
    for i in range(n):
        # Assume the current index has the minimum value
        min_index = i
        
        # Search for the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            # Update min_index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the element at current position
        # Only swap if the minimum element is not already in the correct position
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted array
    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))