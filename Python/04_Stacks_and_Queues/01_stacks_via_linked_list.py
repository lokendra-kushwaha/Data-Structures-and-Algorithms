"""
=============================================================================
DATA STRUCTURES & ALGORITHMS: THE STACK (LIFO ARCHITECTURE)
=============================================================================

[CONCEPTUAL OVERVIEW]
A Stack is a linear Abstract Data Type (ADT) that stores and organizes data 
governed strictly by the **LIFO (Last In, First Out)** principle. This means 
that the element added most recently is always the first one to be removed.

[VISUAL ARCHITECTURE & MEMORY TOPOLOGY]
Visualizing a vertical stack where all structural operations occur exclusively 
at a single designated entry/exit point known as "The Top":

           +---------+
           |    5    | <-- Top (Operations: push, pop, peek happen here)
           +---------+
           |    4    |
           +---------+
           |    3    |
           +---------+
           |    2    |
           +---------+
           |    1    | <-- Bottom (First element inserted)
           +---------+

[CORE OPERATIONS & TIME COMPLEXITIES]
1. push(item)   : Inserts a new element onto the top of the stack.      -> O(1)
2. pop()        : Removes and returns the top element from the stack.   -> O(1)
3. peek()       : Inspects the top element without removing it.         -> O(1)
4. is_empty()   : Validates whether the stack contains any elements.    -> O(1)
5. size()       : Returns the total active count of elements.           -> O(1)

[DUAL IMPLEMENTATION STRATEGIES]
Stacks can be engineered using two primary underlying data structures:

1. Linked List Implementation (The Dynamic Approach):
   - By restricting all structural mutations strictly to the `head` pointer, 
     a Singly Linked List functions perfectly as a Stack.
   - `push()` maps directly to `insert_head()`.
   - `pop()` maps directly to `delete_head()`.
   - *Advantage:* Truly dynamic sizing; never runs out of capacity (limited 
     only by system RAM) and guarantees strict O(1) operations.

2. Array Implementation (The Contiguous Approach):
   - Utilizing contiguous memory blocks where the tail of the array acts 
     as the stack's top.
   - `push()` maps to array appending.
   - `pop()` maps to array popping.
   - *Advantage:* Superior CPU cache locality and rapid element traversal.
=============================================================================
"""
# ===========================================================================
"""
=============================================================================
Data Structures & Algorithms - Stack via Linked List
=============================================================================
A dynamic, Node-based implementation of the Stack (LIFO) data structure.
Since this utilizes a Linked List under the hood, it is not constrained 
by a fixed size, and all primary operations run in strictly O(1) time.
=============================================================================
"""

class Node:
    """A fundamental memory block for the Stack."""
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    """
    A LIFO (Last In, First Out) data structure managed via pointers.
    
    Attributes:
        top (Node | None): Pointer to the most recently added node.
        size (int): Current number of elements in the stack.
    """
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        """
        Checks if the stack contains no elements.
        
        Time Complexity: O(1)
        Returns:
            bool: True if empty, False otherwise.
        """
        return self.top is None

    def __str__(self):
        """
        Visualizes the stack from Top to Bottom (Replaces traverse method).

        Time Complexity: O(N)
        Returns:
            str: A formatted string representing the stack.
        """
        if self.is_empty():
            return "Stack is Empty"
            
        temp = self.top
        result = "Top -> "
        while temp is not None:
            result += f"[{temp.data}] -> "
            temp = temp.next
        return result + "Bottom"

    def __len__(self):
        """
        Magic method to support the native len() function.
        Time Complexity: O(1)
        """
        return self.size

    def push(self, value):
        """
        Adds a new element to the top of the stack (Equivalent to insert_head).
        
        Time Complexity: O(1)
        Args:
            value (Any): The data to be added to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the top element of the stack (Equivalent to delete_head).
        
        Time Complexity: O(1)
        Raises:
            IndexError: If attempting to pop from an empty stack.
        Returns:
            Any: The data from the removed top node.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
            
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        """
        Returns the top element without removing it.
        
        Time Complexity: O(1)
        Raises:
            IndexError: If the stack is empty.
        Returns:
            Any: The data at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

"""
# =====================================================================
# SYSTEM TESTING
# =====================================================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 STACK (LINKED LIST) - CORE TESTING")
    print("="*50 + "\n")

    s = Stack()
    print(f"Initial State: is_empty() -> {s.is_empty()}")

    print("\n--- Pushing Items ---")
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(f"Current Size: len(s) -> {len(s)}")

    print("\n--- Peeking & Popping ---")
    print(f"Peek (Top Item): {s.peek()}")
    print(f"Popped Item: {s.pop()}")
    print(f"Stack after Pop: \n{s}")

    print("\n--- Error Handling Test ---")
    s.pop() # Removes 20
    s.pop() # Removes 10
    
    try:
        s.pop() # IndexError
    except Exception as e:
        print(f"✅ Successfully caught error: {type(e).__name__} -> {e}")
"""
        
# =====================================================================
# STACK ALGORITHMS & INTERVIEW PROBLEMS
# =====================================================================

