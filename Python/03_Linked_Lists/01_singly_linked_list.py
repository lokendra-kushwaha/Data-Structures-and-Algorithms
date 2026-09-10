# ============================================================================
# 1. INTRODUCTION TO LINKED LISTS
# ============================================================================

# What is a Linked List?
# A Linked List is a linear data structure used to store data in NON-CONTINUOUS 
# memory locations. In many computational cases, it acts as a highly optimized 
# replacement for standard Arrays.

# How does it work?
# A Linked List is simply a chain of independent "Nodes" scattered across the memory (Collection of nodes).

# What is a Node?
# A Node is a structural object that contains exactly two compartments:
# 1. Data: The actual information you want to store (integers, strings, objects).
# 2. Address (Pointer): The exact memory location of the "next" Node in the chain.

# ============================================================================
# VISUALIZING THE NODES
# ============================================================================

# Step 1: Two Independent Nodes in Memory
#   Node 1                    Node 2
# ------------              ------------      
# | 2 | None |              | 3 | None |             
# ------------              ------------                
#    501                         613       <-- Memory addresses of the nodes     

# Step 2: Connecting the Nodes (Forming a List)
#  Node 1.                    Node 2.
# -----------               ------------      
# | 2 | 613 |  -------->    | 3 | None |   <-- A linked List Containing two nodes      
# -----------               ------------                
#    501                        613 
#     |                          |
#    Head                       Tail -> Address -> None 

# Step 3: A Full Linked List (Connecting 4 Nodes)
# -----------              -----------                  -----------                ------------
# | 2 | 613 |  --------->  | 3 | 707 |  ------------->  | 4 | 905 |  ----------->  | 5 | None |
# -----------              -----------                  -----------                ------------
#    501                      613                          707                        905
#     |                                                                                |
#    Head                                                                             Tail (Address - None: This is the identity of tail)

# ============================================================================
# 2. WHY USE A LINKED LIST? (ARRAY VS. LINKED LIST)
# ============================================================================

# If we already have Arrays, why learn Linked Lists? The answer lies in the 
# Time Complexity of "Write" operations (Insertion and Deletion).

# ---------------------------------------------------------
# THE ARRAY PROBLEM: The O(n) Shifting Nightmare
# ---------------------------------------------------------
# Arrays store data in continuous memory blocks. If you have an array with 10 Million 
# items and you want to insert or delete an item at the very beginning, you MUST shift 
# the remaining 9,999,999 items one by one. This takes O(n) time.

# Diagram: Inserting '99' at index 1 in an Array
# Initial:  | 2 | 3 | 4 | 5 |
# Step 1:   | 2 |   | 3 | 4 | 5 |  <-- Shift everything right (Heavy CPU usage)
# Step 2:   | 2 | 99| 3 | 4 | 5 |  <-- Finally insert the data

# ---------------------------------------------------------
# THE LINKED LIST SOLUTION: The O(1) Pointer Hack
# ---------------------------------------------------------
# Because Linked Lists do not require continuous memory, we NEVER shift items. 
# To insert or delete a node, we simply "break" the old connection and point it 
# to the new address. This takes O(1) constant time!

# Diagram: Inserting '99' between Node '2' and Node '3'
# Before:   [2] --------> [3] --------> [4]
#
# Action:   1. Create Node [99]
#           2. Point [99] to [3]
#           3. Point [2] to [99]
#
# After:    [2]           [3] --------> [4]
#             \          /
#              -> [99] -> 

# ============================================================================
# SUMMARY OF DIFFERENCES
# ============================================================================

# 1. Memory Layout: Array is continuous (But we can solve this, which we also did by creating a dynamic array); Linked List is scattered (non-continuous).
# 2. Write Operations (Insert/Delete): Array is slow O(n); Linked List is blazing fast O(1).
# 3. Memory Wastage: Dynamic arrays over-allocate (wasting space); Linked Lists only 
#    consume exactly what they need per node.
# 4. Read Operations (Searching): Array is fast O(1) using math (Base + Index * Size); 
#    Linked List is slow O(n) because you must traverse node by node.
# 5. Linked List can be used to create other data structures -> stacks, queues, doubly linked lists, circular linked list

