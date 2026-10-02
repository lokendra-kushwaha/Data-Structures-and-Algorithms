# ============================================================================
#                      DATA STRUCTURES: HASHING
# ============================================================================

# ----------------------------------------------------------------------------
# 1. WHY DO WE NEED HASHING? (The Quest for Speed)
# ----------------------------------------------------------------------------
# The primary goal of Hashing is to provide extremely FAST SEARCHING.
# Let's look at how searching evolved before we reached Hashing.

# --- A. LINEAR SEARCH ---
# Time Complexity: O(n)
# In Linear Search, if we want to find an element, we must check from the 
# beginning (index 0) to the end.
#
# Array:
# ---------------------------------
# | 10 | 25 |  3 |  4 | 99 |  7 |
# ---------------------------------
#   0    1     2    3    4    5 
#
# If we want to search for '4', we have to check indices 0, 1, 2, and 3. 
# If the array size doubles, the worst-case search time also doubles.

# --- B. BINARY SEARCH ---
# Time Complexity: O(log n)
# Binary Search requires the array to be SORTED. We repeatedly divide the 
# search interval in half.
#
# Sorted Array:
# ---------------------------------
# |  1 |  2 |  3 |  4 |  5 |  6 |
# ---------------------------------
#   0    1    2    3    4    5
#
# To find '5', we check the middle element, discard the left half, and search
# the right half. It is much faster than Linear Search, but can we do better?
# Can we search in O(1) time (Constant Time)? YES!


# ----------------------------------------------------------------------------
# 2. DIRECT INDEX MAPPING (The O(1) Approach & Its Flaw)
# ----------------------------------------------------------------------------
# What if we store the item at the exact index that matches its value?
# Example Items to store: {0, 1, 2, 3, 4, 5, 6}
#
# ---------------------------------------------
# |  0 |  1 |  2 |  3 |  4 |  5 |  6 |
# ---------------------------------------------
#    0    1    2    3    4    5    6    <- Indices
#
# How does this give O(1) search time?
# Arrays use a mathematical formula under the hood: 
# Target Address = Base Address + (Target Index * Size of Data Type)
# This formula is independent of the length of the array. Hence, fetching 
# an item at index 5 takes exactly the same time as index 5,000,000.

# THE PROBLEM WITH DIRECT MAPPING: MEMORY WASTAGE
# Assume we need to store these 5 items: {0, 1, 2, 3, 1000}
# To store '1000' at index 1000, we must create an array of size 1001.
#
# --------------------------------------------------------
# |  0 |  1 |  2 |  3 | NULL | NULL | ..... | 1000 |
# --------------------------------------------------------
#    0    1    2    3     4      5    .....   1000
#
# We only stored 5 items, but we wasted 996 memory blocks. This is highly 
# inefficient. We need a way to map large numbers to a small array.


# ----------------------------------------------------------------------------
# 3. THE SOLUTION: HASH FUNCTION
# ----------------------------------------------------------------------------
# A Hash Function takes a large value (Item) and converts it into a small, 
# practical index that fits within our limited array size.
#
# A simple Hash Function: h(i) = i % size (Modulo arithmetic)
#
# Let's say our Array Size = 7.
# Items to store: {15, 22, 31}
#
# Calculating Hash (Index):
# h(15) = 15 % 7 = 1
# h(22) = 22 % 7 = 1 (Wait, let's use 23 for this ideal example)
# h(23) = 23 % 7 = 2
# h(31) = 31 % 7 = 3
#
# Memory Layout (Size 7):
# ---------------------------------------------
# | NULL | 15 | 23 | 31 | NULL | NULL | NULL |
# ---------------------------------------------
#     0     1    2    3     4      5      6 
#
# When searching for 23, we simply calculate h(23) = 2. We jump to index 2 
# and find our item in O(1) time. No memory is wasted!


# ----------------------------------------------------------------------------
# 4. THE VILLAIN: COLLISION
# ----------------------------------------------------------------------------
# We want a hash function that distributes items evenly. But what happens 
# if two different items generate the SAME hash index? This is a COLLISION.
#
# Array Size = 10. Items: {14, 24}
# h(14) = 14 % 10 = 4
# h(24) = 24 % 10 = 4   <-- COLLISION! Both want to sit at index 4.
#
# Array View:
# --------------------------------------------------
# |   |   |   |   | ?? |   |   |   |   |   |
# --------------------------------------------------
#   0   1   2   3   4    5   6   7   8   9
#
# How do we handle this? There are two main techniques:
# 1. Closed Addressing (Separate Chaining)
# 2. Open Addressing (Linear Probing, Quadratic Probing, Double Hashing)


