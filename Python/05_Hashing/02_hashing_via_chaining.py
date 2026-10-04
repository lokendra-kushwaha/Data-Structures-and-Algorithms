# ============================================================================
#       CUSTOM DICTIONARY IMPLEMENTATION USING SEPARATE CHAINING
# ============================================================================
#
# HOW SEPARATE CHAINING WORKS:
# Instead of storing raw values in the array, every index (bucket) in the 
# array holds a "Singly Linked List". When a collision occurs (two keys hash 
# to the same index), we simply append the new key-value pair as a new Node 
# at the end of that specific Linked List.
#
# ASCII VISUALIZATION:
# Index   Array of Linked Lists (Buckets)
#         +---------+
#   0     | Bucket 0| -> [ key:'c', val:100 ] -> [ key:'java', val:56 ] -> None
#         +---------+
#   1     | Bucket 1| -> None  (Empty bucket)
#         +---------+      
#   2     | Bucket 2| -> [ key:'python', val:34 ] -> None
#         +---------+      
#
# WHAT IS THE LOAD FACTOR?
# Load Factor (λ) = Total Number of Items / Total Number of Buckets (Capacity)
# It measures how "full" our hash table is. 
# - If Capacity = 3, and we insert 6 items, Load Factor = 6 / 3 = 2.0.
# - This means, on average, every linked list has 2 nodes.
#
# WHY DO WE NEED REHASHING?
# If we keep adding items without increasing the array size, the Linked Lists 
# will become very long. Searching a long linked list takes O(N) time, destroying 
# our O(1) hashing speed! 
# Solution: When Load Factor >= 2.0 (Threshold), we DOUBLE the capacity of the 
# array, and recalculate the hash for EVERY existing node to distribute them 
# evenly across the new, larger array. This restores O(1) performance.
# ============================================================================

class Node:
    """
    A fundamental memory block for the Singly Linked List.

    Attributes:
        key (Any): The dictionary key used for hashing and searching.
        value (Any): The actual data associated with the key.
        next (Node | None): A pointer to the next Node in the sequence. 
                            Defaults to None for a newly created node.
    """

    def __init__(self, key, value):
        """
        Initializes a new Node with a key-value pair.

        Args:
            key (Any): The key to be stored in the node.
            value (Any): The value to be associated with the key.
        """
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    """
    An independent manager class orchestrating Node objects.

    Handles its own sequence logic, insertions, deletions, and string representation.

    Attributes:
        head (Node | None): Pointer to the first node in the list.
        n (int): The current total count of nodes in the list.
    """

    def __init__(self):
        """Initializes an empty Linked List."""
        self.head = None
        self.n = 0

    def __len__(self):
        """
        Retrieves the total number of nodes in the linked list.

        Returns:
            int: The size of the linked list.
        """
        return self.n

    def __str__(self):
        """
        Generates a string representation of the linked list's contents.

        Uses the '->' format to visually indicate Key-Value mapping.

        Returns:
            str: A formatted string of nodes, e.g., "'key' -> value, ".
        """
        curr = self.head
        result = ''
        
        while curr is not None:
            result += f"'{curr.key}' -> {curr.value}, "
            curr = curr.next
            
        return result

    def append(self, key, value):
        """
        Appends a new node to the very end of the linked list.

        Time Complexity: O(N) where N is the number of nodes.

        Args:
            key (Any): The dictionary key to append.
            value (Any): The value associated with the key.
        """
        new_node = Node(key, value)
        
        # Edge Case: If list is empty
        if self.head is None:
            self.head = new_node
            self.n += 1
            return

        # Traversal to find the tail
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        # Connect the last node to the new node
        curr.next = new_node
        self.n += 1

    def delete_head(self):
        """
        Removes the first node (head) from the linked list.

        Time Complexity: O(1).

        Raises:
            IndexError: If the linked list is already empty.
        """
        if self.head is None:
            raise IndexError("Cannot delete head from an empty linked list.")
        
        self.head = self.head.next
        self.n -= 1

    def remove(self, key):
        """
        Removes the first occurrence of a specific node by its key.

        Time Complexity: O(N) where N is the number of nodes.

        Args:
            key (Any): The key of the node to be removed.

        Raises:
            KeyError: If the target key is not present in the linked list.
        """
        if self.head is None:
            raise KeyError(f"Key not found: '{key}'")

        # Case 1: The node to remove is at the head
        if self.head.key == key:
            self.delete_head()
            return

        # Case 2: The node is somewhere in the middle or end
        curr = self.head
        while curr.next is not None:
            if curr.next.key == key:
                curr.next = curr.next.next  
                self.n -= 1
                return
            curr = curr.next
        
        # Case 3: Reached the end, key not found
        raise KeyError(f"Key not found: '{key}'")

    def get_node_by_key(self, key):
        """
        Searches for a node by its key.

        Time Complexity: O(N) where N is the number of nodes.

        Args:
            key (Any): The target key to find.

        Returns:
            Node | None: The actual Node object if found, otherwise None.
        """
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None