# ============================================================================
# 3. CORE IMPLEMENTATION: BUILDING AND CONNECTING NODES
# ============================================================================

class Node:
    """The fundamental building block of a Linked List."""
    def __init__(self, value):
        self.data = value
        self.next = None  # Pointer to the next node (defaults to None)

if __name__ == "__main__":
    # 1. Instantiating isolated nodes in the memory
    #    Node 1                   Node 2                      Node 3                    Node 4
    # ------------             ------------                ------------             ------------
    # | 1 | None |             | 2 | None |                | 3 | None |             | 4 | None |
    # ------------             ------------                ------------             ------------
    #    144                      128                           448                       440
    a = Node(1)
    # Memory: [1 | None] at approx Address 144
    
    b = Node(2)
    # Memory: [2 | None] at approx Address 128
    
    c = Node(3)
    # Memory: [3 | None] at approx Address 448
    
    d = Node(4)
    # Memory: [4 | None] at approx Address 440

    print("=== EXTRACTING NODE DATA ===")
    print(f"Node A data: {a.data}")
    print(f"Node B data: {b.data}")
    
    print("\n=== VERIFYING SCATTERED MEMORY LOCATIONS ===")
    print(f"Address of A: {id(a)}")
    print(f"Address of B: {id(b)}")
    print(f"Address of C: {id(c)}")
    print(f"Address of D: {id(d)}")

    # 2. Hacking the Pointers: Connecting the Nodes manually
    a.next = b
    b.next = c
    c.next = d

    # The Architecture after connection:
    # ------------            ------------              ------------            ------------
    # | 1 | 128  |  ------->  | 2 | 448  |   ------->   | 3 | 440  |  ------->  | 4 | None |
    # ------------            ------------              ------------            ------------
    #    144                      128                       448                     440
    #     |                                                                          |
    #   Head                                                                Tail -> Address -> None

    print("\n=== VERIFYING THE CONNECTIONS ===")
    print(f"Node A's next pointer points to -> {id(a.next)} (Matches B's ID!)")
    print(f"Node B's next pointer points to -> {id(b.next)} (Matches C's ID!)")
    print(f"Node D's next pointer points to -> {d.next} (End of the line)")


"""
=============================================================================
Data Structures & Algorithms - Singly Linked List
=============================================================================
A foundational implementation of a Singly Linked List in pure Python.
This module demonstrates low-level memory pointer manipulation, dynamic 
node linking, and custom iterator mechanics without relying on built-in 
Python list structures.
=============================================================================
"""