# ============================================================================
#                    COLLISION RESOLUTION TECHNIQUES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. CLOSED ADDRESSING (SEPARATE CHAINING)
# ----------------------------------------------------------------------------
# Rule: If a collision occurs, the new item MUST stay at the generated index.
# How? Instead of an array of integers, we create an array of Linked List Nodes.
# Every index acts as the "Head" of a linked list.
#
# Hash Function: h(i) = i % 10
# Items to insert: {12, 22, 45, 32}
#
# Step 1: Insert 12 (12 % 10 = 2)
# Step 2: Insert 45 (45 % 10 = 5)
# Step 3: Insert 22 (22 % 10 = 2) -> Collision at 2! Add to the chain.
# Step 4: Insert 32 (32 % 10 = 2) -> Collision at 2! Add to the chain.
#
# ASCII DIAGRAM: SEPARATE CHAINING
# 
# Index   Array of Head Pointers     Linked Lists (Chains)
#         +---------+
#   0     |  NULL   | 
#         +---------+
#   1     |  NULL   | 
#         +---------+      +----+---+      +----+---+      +----+---+
#   2     |    *---------> | 12 | *------> | 22 | *------> | 32 | *------> NULL
#         +---------+      +----+---+      +----+---+      +----+---+
#   3     |  NULL   | 
#         +---------+
#   4     |  NULL   | 
#         +---------+      +----+---+ 
#   5     |    *---------> | 45 | *------> NULL
#         +---------+      +----+---+ 
#   6-9   |  NULL   | 
#         +---------+
#
# SEARCHING IN CHAINING:
# Scenario A (Item Exists): Search for '22'
# 1. Calculate Hash: h(22) = 22 % 10 = 2
# 2. Go to Index 2.
# 3. Traverse the chain: [12] -> [22] (Found!). Time taken: O(1) + time to traverse chain.
#
# Scenario B (Item Missing): Search for '52'
# 1. Calculate Hash: h(52) = 52 % 10 = 2
# 2. Go to Index 2.
# 3. Traverse chain: [12] -> [22] -> [32] -> NULL. (Not found).
#
# FATAL FLAW & SOLUTIONS FOR CHAINING:
# If many items hash to the same index, the chain becomes a very long Linked List.
# Searching a long linked list takes O(n) time, ruining our O(1) goal!
# 
# Solutions:
# 1. REHASHING via LOAD FACTOR:
#    Load Factor (alpha) = Total Elements / Array Size.
#    If the Load Factor crosses a threshold (usually 0.75), we create a new array
#    double the size and recalculate hashes for all elements (Rehashing).
# 
# 2. BALANCED BINARY SEARCH TREE (BST):
#    Modern languages (like Java 8+ HashMap) monitor chain lengths. If a chain 
#    exceeds a certain length (e.g., 8 nodes), the Linked List is converted into a 
#    Red-Black Tree. Searching drops from O(n) worst-case to O(log n).


# ----------------------------------------------------------------------------
# 2. OPEN ADDRESSING (PROBING)
# ----------------------------------------------------------------------------
# Rule: If a collision occurs, we do NOT use linked lists. All items must sit
# directly inside the array. We look for the next available empty slot.
# Note: In Open Addressing, Array Size MUST be >= Number of Items.

# --- A. LINEAR PROBING ---
# Hash Function: g(i) = [ h(i) + k(x) ] % size
# Where: h(i) = i % size
#        k(x) = x (where x starts from 0, 1, 2, 3...) -> x is the probe count.
#
# Items: {15, 25, 35}, Size = 10
#
# 1. Insert 15:
#    x = 0 -> (15%10 + 0) % 10 = 5. (Slot 5 is empty. Inserted).
# 
# 2. Insert 25:
#    x = 0 -> (25%10 + 0) % 10 = 5. (Slot 5 is FULL! Collision).
#    x = 1 -> (25%10 + 1) % 10 = 6. (Slot 6 is empty. Inserted).
#
# 3. Insert 35:
#    x = 0 -> (35%10 + 0) % 10 = 5. (FULL)
#    x = 1 -> (35%10 + 1) % 10 = 6. (FULL)
#    x = 2 -> (35%10 + 2) % 10 = 7. (Slot 7 is empty. Inserted).
#
# ASCII DIAGRAM: LINEAR PROBING ARRAY
# -------------------------------------------------------
# |    |    |    |    |    | 15 | 25 | 35 |    |    |
# -------------------------------------------------------
#   0    1    2    3    4    5    6    7    8    9
#
# PROBLEM WITH LINEAR PROBING: "PRIMARY CLUSTERING"
# Items tend to cluster together in one part of the array. If a cluster forms,
# new items colliding there have to step through the entire cluster one by one
# to find an empty spot. This severely degrades performance.


