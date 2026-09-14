# ==============================================================================
# 🧠 QUEUES (LINKED LIST IMPLEMENTATION)
# ==============================================================================

# 1. WHAT IS A QUEUE?
# A Queue is a linear data structure that strictly follows the 
# FIFO (First In, First Out) principle. Think of it like a line at a ticket counter: 
# the first person to join the line is the first one to be served.

# 2. STACK VS QUEUE MECHANICS
# * Stack: Insertion and deletion happen from the SAME end (Top).
# * Queue: Insertion happens at the REAR (Tail), and deletion happens at the FRONT (Head).

# 3. QUEUE OPERATIONS & TIME COMPLEXITY (Linked List Approach)
# * Enqueue -> Add item to the rear        -> O(1) Time Complexity
# * Dequeue -> Remove item from the front  -> O(1) Time Complexity
# * Peek    -> View front or rear item     -> O(1) Time Complexity


# ==============================================================================
# ⚙️ QUEUE IMPLEMENTATION
# ==============================================================================

class Node:
    """A standard node building block for the Linked List."""
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    """
    A dynamic Queue data structure implemented using a Singly Linked List.
    This allows the queue to grow and shrink without strict memory limits.
    """

    def __init__(self):
        self.front = None  # Pointer to the first element (dequeue happens here)
        self.rear = None   # Pointer to the last element (enqueue happens here)
        self._size = 0     # Internal counter for O(1) size retrieval

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.front is None

    def enqueue(self, value):
        """
        Inserts a new element at the rear (tail) of the queue.
        """
        new_node = Node(value)

        # If the queue is empty, the new node is BOTH front and rear
        if self.is_empty():
            self.front = new_node
            self.rear = self.front
        else:
            # Link the current rear to the new node, then update rear pointer
            self.rear.next = new_node
            self.rear = new_node
            
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front (head) of the queue.
        
        Raises:
            IndexError: If attempting to dequeue from an empty queue.
        """
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
            
        data = self.front.data
        self.front = self.front.next  # Move front pointer to the next node
        
        # If the queue becomes empty after popping, rear must also be None
        if self.front is None:
            self.rear = None
            
        self._size -= 1
        return data

    def size(self) -> int:
        """Returns the total number of elements in O(1) time."""
        return self._size

    def get_front(self):
        """Returns the data at the front without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty: No front element exists.")
        return self.front.data

    def get_rear(self):
        """Returns the data at the rear without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty: No rear element exists.")
        return self.rear.data

    def __str__(self) -> str:
        """Returns a string representation of the queue from Front to Rear."""
        if self.is_empty():
            return "[Empty Queue]"
            
        elements = []
        current = self.front
        while current is not None:
            elements.append(str(current.data))
            current = current.next
            
        return "FRONT -> " + " | ".join(elements) + " <- REAR"


# ==============================================================================
# 🚀 EXECUTION & TESTING
# ==============================================================================

if __name__ == "__main__":
    q = Queue()

    print("Initial state:", q)

    # Testing Enqueue
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print("After enqueuing 3 items:", q)

    # Testing Dequeue
    print("Dequeued:", q.dequeue())
    print("State:", q)

    print("Dequeued:", q.dequeue())
    print("State:", q)

    print("Dequeued:", q.dequeue())
    print("State:", q)

    # Triggering Underflow Error (Uncomment to test)
    # q.dequeue()

    # Re-enqueuing to test empty state recovery
    q.enqueue(10)
    print("After enqueuing to empty queue:", q)
    print(f"Current Size: {q.size()}")
    print(f"Front Data: {q.get_front()}")
    print(f"Rear Data: {q.get_rear()}")

# Queue using 2 Stacks --> Interview problem