class Node:
    """
    A fundamental memory block for the Singly Linked List.
    
    Attributes:
        data (Any): The value or data stored within the node.
        next (Node | None): A pointer to the next Node in the sequence. 
                            Defaults to None for a newly created node.
    """
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    """
    A manager class that orchestrates Node objects to form a sequence.
    Maintains the head pointer and tracking the total number of nodes dynamically.
    
    Attributes:
        head (Node | None): Pointer to the first node in the list.
        n (int): The current total count of nodes in the list.
    """
    def __init__(self):
        # Empty Linked List -> 0 Nodes (Head = None)
        self.head = None
        self.n = 0

    def __len__(self):
        """
        Retrieves the total number of nodes in the linked list.
        
        Time Complexity: O(1) - Because we maintain the self.n counter.
        
        Returns:
            int: The size of the linked list.
        """
        return self.n

    def __str__(self):
        """
        Generates a visually readable string representation of the linked list.
        Format: "val1 -> val2 -> val3"
        
        Time Complexity: O(N) - Must visit every node to extract its data.

        Returns:
            str: The formatted string displaying the node sequence.
        """
        curr = self.head
        result = ''
        
        while curr is not None:
            result += str(curr.data) + ' -> '
            curr = curr.next

        # Slicing [:-3] removes the trailing ' -> '
        return result[:-3] 

    def __iter__(self):
        """
        Initializes the iteration protocol, allowing 'for loops' to work natively.
        Uses a temporary pointer to protect the main head pointer.
        
        Returns:
            LinkedList: The iterable object itself.
        """
        self._current_node = self.head
        return self

    def __next__(self):
        """
        Moves the temporary pointer forward and retrieves data progressively.
        
        Raises:
            StopIteration: When the pointer reaches the end (None) of the list.

        Returns:
            Any: The data from the current node in the iteration sequence.
        """
        if self._current_node is None:
            raise StopIteration
            
        result = self._current_node.data
        self._current_node = self._current_node.next
        
        return result

    # =====================================================================
    # INSERTION & MODIFICATION METHODS
    # =====================================================================

    def insert_head(self, value):
            """
            Inserts a new node at the very beginning of the linked list.
            
            Time Complexity: O(1) - Direct pointer reassignment without traversal.
    
            Args:
                value (Any): The data to be stored in the new head node.
            """
            new_node = Node(value)
            new_node.next = self.head  # Connect new node to the current head
            self.head = new_node       # Reassign head pointer to the new node
            self.n += 1                # Increment node counter
    
    def append(self, value):
        """
        Appends a new node to the very end of the linked list.
        
        Time Complexity: O(N) - Requires traversing the entire list to find the tail.

        Args:
            value (Any): The data to be stored in the new tail node.
        """
        new_node = Node(value)
        
        # Edge Case: If the list is completely empty
        if self.head is None:
            self.head = new_node
            self.n += 1
            return

        # Traversal to find the last node
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        # Connect the last node to the new node
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        """
        Inserts a new node immediately after the first occurrence of a specific value.
        
        Time Complexity: O(N) - Must search for the target value node.

        Args:
            after (Any): The target value after which the new node will be inserted.
            value (Any): The data to be stored in the newly inserted node.
            
        Raises:
            ValueError: If the 'after' target value is not found in the list.
        """
        new_node = Node(value)
        curr = self.head

        # Traverse to find the target node
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        # Case 1: Target value found (curr is not None)
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        # Case 2: Loop finished but target value was never found
        else:
            raise ValueError('Target item not found in the linked list.')

    def clear(self):
        """
        Completely empties the linked list.
        
        Time Complexity: O(1) - Python's Garbage Collector automatically handles 
        the disconnected nodes in memory once the head is severed.
        """
        self.head = None
        self.n = 0

    # =====================================================================
    # DELETION METHODS
    # =====================================================================

    def delete_head(self):
        """
        Removes the first node (head) from the linked list.
        
        Time Complexity: O(1) - Direct pointer reassignment.

        Raises:
            IndexError: If the linked list is already empty.
        """
        if self.head is None:
            raise IndexError("Cannot delete head from an empty linked list")
        
        # Move head pointer to the second node, severing the first
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        """
        Removes the last node (tail) from the linked list.
        
        Time Complexity: O(N) - Must traverse to the second-to-last node.

        Raises:
            IndexError: If the linked list is already empty.
        """
        if self.head is None:
            raise IndexError("pop from empty linked list")

        curr = self.head

        # Case: If there is only one node in the list
        if curr.next is None:
            self.delete_head()
            return

        # Traverse to the second-to-last node
        while curr.next.next is not None:
            curr = curr.next

        # Sever the connection to the last node
        curr.next = None
        self.n -= 1

    def remove(self, value):
        """
        Removes the first occurrence of a specific value from the linked list.
        
        Time Complexity: O(N) - Must traverse to find the target value.

        Args:
            value (Any): The data value to be removed.

        Raises:
            ValueError: If the list is empty or the item is not found.
        """
        if self.head is None:
            raise ValueError(f"LinkedList.remove(x): {value} not in list")

        # Case: If the item to be removed is at the head
        if self.head.data == value:
            self.delete_head()
            return

        curr = self.head

        # Traverse, looking one node ahead (curr.next.data) to maintain the link
        while curr.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        # Case 1: Item not found (reached the end)
        if curr.next is None:
            raise ValueError(f"LinkedList.remove(x): {value} not in list")
        # Case 2: Item found, bypass it to remove it from the chain
        else:
            curr.next = curr.next.next
            self.n -= 1

    # =====================================================================
    # SEARCH & ACCESS METHODS
    # =====================================================================

    def search(self, item):
        """
        Searches for a specific value and returns its position (index) in the list.
        
        Time Complexity: O(N) - Linear search through the nodes.

        Args:
            item (Any): The target data value to find.

        Raises:
            ValueError: If the target item is not present in the linked list.

        Returns:
            int: The index position (0-based) of the item.
        """
        curr = self.head
        pos = 0

        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1

        raise ValueError(f"{item} is not in linked list")

    def __getitem__(self, index):
        """
        Magic method to access list items using bracket notation (e.g., my_list[2]).
        
        Time Complexity: O(N) - Must traverse 'index' number of steps.

        Args:
            index (int): The 0-based position of the node to retrieve.

        Raises:
            IndexError: If the provided index is out of the linked list bounds.

        Returns:
            Any: The data stored at the specified index.
        """
        curr = self.head
        pos = 0

        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1

        raise IndexError("Linked List index out of bounds")

    # =====================================================================
    # ALGORITHMIC PROBLEM SOLVING (LEETCODE / HACKERRANK)
    # =====================================================================

    def replace_max(self, value):
        """
        Finds the node with the maximum data value and replaces its data.
        
        Time Complexity: O(N) - Linear scan to find the maximum value.

        Args:
            value (Any): The new value to replace the maximum data with.

        Raises:
            ValueError: If the linked list is empty.
        """
        if self.head is None:
            raise ValueError("Cannot replace max in an empty linked list")

        temp = self.head
        max_node = temp

        # Traverse to find the node with the maximum value
        while temp is not None:
            if temp.data > max_node.data:
                max_node = temp
            temp = temp.next

        # Replace the data of the found max node
        max_node.data = value

    def sum_odd_nodes(self):
        """
        Calculates the sum of data in nodes located at odd indices (1, 3, 5...).
        Assumes 0-based indexing (Head is at index 0).
        
        Time Complexity: O(N) - Must traverse the entire list.

        Returns:
            int | float: The calculated sum. Returns 0 if the list is empty.
        """
        temp = self.head
        counter = 0
        result = 0

        while temp is not None:
            # Check if the current index is odd
            if counter % 2 != 0:
                result += temp.data

            counter += 1
            temp = temp.next

        return result

    def reverse(self):
        """
        Reverses the entire linked list IN-PLACE using a three-pointer approach.
        This alters the original list without consuming extra memory.
        
        Time Complexity: O(N) - Single pass through the list.
        Space Complexity: O(1) - No extra data structures created.
        """
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            # Store the next node safely before breaking the link
            next_node = curr_node.next 
            
            # Reverse the pointer direction
            curr_node.next = prev_node 
            
            # Shift pointers one step forward
            prev_node = curr_node
            curr_node = next_node

        # Reassign head to the new front (which was previously the tail)
        self.head = prev_node

    def change_sentence(self):
        """
        String manipulation logic for a linked list of characters.
        Rules:
        - Replaces '*' or '/' with a space (' ').
        - If two consecutive '*' or '/' appear, the second is skipped, 
          and the following character is capitalized.
        
        Time Complexity: O(N) - Single pass through the list.
        """
        temp = self.head

        while temp is not None:
            # Check if current node is a special character
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                
                # Boundary Check 1: Ensure there is a next node
                if temp.next is not None and temp.next.data in ['*', '/']:
                    
                    # Boundary Check 2: Ensure there is a character after the second symbol
                    if temp.next.next is not None:
                        # Capitalize the target character and bypass the second symbol
                        temp.next.next.data = temp.next.next.data.upper()
                        temp.next = temp.next.next
                    else:
                        # If the second symbol is the last node, just cut it off
                        temp.next = None

            temp = temp.next