# --- B. QUADRATIC PROBING ---
# To solve the "Primary Clustering" of Linear Probing, we change how we skip slots.
# Instead of stepping by 1, 2, 3... we step by squares: 1, 4, 9, 16...
# This throws the colliding element far away, preventing clusters from growing.
#
# Hash Function: g(i) = [ h(i) + k(x) ] % size
# Where: k(x) = x^2 (where x = 0, 1, 2, 3...)
#
# Items: {15, 25, 35}, Size = 10
#
# 1. Insert 15:
#    x = 0 -> (15%10 + 0^2) % 10 = 5. (Inserted at 5).
#
# 2. Insert 25:
#    x = 0 -> (25%10 + 0^2) % 10 = 5. (Collision!)
#    x = 1 -> (25%10 + 1^2) % 10 = 6. (Inserted at 6).
#
# 3. Insert 35:
#    x = 0 -> (35%10 + 0^2) % 10 = 5. (Collision!)
#    x = 1 -> (35%10 + 1^2) % 10 = 6. (Collision at 6!)
#    x = 2 -> (35%10 + 2^2) % 10 = (5 + 4) % 10 = 9. (Inserted at 9).
#
# ASCII DIAGRAM: QUADRATIC PROBING ARRAY
# -------------------------------------------------------
# |    |    |    |    |    | 15 | 25 |    |    | 35 |
# -------------------------------------------------------
#   0    1    2    3    4    5    6    7    8    9
#
# Notice how '35' jumped directly to index 9 instead of sitting at 7. 
# This breaks the cluster! 
# 
# SEARCHING IN QUADRATIC PROBING:
# Search for '35':
# x = 0 -> index 5 (Found 15. Not our item).
# x = 1 -> index 6 (Found 25. Not our item).
# x = 2 -> index 9 (Found 35. Match!). 
#
# (Note: Quadratic probing solves Primary Clustering but can suffer from 
# Secondary Clustering, which is solved by Double Hashing - using a second 
# hash function to determine the step size).

# ============================================================================
#                               SUMMARY
# ============================================================================
# 1. Arrays give O(1) access by index, but using values as indices wastes memory.
# 2. Hash Functions map large values to small array indices.
# 3. Collisions happen when two values map to the same index.
# 4. Chaining solves collisions using Linked Lists (Nodes) at each index.
#    - Long chains cause O(n) delay. Solved by Rehashing or BSTs.
# 5. Open Addressing keeps all data in the array.
#    - Linear Probing steps by +1. Causes Primary Clustering.
#    - Quadratic Probing steps by +x^2. Solves Primary Clustering.
# ============================================================================


# ============================================================================
#            BUILDING A CUSTOM DICTIONARY (HASH MAP) FROM SCRATCH
# ============================================================================
# HOW IT WORKS:
# Python's built-in `dict` uses Hash Tables under the hood. Here, we are 
# recreating that exact behavior using OPEN ADDRESSING with LINEAR PROBING.
#
# STRATEGY - PARALLEL ARRAYS:
# Instead of storing nodes (like in chaining), we use two parallel arrays 
# of the exact same size:
# 1. `self.slots` -> Stores the KEYS
# 2. `self.data`  -> Stores the corresponding VALUES
#
# ASCII VISUALIZATION:
# Index:      0         1         2
#          +--------+--------+--------+
# slots -> | 'java' |'python'| 'c++'  |   <-- (Keys are hashed to find index)
#          +--------+--------+--------+
# data  -> |   45   |   45   |  450   |   <-- (Values sit at the exact same index)
#          +--------+--------+--------+
# 
# COLLISION RESOLUTION (LINEAR PROBING):
# If a key hashes to an index that is already occupied by a different key, 
# we simply move to the next available index (Index + 1). If we reach the end 
# of the array, we wrap around to index 0 using the modulo (%) operator.
# ============================================================================

