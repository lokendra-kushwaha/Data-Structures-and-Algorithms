# ==========================================
# LINKED LIST
# ==========================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self._length += 1

    def __len__(self):
        return self._length


def get_broadcast_shape_linked_list(shape1: tuple, shape2: tuple) -> tuple | str:
    """
    Calculates the broadcasted shape of two multidimensional arrays using a Linked List architecture.

    This function mimics NumPy's broadcasting rules but utilizes a custom Singly Linked List 
    to achieve strictly O(1) time complexity for left-padding operations. By avoiding the 
    O(N) memory-shifting overhead of native Python dynamic arrays (lists), this engine 
    scales flawlessly even with millions of dimensions.

    Args:
        shape1 (tuple): The dimensional shape of the first array (e.g., (15, 3, 5)).
        shape2 (tuple): The dimensional shape of the second array (e.g., (3, 1)).

    Returns:
        tuple | str: A tuple representing the final broadcasted shape if compatible. 
                     Returns an error string ('❌ Error: Cannot broadcast') if the shapes 
                     violate broadcasting rules.

    Time Complexity: O(max(N, M)) where N and M are the lengths of shape1 and shape2.
    Space Complexity: O(max(N, M)) to store the linked lists and the resulting shape.
    """
    
    # Initialize custom Linked Lists to hold the dimensions
    s1 = LinkedList()
    s2 = LinkedList()

    # Populate the linked lists with the dimensions from the input tuples
    for i in shape1:
        s1.append(i)
    for i in shape2:
        s2.append(i)

    n = len(s1)
    m = len(s2)

    # ---------------------------------------------------------
    # THE CORE OPTIMIZATION: O(1) Zero-Shift Padding
    # Instead of shifting elements in a contiguous array (O(N) cost),
    # we strictly use O(1) head insertion to left-pad the shorter shape with 1s.
    # ---------------------------------------------------------
    if n > m:
        for _ in range(n - m):
            s2.insert_head(1)
    elif n < m:
        for _ in range(m - n):
            s1.insert_head(1)

    new_shape = []
    i = 0
    
    # Initialize C-style pointer traversal from the heads of both lists
    s1_head = s1.head
    s2_head = s2.head
    
    # Traverse both shapes left-to-right to validate broadcasting compatibility
    while i < max(n, m):
        
        # RULE: Dimensions are compatible if they are equal, or if one of them is exactly 1.
        if s1_head.data == s2_head.data or s1_head.data == 1 or s2_head.data == 1:
            # The resulting dimension is always the maximum of the two
            new_shape.append(max(s1_head.data, s2_head.data))
        else:
            # Fail fast if any dimension violates the broadcasting rule
            return '❌ Error: Cannot broadcast'
        
        # Pointer jump (O(1) traversal without indexing arithmetic overhead)
        s1_head = s1_head.next
        s2_head = s2_head.next
        i += 1
        
    return tuple(new_shape)