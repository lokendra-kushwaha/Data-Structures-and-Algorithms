"""
================================================================================
                        UNDERSTANDING BINARY SEARCH
================================================================================

1. WHAT IS BINARY SEARCH?
=========================
Binary Search is a highly efficient searching algorithm that operates on the 
"Divide and Conquer" principle. Instead of checking every single element one 
by one, it repeatedly divides the search interval in half. If the value of the 
search key is less than the item in the middle of the interval, the algorithm 
narrows the interval to the lower half. Otherwise, it narrows it to the upper 
half. 

Prerequisite: The array MUST be sorted before applying Binary Search.

2. HOW IT WORKS (THE MECHANISM)
===============================
Let's trace how Binary Search finds the number '7' in a sorted array of 10 elements.
Target = 7

STEP 1: Initial State
We place two pointers, 'Left' (L) at index 0, and 'Right' (R) at the last index.
We calculate 'Mid' (M) = (Left + Right) // 2 = (0 + 9) // 2 = 4.

Index:  0   1   2   3   4   5   6   7   8   9
Array: [1,  2,  2,  3,  3,  4,  5,  7,  8,  9]
        ^               ^                   ^
        L               M                   R

Condition Check: array[4] is 3. 
Is 3 == 7? No. 
Is 3 < 7? Yes! So, 7 must be on the right side. 
Action: We move L to M + 1.

STEP 2: Second Iteration
L is now at index 5. R is at index 9.
M = (5 + 9) // 2 = 7.

Index:  0   1   2   3   4   5   6   7   8   9
Array: [1,  2,  2,  3,  3,  4,  5,  7,  8,  9]
                            ^       ^       ^
                            L       M       R

Condition Check: array[7] is 7.
Is 7 == 7? Yes!
Action: TARGET FOUND! Return index 7.

Notice how we completely ignored the left half of the array after just one check.

3. THE BIG QUESTION: BINARY SEARCH VS. LINEAR SEARCH
====================================================
You asked a brilliant question: "If sorting takes O(N log N) time, why is Binary 
Search better than Linear Search which only takes O(N) time?"

Mathematically, you are right! 
If you only need to search for an item EXACTLY ONCE in an unsorted array:
  Linear Search Cost = O(N)
  Sort + Binary Search Cost = O(N log N) + O(log N) = O(N log N)
In a single-search scenario, Linear Search is actually FASTER.

SO WHY DO WE USE BINARY SEARCH? -> "The Read-Heavy Reality"
In real-world applications (like Databases, Phonebooks, User Directories), data 
is inserted or sorted VERY RARELY, but it is searched MILLIONS of times.

Imagine an array of 1,000,000 elements:
  Linear Search: 1,000,000 operations per search.
    If 100,000 users search: 1,000,000 x 100,000 = 100 Billion operations.

  Binary Search: 20 operations per search (log2(1,000,000) approx 20).
    Sort once: approx 20,000,000 operations.
    If 100,000 users search: 20 x 100,000 = 2,000,000 operations.
    Total = 22 Million operations.

Conclusion: Binary search wins massively when you have to perform MULTIPLE 
searches on the same dataset. We pay the expensive "sorting tax" once, to make 
every future search blazingly fast.

4. TIME & SPACE COMPLEXITY
==========================
TIME COMPLEXITY (How fast is it?):
  Best Case: O(1) -> If the target is exactly at the middle on the first try.
  Worst Case: O(log N) -> It halves the array until 1 element is left.
  Average Case: O(log N)

SPACE COMPLEXITY (How much memory does it use?):
  Iterative (While Loop): O(1) -> Only variables L, R, M are used. No extra memory.
  Recursive (Function Calls): O(log N) -> Each recursive call adds a frame 
  to the CPU Call Stack.

================================================================================
"""

def binary_search_recursive(array, item):

    mid =  resize_array(array, item)

    if array[mid] == item:
        return mid
    return None

def resize_array(sorted_array, item):
    
    mid = len(sorted_array) // 2

    if len(sorted_array) == 1:
        return mid
    
    elif sorted_array[mid] > item:
        return resize_array(sorted_array[:mid], item)
    
    else:
        return resize_array(sorted_array[mid:], item)


l = [1, 2, 7, 4, 3, 2, 5, 8, 9, 3]
sorted_array = sorted(l)
print(binary_search_recursive(sorted_array, 1))

def binary_search(array, item, left, right):
    if left <= right:
        # search
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            return binary_search(array, item, left, mid - 1)
        else:
            return binary_search(array, item, mid + 1, right)
    
    else:
        return None


"""
Binary Search Implementations
=============================
This module contains optimized implementations of the Binary Search algorithm,
both iterative and recursive approaches.
"""

def binary_search_iterative(array, item):
    """
    Searches for an item in a sorted array using an iterative binary search.

    Args:
        array (list): A previously sorted list of elements.
        item (int/str): The element you want to find in the array.

    Returns:
        int or None: The index of the item if it is found in the array. 
                     Returns None if the item is not present.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == item:
            return mid
            
        elif array[mid] > item:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return None


def binary_search_recursive(array, item, left, right):
    """
    Searches for an item in a sorted array using a recursive binary search.

    Args:
        array (list): A previously sorted list of elements.
        item (int/str): The element you want to find in the array.
        left (int): The starting index of the current search interval.
        right (int): The ending index of the current search interval.

    Returns:
        int or None: The index of the item if it is found in the array. 
                     Returns None if the item is not present.
    """
    # Base condition to stop recursion if item is not found
    if left > right:
        return None
        
    mid = (left + right) // 2

    if array[mid] == item:
        return mid
        
    elif array[mid] > item:
        return binary_search_recursive(array, item, left, mid - 1)
        
    else:
        return binary_search_recursive(array, item, mid + 1, right)


# ==========================================
# Testing the Functions
# ==========================================
if __name__ == "__main__":
    l = [1, 2, 7, 4, 3, 2, 5, 8, 9, 3]
    sorted_l = sorted(l)
    print(f"Sorted Array: {sorted_l}")
    
    # Testing Iterative
    print("\n--- Iterative Results ---")
    print(f"Index of 0: {binary_search_iterative(sorted_l, 0)}") # Output: None
    print(f"Index of 7: {binary_search_iterative(sorted_l, 7)}") # Output: Correct Index
    
    # Testing Recursive
    print("\n--- Recursive Results ---")
    print(f"Index of 7: {binary_search_recursive(sorted_l, 7, 0, len(sorted_l) - 1)}")


# 
# git commit -m "Refactor: optimize space complexity to O(1) using pointers and fix index return bug"