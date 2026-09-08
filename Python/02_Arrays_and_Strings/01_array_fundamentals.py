# ============================================================================
# 1. INTRODUCTION TO DATA STRUCTURES
# ============================================================================

# What is a Data Structure?
# It is a specialized format for organizing, processing, retrieving, and 
# storing data efficiently in computer memory. 

# Why do we need them?
# In Computer Science, there are certain complex problems (like searching 
# massive databases or routing algorithms). Data structures provide optimized 
# solutions to these problems, drastically reducing time and memory overhead.

# ============================================================================
# CLASSIFICATION OF DATA STRUCTURES
# ============================================================================

# 1. Linear Data Structures
# Data elements are arranged sequentially, one after the other. 
# Examples: Arrays, Linked Lists, Stacks, Queues, Hashing.

# Visualizing an Array:
# -----------------
# | 2 | 3 | 4 | 5 |    
# -----------------
#  701 705 709 713  (Memory Addresses)

# Visualizing a Linked List:
#       Head
#        |
#  -----------              -----------              -----------              ------------
#  | 2 | 613 |   ----->     | 3 | 707 |   ----->     | 4 | 905 |   ----->     | 5 | None |
#  -----------              -----------              -----------              ------------
#      501                      613                      707                      905
#  (Base Addr)              (Next Addr)              (Next Addr)                (Tail)


# 2. Non-Linear Data Structures
# Data elements are not placed sequentially. Elements are connected in a 
# hierarchical or network-like manner.
# Examples: Trees, Graphs.

# Visualizing a Tree (Hierarchical):
#           [Root: 10]
#            /      \
#         [5]        [15]
#        /   \         \
#      [2]   [7]       [20]

# Visualizing a Graph (Network):
#      [A] ------- [B]
#       |  \        |
#       |     \     |
#       |        \  |
#      [C] ------- [D]

# ============================================================================
# 2. DEEP DIVE: ARRAYS
# ============================================================================

# An Array is a linear data structure used to store multiple items of the 
# SAME data type in CONTINUOUS (contiguous) memory locations.

# The Mathematical Engine of Arrays:
# Because memory is continuous, arrays fetch data instantly using a simple formula:
# Target Address = Base_Address + (Index * Item_Size)

# Note: Storing raw data directly inside these continuous blocks is referred 
# to as "Call by Value".

# Disadvantages of Standard (Static) Arrays:
# 1. Fixed Size: You must declare the size beforehand. Causes memory wastage.
# 2. Homogeneous: Lacks flexibility (cannot store strings and ints together).

# ============================================================================
# 3. THE SOLUTION: REFERENTIAL ARRAYS
# ============================================================================

# How do we store different data types in a single array (like Python Lists)? 
# Solution: We don't store actual data in the array. We store the data randomly 
# in the memory, and store their Memory Addresses (Pointers) inside the array.

# Step 1: Data stored randomly in memory
#  [Value: 2]   [Value: 3]   [Value: "hello"]   [Value: 5]
#  Addr: 720    Addr: 403      Addr: 104        Addr: 503

# Step 2: The Referential Array (Storing Pointers)
# -------------------------
# | 720 | 403 | 104 | 503 |  <-- Remains homogeneous (holds integer addresses)
# -------------------------
#   701   705   709   713    <-- Continuous memory of the array itself

# Note: This architecture is known as "Call by Reference".

# Pros & Cons of Referential Arrays:
# Advantage: Extreme flexibility. Can mix integers, strings, and objects.
# Disadvantage: Slower speed (pointer indirection) and extra memory consumption.

# ============================================================================
# 4. SOLVING THE FIXED SIZE PROBLEM: DYNAMIC ARRAYS
# ============================================================================

# A Dynamic Array resizes itself. Under the hood, it is still a static array, 
# but it uses a clever memory reallocation trick.

# Visualizing Dynamic Reallocation (How it grows):
# Step 1: Initial Array (Size 2) gets full.
# [ 2 | 3 ] (Full!)

# Step 2: Python creates a NEW, larger array in a different memory location (Size 4).
# [   |   |   |   ] 

# Step 3: Copies old elements to the new array.
# [ 2 | 3 |   |   ]

# Step 4: Destroys the old array and appends the new element.
# [ 2 | 3 | 4 |   ] <-- Ready for more data!

# ============================================================================
# PROVING PYTHON LISTS ARE DYNAMIC ARRAYS (CODE)
# ============================================================================

