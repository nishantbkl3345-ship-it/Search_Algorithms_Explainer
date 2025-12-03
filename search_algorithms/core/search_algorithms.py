"""
Core search algorithm implementations.

This module contains the main search algorithms with step-by-step execution tracking.
"""


def linear_search(arr, target):
    """
    Perform linear search with step-by-step explanation.
    
    Args:
        arr (list): The list to search in.
        target (int): The target value to find.
        
    Returns:
        tuple: (index_found_or_-1, steps_taken)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    print("\n--------- LINEAR SEARCH ---------")
    steps = 0

    for i in range(len(arr)):
        value = arr[i]
        steps += 1
        print(f"Step {steps} : index = {i} , element = {value} , target = {target}")

        if value == target:
            print("=> Match found")
            print(f"=> Element {target} found at index {i}")
            print(f"Total steps taken (Linear Search): {steps}")
            return i, steps
        else:
            print("=> Not equal, moving next\n")

    print("=> Element not found")
    print(f"Total steps taken (Linear Search): {steps}")
    return -1, steps


def binary_search(arr, target):
    """
    Perform binary search with step-by-step explanation on a sorted copy.
    
    Args:
        arr (list): The list to search in (will be sorted).
        target (int): The target value to find.
        
    Returns:
        tuple: (index_found_or_-1_in_sorted_array, steps_taken)
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Note: Binary search requires a sorted list, so this function creates
    a sorted copy of the input array.
    """
    print("\n--------- BINARY SEARCH ---------")
    if len(arr) == 0:
        print("List is empty. Nothing to search.")
        return -1, 0

    # Binary search requires a sorted list → use a sorted copy
    sorted_arr = sorted(arr)
    print("Note: Binary Search works on a sorted list.")
    print("Sorted list used:")
    _print_list_plain(sorted_arr)

    low, high = 0, len(sorted_arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        value = sorted_arr[mid]

        print(
            f"Step {steps} : low = {low} , high = {high} , mid = {mid} , "
            f"element = {value} , target = {target}"
        )

        if value == target:
            print("=> Match found")
            print(f"=> Element {target} found at index {mid} (in sorted list)")
            print(f"Total steps taken (Binary Search): {steps}")
            return mid, steps
        elif value < target:
            print("=> element < target , searching RIGHT half (low = mid + 1)\n")
            low = mid + 1
        else:
            print("=> element > target , searching LEFT half (high = mid - 1)\n")
            high = mid - 1

    print("=> Element not found")
    print(f"Total steps taken (Binary Search): {steps}")
    return -1, steps


def _print_list_plain(arr):
    """Print the list in a simple, single-line format."""
    output = " ".join(str(x) for x in arr)
    print(f"List contents: {output}")