def reverse_string(text):
    """
    Reverses a string using a Stack (LIFO property).
    Time Complexity: O(N) | Space Complexity: O(N)
    """
    s = Stack()
    for char in text:
        s.push(char)

    res = ''
    while not s.is_empty():
        res += s.pop()

    return res


def text_editor(text, pattern):
    """
    Simulates a text editor's Undo/Redo functionality using Two Stacks.
    'u' pattern stands for Undo, 'r' (or anything else) stands for Redo.
    """
    u = Stack()  # Undo Stack (Stores current active characters)
    r = Stack()  # Redo Stack (Stores undone characters)

    # Load initial text into the Undo stack
    for char in text:
        u.push(char)

    # Process operations
    for action in pattern:
        if action.lower() == 'u':
            # Perform Undo only if there's something to undo
            if not u.is_empty():
                r.push(u.pop())
        else:
            # Perform Redo only if there's something to redo
            if not r.is_empty():
                u.push(r.pop())

    # Rebuild the final string
    res = ""
    while not u.is_empty():
        res = u.pop() + res  # Prepend to maintain original order

    return res


def find_the_celebrity(matrix):
    """
    Finds a celebrity in a party using a Stack.
    Rules: A celebrity knows NO ONE, but EVERYONE knows the celebrity.
    Matrix: matrix[i][j] == 1 means 'i' knows 'j'.
    
    Time Complexity: O(N)
    """
    s = Stack()
    n = len(matrix)

    # Push all people (candidates) onto the stack
    for i in range(n):
        s.push(i)

    # Elimination Phase
    while s.size >= 2:
        i = s.pop()
        j = s.pop()

        if matrix[i][j] == 0:
            # i does NOT know j. Thus, j cannot be a celebrity. 
            # i is still a candidate.
            s.push(i)
        else:
            # i knows j. Thus, i cannot be a celebrity.
            # j is still a candidate.
            s.push(j)

    # If stack is empty, there is no candidate
    if s.is_empty():
        return 'No one is a celebrity.'

    # Verification Phase (Verify the last remaining candidate)
    celeb = s.pop()
    for i in range(n):
        if i != celeb:
            # If celeb knows 'i', OR 'i' does NOT know celeb -> Fake Celebrity
            if matrix[celeb][i] == 1 or matrix[i][celeb] == 0:
                return 'No one is a celebrity.'

    return f'The celebrity is {celeb}'


def is_balanced_bracket(mathematical_string):
    """
    Validates if a mathematical expression has perfectly balanced brackets.
    Time Complexity: O(N) | Space Complexity: O(N)
    """
    s = Stack()
    # Dictionary mapping closing brackets to their matching opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in mathematical_string:
        # If it's an OPENING bracket, push to stack
        if char in ['(', '{', '[']:
            s.push(char)
            
        # If it's a CLOSING bracket
        elif char in [')', '}', ']']:
            
            # 1. If stack is empty but a closing bracket arrives -> Unbalanced
            if s.is_empty():
                return False
                
            # 2. Pop the top bracket and check if it matches the current closing bracket
            top_char = s.pop()
            if top_char != bracket_map[char]:
                return False

    # 3. At the end, if stack is completely empty, it means all brackets matched perfectly
    return s.is_empty()


# =====================================================================
# SYSTEM TESTING: STACK ALGORITHMS
# =====================================================================
"""
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 STACK ALGORITHMS - INTERVIEW PROBLEMS TEST")
    print("="*50 + "\n")

    # ---------------------------------------------------------
    print("--- 1. String Reversal ---")
    original_str = 'Lokendra'
    reverse = reverse_string(original_str)
    print(f"Original String : '{original_str}'")
    print(f"Reversed String : '{reverse}'")

    # ---------------------------------------------------------
    print("\n--- 2. Text Editor (Undo/Redo) ---")
    text = 'Lokendra'
    pattern = 'uurur'
    edit = text_editor(text, pattern)
    print(f"Original Text   : '{text}'")
    print(f"Action Pattern  : '{pattern}' (u=Undo, r=Redo)")
    print(f"Final Text      : '{edit}'")

    # ---------------------------------------------------------
    print("\n--- 3. Find the Celebrity ---")
    matrix = [
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0],  # Node 2 knows no one (Potential Celebrity)
        [0, 0, 1, 0]
    ]
    celebrity = find_the_celebrity(matrix)
    print("Party Matrix:")
    for row in matrix:
        print(f"  {row}")
    print(f"Result: {celebrity}")

    # ---------------------------------------------------------
    print("\n--- 4. Balanced Bracket Validator ---")
    expr1 = '[(a+b)*c]'
    expr2 = '[(a+b)*c'  # Custom edge case (Missing closing bracket)
    
    print(f"Expression: '{expr1}' -> Balanced? {is_balanced_bracket(expr1)}")
    print(f"Expression: '{expr2}' -> Balanced? {is_balanced_bracket(expr2)}")

    print("\n🎯 ALL ALGORITHMS TESTED SUCCESSFULLY.")
    print("="*50 + "\n")
"""