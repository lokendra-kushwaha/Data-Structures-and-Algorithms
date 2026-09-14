# ==============================================================================
# 🧠 STACKS & PYTHON LISTS
# ==============================================================================

# 1. PYTHON LISTS AS NATIVE STACKS
# Python does not have native fixed-size arrays like C or Java. 
# It uses dynamic lists under the hood. 
# However, Python lists are highly optimized to act as Stacks right out of the box, 
# provided you strictly add and remove data from one end (the right side).

# 2. STACK OPERATIONS & TIME COMPLEXITY (Using Python Lists)
# * Push -> L.append(value) -> O(1) : Adds a new element to the top (end) of the stack.
# * Pop  -> L.pop()         -> O(1) : Removes and returns the top (last) element.
# * Peek -> L[-1]           -> O(1) : Views the top element without deleting it.
# * Size -> len(L)          -> O(1) : Returns the total number of elements currently in the stack.
'''
L = [1, 2, 3, 4]

L.append(5) # like stack's push function
print(L)

L.pop() # like stack's pop function
print(L)

print(L[-1]) # like stack's peek function
'''
# ==============================================================================
# ⚙️ FIXED-SIZE STACK IMPLEMENTATION
# ==============================================================================

class Stack:
    """
    A fixed-size Stack data structure implementation using a pre-allocated Python list.
    
    This class simulates a rigid array environment where the maximum size is defined 
    at instantiation, preventing dynamic memory resizing.
    """

    def __init__(self, size: int):
        """
        Initializes the stack with a fixed size and a top pointer.

        Args:
            size (int): The maximum number of elements the stack can hold.
        """
        self.size = size
        # Simulating a fixed-size array by pre-allocating 'None'
        # The double underscore '__' makes the stack private (encapsulation)
        self.__stack = [None] * self.size 
        self.top = -1  # Pointer tracking the index of the highest element

    def is_full(self) -> bool:
        """Checks if the stack has reached its maximum capacity."""
        return self.top == self.size - 1

    def is_empty(self) -> bool:
        """Checks if the stack contains no elements."""
        return self.top == -1

    def push(self, value):
        """
        Pushes a new element onto the top of the stack.

        Args:
            value: The data to be inserted.

        Raises:
            OverflowError: If attempting to push to a stack that is already full.
        """
        if self.is_full():
            raise OverflowError(f"Stack Overflow: Cannot push {value}. Maximum capacity ({self.size}) reached.")
        
        self.top += 1
        self.__stack[self.top] = value

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
            The data stored at the current top of the stack.

        Raises:
            IndexError: If attempting to pop from an empty stack.
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: The stack is currently empty.")
        
        data = self.__stack[self.top]
        # We don't need to physically delete the data; moving the pointer down is enough.
        # The next push will simply overwrite the old value.
        self.top -= 1
        return data

    def peek(self):
        """
        Returns the top element without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty: Nothing to peek at.")
        return self.__stack[self.top]

    def __str__(self) -> str:
        """Returns a string representation of the current active stack."""
        if self.is_empty():
            return "[Empty Stack]"
            
    
        active_elements = [str(self.__stack[i]) for i in range(self.top + 1)]
        return " -> ".join(active_elements)


if __name__ == "__main__":
    # --- Execution & Testing ---

    # Initialize a stack of size 3
    s = Stack(3)
    print("Initial:", s)

    # Push operations
    s.push(4)
    s.push(5)
    s.push(6)
    print("After 3 Pushes:", s)

    # Triggering Overflow (Uncomment to test)
    # s.push(7) 

    # Pop operations
    print("Popped:", s.pop())
    print("Popped:", s.pop())
    print("After 2 Pops:", s)

    # Peek operation
    print("Current Top:", s.peek())

    