class Dictionary:
    """
    A Custom Dictionary class implemented using a Hash Table with Linear Probing.
    """

    def __init__(self, size):
        """
        Initializes the custom dictionary with a fixed size.
        
        Args:
            size (int): The maximum number of key-value pairs the dictionary can hold.
        """
        self.size = size
        # Array to store the keys
        self.slots = [None] * self.size
        # Array to store the values
        self.data = [None] * self.size

    def hash_function(self, key):
        """
        Generates an array index for a given key.
        Uses Python's built-in hash() and limits it within array boundaries.
        """
        return abs(hash(key)) % self.size

    def rehash(self, old_hash):
        """
        Resolves collisions using Linear Probing.
        Moves to the very next slot (step size = +1). Wraps around if at the end.
        """
        return (old_hash + 1) % self.size

    def put(self, key, value):
        """
        Inserts a key-value pair into the dictionary. 
        Updates the value if the key already exists.
        """
        hash_value = self.hash_function(key)

        # CASE 1: The slot is completely empty. Direct insertion.
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
            
        else:
            # CASE 2: The slot is occupied, but it's the SAME key. Update value.
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
                
            # CASE 3: COLLISION! The slot is occupied by a DIFFERENT key.
            else:
                new_hash_value = self.rehash(hash_value)
                
                # Probe (loop) until we find an EMPTY slot OR the EXACT SAME key
                while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                    
                    # Safety condition: If we complete a full circle, the array is full!
                    if new_hash_value == hash_value:
                        raise Exception("Dictionary is completely full! Cannot insert new items.")

                # If we found an empty slot during probing
                if self.slots[new_hash_value] is None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                # If we found the exact key during probing (Update scenario)
                else:
                    self.data[new_hash_value] = value

    def get(self, key):
        """
        Retrieves the value for a given key.
        Raises a KeyError if the key does not exist in the dictionary.
        """
        start_position = self.hash_function(key)
        current_position = start_position

        # Probe through the slots until we hit an empty space (None)
        while self.slots[current_position] is not None:
            
            # Match found! Return the corresponding value from the data array.
            if self.slots[current_position] == key:
                return self.data[current_position]

            # Not a match. Keep probing linearly.
            current_position = self.rehash(current_position)

            # If we probed all the way around and reached the start position, it doesn't exist.
            if current_position == start_position:
                raise KeyError(f"Key not found: '{key}'")
        
        # If we hit a 'None' slot, the chain is broken. The key doesn't exist.
        raise KeyError(f"Key not found: '{key}'")

    def __setitem__(self, key, value):
        """
        Magic method to allow dictionary assignment syntax: d[key] = value
        """
        self.put(key, value)

    def __getitem__(self, key):
        """
        Magic method to allow dictionary retrieval syntax: print(d[key])
        """
        return self.get(key)

    def __str__(self):
        """
        String representation of the dictionary. Prints exactly like Python's built-in dict.
        Example output: {'python': 45, 'java': 45}
        """
        res = ''
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                # Formatting as " 'key': value, "
                res += f"'{self.slots[i]}': {self.data[i]}, "
                
        # Removing the trailing comma and space
        if len(res) > 0:
            res = res[:-2]
            
        return '{' + res + '}'


# ============================================================================
#                              TESTING THE CODE
# ============================================================================
if __name__ == "__main__":
    # Initialize dictionary with max size 3
    d1 = Dictionary(3)

    print("--- Initial State ---")
    print("Slots Array:", d1.slots)
    print("Data Array:", d1.data)

    print("\n--- Inserting Items ---")
    d1['python'] = 45   # Using __setitem__ magic method
    print("Added 'python':", d1.data)

    d1['java'] = 45
    print("Added 'java':  ", d1.data)

    d1['c++'] = 450
    print("Added 'c++':   ", d1.data)

    print("\n--- Fetching Items ---")
    print("Value for 'python':", d1['python'])  # Using __getitem__ magic method
    print("Value for 'java':  ", d1.get('java'))

    print("\n--- Final Dictionary State ---")
    print(d1)  # Using __str__ magic method

    print("\n--- Testing Error Handling (KeyError) ---")
    try:
        print(d1.get('php'))
    except KeyError as e:
        print(f"Successfully caught error -> {type(e).__name__}: {e}")