class Dictionary:
    """
    A Hash Map Dictionary utilizing Separate Chaining to resolve collisions.

    Attributes:
        capacity (int): The current maximum size of the bucket array.
        size (int): The total number of key-value pairs stored.
        buckets (list): The array holding LinkedList objects for each bucket.
    """

    def __init__(self, capacity):
        """
        Initializes the bucket array with the given capacity.

        Args:
            capacity (int): The initial number of buckets for the hash table.
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        """
        Generates an array filled with empty LinkedList objects.

        Args:
            capacity (int): The required size of the array.

        Returns:
            list: A list containing initialized LinkedList objects.
        """
        return [LinkedList() for _ in range(capacity)]

    def hash_function(self, key):
        """
        Generates a valid bucket index using modulo arithmetic.

        Args:
            key (Any): The key to be hashed.

        Returns:
            int: The calculated array index.
        """
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        """
        Inserts or updates a key-value pair in the dictionary. 
        
        Automatically triggers a rehash if the load factor reaches 2.0 or higher.

        Args:
            key (Any): The key to insert or update.
            value (Any): The value to associate with the key.
        """
        bucket_index = self.hash_function(key)
        linked_list = self.buckets[bucket_index]

        node = linked_list.get_node_by_key(key)
        
        if node is None:
            linked_list.append(key, value)
            self.size += 1

            load_factor = self.size / self.capacity
            if load_factor >= 2.0:
                self.rehash()
        else:
            node.value = value

    def get(self, key):
        """
        Retrieves a value by its key.

        Args:
            key (Any): The target key to search for.

        Returns:
            Any: The value associated with the specified key.

        Raises:
            KeyError: If the key does not exist in the dictionary.
        """
        bucket_index = self.hash_function(key)
        node = self.buckets[bucket_index].get_node_by_key(key)
        
        if node is None:
            raise KeyError(f"Key not found: '{key}'")
        return node.value

    def rehash(self):
        """Doubles capacity and redistributes items to maintain O(1) performance."""
        self.capacity = self.capacity * 2
        old_buckets = self.buckets
        
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        for linked_list in old_buckets:
            curr = linked_list.head
            while curr is not None:
                self.put(curr.key, curr.value)
                curr = curr.next

    def __setitem__(self, key, value):
        """
        Magic method to allow assignment syntax (e.g., d[key] = value).

        Args:
            key (Any): The key to assign.
            value (Any): The value to associate.
        """
        self.put(key, value)

    def __getitem__(self, key):
        """
        Magic method to allow retrieval syntax (e.g., val = d[key]).

        Args:
            key (Any): The target key.

        Returns:
            Any: The stored value.
        """
        return self.get(key)

    def __delitem__(self, key):
        """
        Magic method to allow deletion syntax (e.g., del d[key]).

        Args:
            key (Any): The key to delete.

        Raises:
            KeyError: If the key is not found (handled by LinkedList).
        """
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)
        self.size -= 1

    def __len__(self):
        """
        Returns the total number of items stored in the dictionary.

        Returns:
            int: The size of the dictionary.
        """
        return self.size

    def __str__(self):
        """
        Constructs the final dictionary string representation.

        Aggregates the __str__ outputs from all internal LinkedList objects.

        Returns:
            str: The formatted dictionary string.
        """
        result = ''
        for linked_list in self.buckets:
            result += str(linked_list)
            
        if len(result) > 0:
            result = result[:-2]
            
        return '{' + result + '}'


# ============================================================================
#                              TESTING THE CODE
# ============================================================================

if __name__ == "__main__":
    D = Dictionary(3)

    print("--- Inserting Initial Items ---")
    D['python'] = 34
    D['c'] = 1000
    D['c++'] = 10000
    D['ruby'] = 20000
    D['java'] = 56
    D['js'] = 56
    D['html'] = 56

    print("\n--- Dictionary State (Using Custom '->' Format) ---")
    print(D)
    print(f"Total Items: {len(D)}")
    print(f"Current Capacity (Expanded via Rehash): {D.capacity}")

    print("\n--- Testing Deletion (Using delete_head / remove) ---")
    del D['c']
    print("Dictionary after deleting 'c':")
    print(D)
    print(f"New Size: {len(D)}")