def get_broadcast_shape(shape1: tuple, shape2:tuple) -> tuple | bool:
    s1 = LinkedList()
    s2 = LinkedList()

    for i in shape1:
        s1.append(i)

    for i in shape2:
        s2.append(i)

    n = len(s1)
    m = len(s2)

    if n > m:
        for i in range(n - m):
            s2.insert_head(1)

    if n < m:
            for i in range(m - n):
                s1.insert_head(1)

    new_shape = []
    i = 0
    s1_head = s1.head
    s2_head = s2.head
    while i < max(n, m):
        if s1_head.data == s2_head.data or s1_head.data == 1 or s2_head.data == 1:
            new_shape.append(max(s1_head.data, s2_head.data))

        else:
            return '❌ Error: Cannot broadcast'

        s1_head = s1_head.next
        s2_head = s2_head.next
        i = i + 1

    
    return tuple(new_shape)



shape1 = (4, 3)
shape2 = (3,)
shape3 = (15, 3, 5)
shape4 = (3, 1)
shape5 = (8, 1, 6, 1)
shape6 = (7, 1, 5)
shape7 = (3, 4)
shape8 = (4, 3)

print(get_broadcast_shape(shape1, shape2))
print(get_broadcast_shape(shape3, shape4))
print(get_broadcast_shape(shape5, shape6))
print(get_broadcast_shape(shape7, shape8))