def prove():
    import sys

    L = []

    # Checking the initial size of an empty list structure in bytes
    print(f"Size of an empty list: {sys.getsizeof(L)} bytes") 

    print("\nAppending items and monitoring memory block jumps:")
    for i in range(10):
        L.append(i) # Appending items one by one
        
        # Checking the size after appending each item
        # Observe how memory jumps in chunks rather than increasing linearly
        print(f"Items: {i + 1} | Memory Size: {sys.getsizeof(L)} bytes")

    # Final size of the list
    print(f"\nFinal size after all appends: {sys.getsizeof(L)} bytes\n")


import ctypes

class MyList:
    """
    A highly optimized, hybrid custom list implementation in Python.

    This class acts as a drop-in replacement for the built-in Python list but 
    offers advanced memory control, acting as either a C-style strict static array 
    or a Python-style dynamic array. It features strict type safety, memory 
    shrinking, and automatic resizing based on CPU-efficient growth algorithms.

    Attributes:
        dtype (type, optional): The allowed data type for the list (e.g., int, str). 
            If None, the list accepts mixed data types.
        size (int): The current memory capacity allocated for the array.
        is_fixed (bool): Flag indicating if the array has a fixed capacity.
        n (int): The actual number of elements currently stored in the array.
        A (ctypes.py_object): The underlying C-level array storing the data.
    """

    def __init__(self, *args, capacity=None, dtype=None):
        """
        Initializes the custom list.

        Args:
            *args: Variable length argument list to pre-populate the array.
            capacity (int, optional): Fixed size of the array. If provided, 
                the array becomes a strict C-style static array.
            dtype (type, optional): Enforces strict type checking (e.g., int).

        Raises:
            MemoryError: If initial *args exceed the provided fixed capacity.
            TypeError: If initial *args do not match the specified dtype.
        """
        self.dtype = dtype

        # Determine if the list is fixed-size or dynamic
        if capacity is not None:
            self.size = capacity
            self.is_fixed = True
        else:
            # Prevent the Zero-Capacity Trap by allocating at least 1 block
            self.size = max(len(args), 1)
            self.is_fixed = False

        self.n = 0
        # Allocate the underlying C array
        self.A = self.__create_array(self.size)

        # Pre-populate the array with any provided *args
        for item in args:
            self.append(item)

    def __create_array(self, capacity):
        """
        Creates a raw C-level array.

        Args:
            capacity (int): The number of memory slots to allocate.

        Returns:
            A ctypes.py_object array of the specified capacity.
        """
        # Creates a C type array(static, referencial) with size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """Returns the actual number of elements in the list."""
        return self.n

    def __str__(self):
        """Returns a string representation of the list (e.g., [1, 2, 3])."""
        if self.n == 0:
            return '[]'
            
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ', '

        # Slice out the trailing comma and space for clean output
        return '[' + result[:-2] + ']'

    def __getitem__(self, index):
        """
        Retrieves an item or a slice of items from the list.

        Args:
            index (int or slice): The index or slice range to fetch.

        Returns:
            The item at the specified index, or a new MyList containing the slice.

        Raises:
            IndexError: If the index is out of bounds.
        """
        # Handle slicing (e.g., my_list[1:4:2])
        if isinstance(index, slice):
            start, stop, step = index.indices(self.n)
            
            result = MyList() 
            for i in range(start, stop, step):
                result.append(self.A[i])
            return result
            
        # Handle standard and negative indexing (e.g., my_list[2] or my_list[-1])
        elif isinstance(index, int):
            if index < 0:
                index = self.n + index
                
            if index < 0 or index >= self.n:
                raise IndexError("Index out of range") 
                
            return self.A[index]

    def __delitem__(self, pos):
        """
        Deletes an item at the specified position and optimizes memory.

        Args:
            pos (int): The index of the item to delete.
        """
        if 0 <= pos < self.n:
            # Shift all elements to the left to fill the memory gap
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]

            self.n = self.n - 1
            
            # Trigger automatic memory shrinking to prevent RAM leaks
            self.__shrink()

    def __add__(self, other):
        """
        Concatenates this list with another MyList.

        Args:
            other (MyList): The other list to append to this one.

        Returns:
            MyList: A completely new list containing elements from both objects.
        """
        result = MyList()
        
        # Copy elements from the first array
        for i in range(self.n):
            result.append(self.A[i])
            
        # Copy elements from the second array
        for i in range(other.n):
            result.append(other.A[i])
            
        return result

    def __iter__(self):
        """Initializes the iterator for the list."""
        self._iter_index = 0
        return self

    def __next__(self):
        """
        Returns the next item in the list during iteration.

        Raises:
            StopIteration: When all items have been traversed.
        """
        if self._iter_index < self.n:
            result = self.A[self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration
    
    def append(self, item):
        """
        Appends a single item to the end of the list.

        Args:
            item: The element to add.

        Raises:
            TypeError: If dtype is set and the item's type does not match.
            MemoryError: If the list is fixed-size and already full.
        """
        # Type enforcement
        if self.dtype is not None and not isinstance(item, self.dtype):
            raise TypeError(f"Invalid type! This list only accepts {self.dtype.__name__}.")

        # Capacity check and dynamic resizing
        if self.n == self.size:
            if getattr(self, 'is_fixed', False):
                raise MemoryError("Fixed capacity reached! Cannot append more items.")
            else:
                new_capacity = max(int(self.size * 1.5), self.size + 1)
                self.__resize(new_capacity)

        self.A[self.n] = item
        self.n += 1

    def pop(self):
        """
        Removes and returns the last item from the list.

        Returns:
            The last item in the array.

        Raises:
            IndexError: If the list is empty.
        """
        if self.n == 0:
            raise IndexError("pop from empty list")

        val = self.A[self.n - 1]
        self.n -= 1

        # Trigger auto-shrinking to free up RAM
        self.__shrink()

        return val
    
    def clear(self):
        """Empties the list and resets internal element count."""
        self.n = 0
        # Note: We do not shrink capacity to 1 here immediately. 
        # The next shrink trigger or append will optimize it naturally.

    def find(self, item):
        """
        Finds the first occurrence of an item.

        Args:
            item: The element to search for.

        Returns:
            int: The index of the item.

        Raises:
            ValueError: If the item is not found in the list.
        """
        for i in range(self.n):
            if self.A[i] == item:
                return i
                
        raise ValueError(f"{item} is not in list")

    def insert(self, pos, item):
        """
        Inserts an item at a specific position.

        Args:
            pos (int): The index where the item should be inserted.
            item: The element to insert.
            
        Raises:
            MemoryError: If the list is fixed-size and already full.
        """
        if self.n == self.size:
            if getattr(self, 'is_fixed', False):
                raise MemoryError("Fixed capacity reached! Cannot insert more items.")
            else:
                new_capacity = max(int(self.size * 1.5), self.size + 1)
                self.__resize(new_capacity)

        # Shift items to the right to make space
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        self.A[pos] = item
        self.n += 1

    def remove(self, item):
        """
        Removes the first occurrence of an item.

        Args:
            item: The element to remove.
            
        Raises:
            ValueError: If the item is not present.
        """
        pos = self.find(item) # find() raises ValueError naturally if not found
        self.__delitem__(pos)
            
    def sum(self):
        """
        Calculates the sum of all elements in the list.
        
        Returns:
            The total sum (numeric types expected).
        """
        total = 0
        for i in range(self.n):
            total += self.A[i]
        return total

    def max(self):
        """
        Finds the maximum value in the list.

        Returns:
            The largest element.

        Raises:
            ValueError: If the list is empty.
        """
        if self.n == 0:
            raise ValueError("max() arg is an empty sequence")
            
        max_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_val:
                max_val = self.A[i]
        return max_val

    def min(self):
        """
        Finds the minimum value in the list.

        Returns:
            The smallest element.

        Raises:
            ValueError: If the list is empty.
        """
        if self.n == 0:
            raise ValueError("min() arg is an empty sequence")
            
        min_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] < min_val:
                min_val = self.A[i]
        return min_val

    def sort(self):
        """
        Sorts the list in ascending order in-place (Bubble Sort logic).

        Returns:
            self: For method chaining.
        """
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.A[i] > self.A[j]:
                    self.A[i], self.A[j] = self.A[j], self.A[i]
        return self

    def extend(self, other):
        """
        Extends the list by appending all items from an iterable.

        Args:
            other (iterable): The collection containing items to be added.

        Returns:
            self: For method chaining.
        """
        for i in other: # Naturally uses __iter__ under the hood
            self.append(i)
        return self

    def __resize(self, new_capacity):
        """
        Internal method to reallocate memory blocks.

        Args:
            new_capacity (int): The new memory size to allocate.
        """
        B = self.__create_array(new_capacity)
        self.size = new_capacity
        
        # Transfer data to the new memory block
        for i in range(self.n):
            B[i] = self.A[i]
            
        self.A = B

    def __shrink(self):
        """Internal method to reduce memory footprint when the array is mostly empty."""
        if getattr(self, 'is_fixed', False):
            return

        if self.n <= self.size // 2 and self.size > 1:
            new_capacity = max(int(self.size / 1.5), 1)
            self.__resize(new_capacity)