'''
# =====================================================================
# SYSTEM TESTING: SINGLY LINKED LIST
# =====================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 LINKED LIST COMPLETE STRESS TEST")
    print("="*60 + "\n")

    # ---------------------------------------------------------
    print("--- 1. Base Insertions (Head & Append) ---")
    L = LinkedList()
    L.insert_head(1)
    L.insert_head(2)
    L.insert_head(3)
    L.insert_head(4)
    print(f"After insert_head: {L}")

    L.append(5)
    print(f"After append(5):   {L}")

    # ---------------------------------------------------------
    print("\n--- 2. Targeted Insertion (insert_after) ---")
    L.insert_after(2, 200)
    print(f"After inserting 200 after 2: {L}")

    l3 = LinkedList()
    l3.append(5)
    l3.insert_after(5, 100)
    print(f"Edge Case (Single node insert_after): {l3}")

    # ---------------------------------------------------------
    print("\n--- 3. Deletion & Memory Clear ---")
    l4 = LinkedList()
    l4.append(5)
    l4.clear()
    print(f"After clear() on l4: '{l4}' (Empty)")

    print(f"\nOriginal List before deletions: {L}")
    L.delete_head()
    L.delete_head()
    print(f"After 2x delete_head(): {L}")

    L.pop()
    print(f"After pop() (tail removed): {L}")

    L.remove(200)
    print(f"After remove(200): {L}")

    # ---------------------------------------------------------
    print("\n--- 4. Search & Indexing (Magic Methods) ---")
    print(f"Index of 2: {L.search(2)}")
    print(f"Index of 1: {L.search(1)}")
    
    print(f"Item at index 1 (L[1]): {L[1]}")
    print(f"Item at index 0 (L[0]): {L[0]}")

    print("\n[Testing Professional Error Handling]")
    try:
        L.search(10)
    except Exception as e:
        print(f"✅ Caught Search Error: {type(e).__name__} -> {e}")

    try:
        print(L[10])
    except Exception as e:
        print(f"✅ Caught Index Error: {type(e).__name__} -> {e}")

    # ---------------------------------------------------------
    print("\n--- 5. Algorithmic Problems ---")
    L.replace_max(12)
    print(f"After replace_max(12): {L}")

    print(f"Sum of odd indices: {L.sum_odd_nodes()}")

    L.reverse()
    print(f"After in-place reverse(): {L}")

    # ---------------------------------------------------------
    print("\n--- 6. String Manipulation (change_sentence) ---")
    L3 = LinkedList()
    for char in ['T', 'h', 'e', '/', '*', 's', 'k', 'y', '*', 'i', 's', '/', '/', 'b', 'l', 'u', 'e']:
        L3.append(char)
    
    print(f"Original Sentence: {L3}")
    L3.change_sentence()
    print(f"Decoded Sentence:  {L3}")

    # ---------------------------------------------------------
    print("\n--- 7. Pythonic Iteration (__iter__ & __next__) ---")
    print(f"Iterating over list L ({L}):")
    for item in L:
        print(f" -> Node Data: {item}")

    print("\n🎯 TESTING COMPLETE.")
    print("="*60 + "\n")
'''