if __name__ == "__main__":

    # ==========================================
    # TEST 1: Proving Python list is a Dynamic Array
    # ==========================================
    prove()

    # ==========================================
    # TEST 2: Basic Operations & Mixed Types
    # ==========================================
    print("--- TEST 1: Basics ---")
    L = MyList()
    L.append('Hello')
    L.append(3.4)
    L.append(True)
    L.append(45)

    print(f"Length: {len(L)}")         # Expected: 4
    print(f"List: {L}")                # Expected: ['Hello', 3.4, True, 45]
    print(f"Index 0: {L[0]}")          # Expected: Hello
    print(f"Index 1: {L[1]}")          # Expected: 3.4


    # ==========================================
    # TEST 3: Deletion & Memory Shrinking
    # ==========================================
    print("\n--- TEST 2: Pop & Clear ---")
    print(f"Popped: {L.pop()} -> Current List: {L}")
    print(f"Popped: {L.pop()} -> Current List: {L}")
    print(f"Popped: {L.pop()} -> Current List: {L}")
    print(f"Popped: {L.pop()} -> Current List: {L}")

    L.clear()
    print(f"After clear(): {L}")       # Expected: []


    # ==========================================
    # TEST 4: Insertion & Searching
    # ==========================================
    print("\n--- TEST 3: Insert & Find ---")
    L.append('Hello')
    L.append(True)
    L.insert(0, 0)
    print(f"After insert at 0: {L}")   # Expected: [0, 'Hello', True]

    print(f"Find 'Hello': Index {L.find('Hello')}")
    print(f"Find True: Index {L.find(True)}")

    # Error Handling Test for Find
    try:
        L.find('1000')
    except ValueError as e:
        print(f"Find Error Caught: {e}")  # Expected to catch ValueError


    # ==========================================
    # TEST 5: Index & Removal Error Handling
    # ==========================================
    print("\n--- TEST 4: Error Handling ---")
    try:
        del L[300]
    except IndexError as e:
        print(f"Del Error Caught: {e}")   # Expected: Index out of range

    try:
        L.remove('World')
    except ValueError as e:
        print(f"Remove Error Caught: {e}") # Expected: 'World' is not in list


    # ==========================================
    # TEST 6: Math Operations & Sorting
    # ==========================================
    print("\n--- TEST 5: Math & Sort ---")
    L2 = MyList()
    L2.extend([1, 1, 20, 120, 20.1, 20.1, -20, -2000])

    print(f"L2 List: {L2}")
    print(f"Sum: {L2.sum()}")
    print(f"Max: {L2.max()}")
    print(f"Min: {L2.min()}")
    print(f"Sorted: {L2.sort()}")


    # ==========================================
    # TEST 7: Advanced Operations (Concat, Negative Index, Iteration)
    # ==========================================
    print("\n--- TEST 6: Advanced Dunder Methods ---")
    L.extend(L2)
    print(f"L extended with L2: {L}")

    print(f"L + L2: {L + L2}")

    print(f"Negative Index L[-5]: {L[-5]}")

    print("Iterating over L2:")
    for i in L2:
        print(i, end=" | ")
    print()


    # ==========================================
    # TEST 8: Initialization, *args, and Strict Type Safety
    # ==========================================
    print("\n--- TEST 7: Constructor Features ---")
    # Testing List Comprehension unrolling
    l3 = MyList(*[i for i in range(10)])
    print(f"Unpacked Generator: {l3}")

    # Testing strict arrays (Fixed size + Typed)
    l4 = MyList(2, 3, 4, 8, 7, capacity=5, dtype=int)
    print(f"Strict Fixed-Type Array: {l4}")

    try:
        l4.append(9)
    except MemoryError as e:
        print(f"Strict Array Capacity Blocked: {e}")

    try:
        l5 = MyList(1, 2, dtype=str)
    except TypeError as e:
        print(f"Strict Array Type Blocked: {e}")
