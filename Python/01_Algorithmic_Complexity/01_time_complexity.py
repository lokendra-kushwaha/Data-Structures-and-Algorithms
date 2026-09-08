# ==================================================================================
# 💎 THE DSA VAULT: ULTIMATE TIME COMPLEXITY & BIG-O MASTERCLASS 💎
# ==================================================================================
# 👨‍💻 Architect: Lokendra
# 🧠 Core Philosophy: "Never just write code. Always measure its speed."
# 
# 📌 ABOUT THIS VAULT:
# This file is not just a collection of notes; it is the ultimate foundation of 
# System Design and Data Structures. It contains the core theory, graphical 
# representations, and 18 strict "First-Principle" mathematical derivations of 
# how algorithms scale in the real world.
#
# ⚠️ HOW TO USE:
# Read the theory first, internalize the graphs, and always trace the practice 
# problems step-by-step using First Principles before jumping to Big-O conclusions.
# ==================================================================================

# ==================================================================================
# 🚀 ALGORITHMIC COMPLEXITY 
# ==================================================================================
# This indicates how efficient your algorithm is.
# For example, just like a bike's mileage determines its efficiency.

# What is efficiency in programming? ->
# It refers to how much time and how much space (memory) the program consumes.
#
# Parameters of measurement:
# 1. Time (CPU Execution Time)
# 2. Space (RAM/Storage Allocation)


# ==================================================================================
# ⏱️ TIME COMPLEXITY MEASUREMENT TECHNIQUES
# ==================================================================================
# Techniques to measure time efficiency:
# 1. Measuring time to execute (using the time module)
# 2. Counting operations involved
# 3. Abstract notion of 'order of growth' (Big O Notation)

# ----------------------------------------------------------------------------------
# ❌ 1. Measuring Time (The Flawed Approach)
# ----------------------------------------------------------------------------------
import time

start = time.time()

for i in range(1, 101):
    print(i)

i = 1
while i < 101:
    print(i)
    i += 1

print(time.time() - start)

# We do not use this method to measure time because execution time depends 
# heavily on hardware. Running it on different CPUs will yield different times.
# Also, even if the algorithm logic remains exactly the same, making minor tweaks 
# (like replacing a 'for' loop with a 'while' loop) will change the execution time.

# Limitations & Benefits of this approach ->
# Benefit:
# 1. Shows different times for different algorithms.

# Problems with this approach:
# 2. Time varies if the implementation changes.
# 3. Different machines yield different times.
# 4. Does not work for extremely small inputs.
# 5. Time varies for different inputs, but we cannot establish a mathematical relationship.


# ----------------------------------------------------------------------------------
# ⚠️ 2. Counting Operations
# ----------------------------------------------------------------------------------
# Assume these basic steps take constant time:
# - mathematical operations (+, -, *, /)
# - comparisons (>, <, ==)
# - assignments (=)
# - accessing objects in memory (indexing)

# Then count the number of operations executed as a function of the size of the input.

def c_to_f(c):
    return c*9.0/5 + 32  # 3 ops (1 multiply, 1 divide, 1 add)

def mysum(x):
    total = 0              # 1 op (assignment)
    for i in range(x + 1): # 1 op (loop initialization)
        total += i         # 2 ops (addition and assignment)
    # loops x times

    return total

# Total operations for mysum(x) -> 1 + 3x 
# (1 operation outside the loop and 3 operations inside the loop running 'x' times).

# Does it solve previous problems?
# - "Different machines different time" -> This problem is solved because the 
#   count of operations will remain the exact same on every machine.
# - "Time varies for different inputs, but can't establish a relationship" -> 
#   This is also solved because we established a mathematical relationship: T(x) = 1 + 3x.

# Limitations & Benefits ->
# Benefits:
# 1. Differentiates time for different algorithms.
# 3. Solves the machine dependency issue.
# 5. Establishes a relationship between time and input size.

# Problems with this approach:
# 2. Operations vary if implementation changes (If we replace the 'for' loop 
#    with a 'while' loop, the exact operation count will change).
# 4. No clear definition of which operations to strictly count.


# ----------------------------------------------------------------------------------
# ✅ What do we actually want?
# ----------------------------------------------------------------------------------
# 1. We want to evaluate the algorithm itself, not the machine or coding style.
# 2. We want to evaluate scalability -> How much time will it take when the input is extremely large?
# 3. We want to evaluate time strictly in terms of input size.


# DIFFERENT INPUTS CHANGE HOW THE PROGRAM RUNS
# Consider a function that searches for an element in a list:

def search_for_elmt(L, e):
    for i in L:
        if i == e:
            return True
    return False

# - When 'e' is the first element in the list -> BEST CASE
# - When 'e' is not in the list or is the last element -> WORST CASE
# - When we have to look through about half the elements -> AVERAGE CASE

# Note: When designing an algorithm, we always evaluate its performance 
# efficiency based on the Worst-Case Scenario.


# ----------------------------------------------------------------------------------
# 🏆 3. Order of Growth & Big Oh Notation (The Industry Standard)
# ----------------------------------------------------------------------------------
# Goals:
# - Want to evaluate the program's efficiency when 'input is very big'.
# - Want to express the 'growth of program's run time' as input size grows [Relationship graph].
# - Want to put an 'upper bound' on growth - as tight as possible -> We assume the worst-case scenario.
# - Do not need to be precise: "order of" not "exact" growth. 
#   [Assume T = i^2 + 2i + 2 -> We only need T = i^2 for our analysis -> Quadratic relation]
# - We will look at 'largest factors' in run time (Which section takes the longest to run?)
# "Thus, generally we want a tight upper bound on growth, as a function of input size, in the worst case."

# MEASURING ORDER OF GROWTH: BIG OH NOTATION
# Big Oh notation measures an 'upper bound on the asymptotic growth', often called order of growth.

# Big Oh or O() is used to describe the worst case:
# - The worst case occurs often and is the main bottleneck when a program runs.
# - It expresses the rate of growth of the program relative to the input size.
# - It evaluates the algorithm, NOT the machine or the specific implementation.


# ----------------------------------------------------------------------------------
# 🧮 EXACT STEPS vs O() (FIRST PRINCIPLES)
# ----------------------------------------------------------------------------------
def fact_iter(n):
    """assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        answer -= 1
    return answer

# Computes factorial.
# Number of steps: (1 + 5n)
# Worst case asymptotic complexity rules:
# - Ignore additive constants.
# - Ignore multiplicative constants.

# Calculation:
# 1. Remove additive constants -> 1 + 5n --> 5n
# 2. Remove multiplicative constants -> 5n --> n
# Final Answer = n -> O(n) (Linear Relation)


# ----------------------------------------------------------------------------------
# 🧩 PRACTICE EXAMPLES (Applying the Rules)
# ----------------------------------------------------------------------------------
# 🧮 BIG O CALCULATION: FIRST PRINCIPLES (Step-by-Step)
# ==================================================================================
# Rule 1: Ignore Additive Constants.
# Rule 2: Ignore Multiplicative Constants.
# Rule 3: Keep only the dominating term (Largest Factor).

# Example 1. T = n^2 + 2n + 2
# Understanding the equation:
# n^2 -> The algorithm has a nested loop.
# 2n -> There are 2 operations happening inside the single loop.
# 2 -> There are 2 operations happening outside all loops.
#
# First Principle Calculation: 
# 1. Removing additive constants -> n^2 + 2n + 2 --> n^2 + 2n
# 2. Removing multiplicative constants -> n^2 + 2n --> n^2 + n
# 3. Looking for the largest factor -> n^2 grows faster than n --> n^2
# 🏆 Final Answer -> O(n^2) (Quadratic Relation)

# Example 2: T = n^2 + 100000n + 3^1000
# Step 1: Remove constant (Because 3^1000 is just a massive constant, it gets dropped) (3^1000) -> n^2 + 100000n
# Step 2: Remove multiplier -> n^2 + n
# Step 3: Dominating term -> n^2
# 🏆 Final Answer -> O(n^2)

# Example 3: T = 0.0001 * n * log(n) + 300n
# Step 1: Remove multipliers -> n*log(n) + n
# Step 2: Dominating term (n*log(n) grows faster than n) -> n*log(n)
# 🏆 Final Answer -> O(n log n)

# Example 4. T = 0.0001*n*log(n) + 300n
# Calculation -> 0.0001*n*log(n) + 300n --> 0.0001*n*log(n) --> n*log(n)
# 🏆 Final Answer -> O(n log n)

# Example 5. T = 2n^30 + 3^n
# Calculation -> 2n^30 + 3^n -> 3^n (For large values of input 'n', exponential dominates polynomial)
# 🏆 Final Answer -> O(3^n)


# ==================================================================================
# 📊 TYPES OF ORDER OF GROWTH & GRAPHS
# ==================================================================================
# 1. Constant
# 2. Linear
# 3. Quadratic
# 4. Logarithmic
# 5. n log(n)
# 6. Exponential

# ----------------------------------------------------------------------------------
# 1. CONSTANT -> O(1)
# ----------------------------------------------------------------------------------
# Example -> The time taken to retrieve a particular item from an array via indexing.
# Why is it constant? -> Because an array uses contiguous memory allocation.
# Mathematical Logic: 
# Target Index Address = (Address of first item) + (bit-size * target index).
# This is just a single, direct arithmetic operation that does not require looping 
# or checking the len(array).

"""
T = c -> Graph
T(Time)
|          
|        
|********************  
|  
|  
|____________________ n(input)
"""

# ----------------------------------------------------------------------------------
# 2. LINEAR -> O(n)
# ----------------------------------------------------------------------------------
# Example -> Linear search.
# Time taken to compare elements one by one in an array.
# If array size doubles -> Time doubles.

"""
# T = n -> Graph
# T(Time)
# |          *
# |        *
# |      *
# |    * 
# |  *
# |*____________________ n(input)
"""

# ----------------------------------------------------------------------------------
# 3. QUADRATIC -> O(n^2)
# ----------------------------------------------------------------------------------
# Example -> Nested loops (like Bubble Sort).
# If input doubles -> Time = input^2 (quadruples).

"""
# T = n^2 -> Graph
# T(Time)
# |        *
# |        *
# |       *
# |     * 
# |   *
# |*____________________ n(input)
"""

# ----------------------------------------------------------------------------------
# 4. LOGARITHMIC -> O(log n)
# ----------------------------------------------------------------------------------
# Example -> Binary search.
# Behavior: 
# Input ->  10    100    1000  (Input grows by multiplication)
# Time  ->   1      2       3  (Time grows only by addition)

"""
# T = log(n) -> Graph
# T(Time)
# |                               *
# |                        *
# |                  *
# |            *
# |        *  
# |      *
# |___ *___________________________ n(input)
# |  *
# | *
"""

# ----------------------------------------------------------------------------------
# 5. LINEARITHMIC -> O(n log n)
# ----------------------------------------------------------------------------------
# Example -> Fast sorting algorithms (Merge sort, Quick sort).
# O(n log n) is worse than Linear O(n), but significantly better than Quadratic O(n^2).

"""
# T = nlog(n) -> Graph
# T(Time)
# |               *
# |              *
# |             *
# |            *
# |          *  
# |        *
# |___  *__________________________ n(input)
# |   *
# |*
"""

# ----------------------------------------------------------------------------------
# 6. EXPONENTIAL -> O(c^n)
# ----------------------------------------------------------------------------------
# Example -> Fibonacci calculation using pure recursion (not using memoization).
# Behavior: (Very, very worst)
# Input ->   1      2       3       4     (Input grows by addition)
# Time  ->  10    100    1000   10000     (Time grows by multiplication)
# This is the exact opposite behavior of Logarithmic growth.

"""
# T = c^n -> Graph
# T(Time)
# |            *
# |           *
# |          *
# |        *
# |      *  
# |   *
# |*_____________________________ n(input)
"""

# ==================================================================================
# 🎯 CONCLUSION 
# ==================================================================================
# Efficiency Ranking (Best to Worst): 
# Constant O(1) > Logarithmic O(log n) > Linear O(n) > Linearithmic O(n log n) > Quadratic O(n^2) > Exponential O(c^n)



"""
====================================================================================
🧩 DSA MASTERCLASS: TIME COMPLEXITY PRACTICE & DERIVATIONS
====================================================================================
Description: 18 Practical examples of calculating Time Complexity (Big O Notation).
Methodology: I use "First Principles" to strictly derive how the loop/algorithm 
             behaves mathematically before dropping constants.
====================================================================================
"""

# ==================================================================================
# 1. TWO INDEPENDENT LOOPS
# ==================================================================================
L = [1, 2, 3, 4]

sum = 0
for i in L: # O(n)
    sum = sum + i
print(sum)

product = 1
for i in L: # O(n)
    product = product * i
print(product)

# 🧠 First Principle Derivation:
# - Loop 1 runs 'n' times. (n ops)
# - Loop 2 runs 'n' times completely independently. (n ops)
# - Total Equation: T(n) = n + n = 2n
# - Rule: Drop the multiplicative constant (2).
# 🏆 Final Complexity -> O(n) (Linear)


# ==================================================================================
# 2. NESTED LOOPS (SAME ARRAY)
# ==================================================================================
L = [1, 2, 3, 4, 5]

for i in L: # Outer
    for j in L: # Inner
        print(f"{i}, {j}")

# 🧠 First Principle Derivation:
# - Outer loop runs 'n' times.
# - For EVERY single iteration of the outer loop, the inner loop runs 'n' times.
# - Total Equation: T(n) = n * n = n^2
# 🏆 Final Complexity -> O(n^2) (Quadratic)


# ==================================================================================
# 3. LINEAR SEARCH
# ==================================================================================
# 🧠 First Principle Derivation:
# - In the worst-case scenario, the element is at the very end of the list or missing.
# - The CPU must check exactly 'n' elements one by one.
# - Total Equation: T(n) = n
# 🏆 Final Complexity -> O(n) (Linear)


# ==================================================================================
# 4. INTEGER TO STRING CONVERSION (Division by 10)
# ==================================================================================
def intToStr(i):
    digits = "0123456789"
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10  # Shrinking input by factor of 10
    return result

# 🧠 First Principle Derivation:
# - Input (i) -> 123 | 1230 | 12300 | 123000 (Multiplication in input)  |
# - Loop runs ->  3  |   4  |   5   |   6    (Addition in time)         | --> Input * 10 -> T + 1
# - The loop runs exactly the number of digits in the integer.
# - Number of digits in a base-10 number 'N' is roughly log10(N).
# - Total Equation: T(N) = log10(N)
# 🏆 Final Complexity -> O(log n) (Logarithmic)


# ==================================================================================
# 5. MIXED LOOPS (Linear + Logarithmic)
# ==================================================================================
# n = 1000
# for(i = n/2; i <= n; i++){          # Outer loop
#     for(j = 2; j <= n; j = j*2){    # Inner loop
#         k = k + n/2
#     } 
# } 

# 🧠 First Principle Derivation:
# - Outer loop runs from n/2 to n. Total steps = n - n/2 = n/2.
# - Inner loop doubles 'j' each time: 2, 4, 8, 16... n.
#   It takes 'k' steps where 2^k = n, so k = log2(n).
# - Total Equation: T(n) = (n/2) * log2(n)
# - Rule: Drop the constant (1/2).
# 🏆 Final Complexity -> O(n log n) (Linearithmic)


# ==================================================================================
# 6. BINARY SEARCH
# ==================================================================================
# 🧠 First Principle Derivation:
# - Search space halves each step: n -> n/2 -> n/4 -> ... -> 1
# - How many times can you divide 'n' by 2 until it reaches 1?
# - Equation: n / (2^k) = 1 => 2^k = n => k = log2(n).
# - Total Equation: T(n) = log2(n)
# 🏆 Final Complexity -> O(log n) (Logarithmic)


# ==================================================================================
# 7. DEPENDENT NESTED LOOPS
# ==================================================================================
L = [1, 2, 3, 4, 5]

for i in range(0, len(L)): 
    for j in range(i+1, len(L)): 
        print(f"({L[i]}, {L[j]})")

# 🧠 First Principle Derivation:
# - When i=0, inner runs (n-1) times.
# - When i=1, inner runs (n-2) times.
# - When i=n-1, inner runs 0 times.
# - Total Equation (Sum of first n-1 integers): (n-1)(n)/2 = (n^2 - n) / 2
# - Rule: Drop denominator constant -> n^2 - n
# - Rule: Keep only the dominating term (n^2).
# 🏆 Final Complexity -> O(n^2) (Quadratic)


# ==================================================================================
# 8. NESTED LOOPS (DIFFERENT ARRAYS)
# ==================================================================================
A = [1, 2, 3, 4]      # length a
B = [2, 3, 4, 5, 6]   # length b

for i in A: 
    for j in B: 
        pass

# 🧠 First Principle Derivation:
# - Outer loop runs 'a' times. Inner loop runs 'b' times.
# - Total Equation: T(a,b) = a * b
# - If arrays are assumed to be roughly the same size (n), it becomes n^2.
# 🏆 Final Complexity -> Exact: O(A * B) | General: O(n^2)


# ==================================================================================
# 9. TRIPLE NESTED WITH CONSTANT INNER
# ==================================================================================
A = [1, 2, 3, 4]
B = [4, 5, 6, 7, 8]
for i in A: # len a
    for j in B: # len b
        for k in range(10000): # Constant 10,000 ops
            if i < j:
                print(f"({i}, {j})")

# 🧠 First Principle Derivation:
# - Total Equation: T(a,b) = a * b * 10000
# - Rule: Drop the massive multiplicative constant 10000.
# 🏆 Final Complexity -> Exact: O(A * B) | General: O(n^2)


# ==================================================================================
# 10. HALF-ARRAY LOOP (Two-Pointer / Reversal)
# ==================================================================================
L = [1, 2, 3, 4, 5]

for i in range(0, len(L)//2): # O(n/2)
    other = len(L) - i - 1 # Swapping elements
    temp = L[i]
    L[i] = L[other]
    L[other] = temp

print(L)

# 🧠 First Principle Derivation:
# - The loop runs exactly n/2 times.
# - Inside the loop, swapping takes 3 constant assignments = 3 ops.
# - Total Equation: T(n) = 3 * (n/2) = 1.5n
# - Rule: Drop the constant 1.5.
# 🏆 Final Complexity -> O(n) (Linear)


# ==================================================================================
# 11. RECURSIVE FACTORIAL
# ==================================================================================
def factorial(n):
    if n == 1: 
        return 1
    else: 
        return n * factorial(n - 1)

# 🧠 First Principle Derivation:
# - Function calls itself with n-1, n-2, ..., 1.
# - Total Function Calls = n.
# - Work done inside each call = 1 multiplication (O(1)).
# Input ->            5   10   100   200
# Function Calls ->   5   10   100   200
# - Total Equation: T(n) = n * 1 = n.
# 🏆 Final Complexity -> O(n) (Linear)


# ==================================================================================
# 12. PURE RECURSIVE FIBONACCI
# ==================================================================================
def fib(n):
    if n == 1 or n == 0: 
        return 1
    else: 
        return fib(n-1) + fib(n-2)

# 🧠 First Principle Derivation:
# - Every function call branches out into exactly 2 more function calls.
# - This creates a massive Tree Structure.
# - Level 1: 1 call. Level 2: 2 calls. Level 3: 4 calls... Level n: 2^n calls.
# Input ->            1   2   3    5      6       (Addition in input)                 |
# Function Calls ->   1   2   4   14  around 32   (Multiplication in function calls)  | -> Property of exponential
# - Total Equation: Nodes in a binary tree of height n bounded by 2^n.
# 🏆 Final Complexity -> O(2^n) (Exponential) 
# Note: log(<2^n) is exact Time Complexity


# ==================================================================================
# 13. RECURSIVE POWER (HALVING)
# ==================================================================================
def power(num):

    if num < 1:
        return 0
    elif num == 1:
        print(1)
        return 1
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr

# 🧠 First Principle Derivation:
# - Input cuts in half every call: num -> num/2 -> num/4 -> 1.
# - Input * 10 = Output Time + 1 (Logarithmic Property).
# Input ->            10   100   1000   (Multiplication in input)   |
# Function Calls ->   4     8     12    (Addition in output)        | -> Property (log)
# - Total Equation: 2^k = num => k = log2(num).
# 🏆 Final Complexity -> O(log n) (Logarithmic)


# ==================================================================================
# 14. MATHEMATICAL MODULO
# ==================================================================================
def mod(a, b):
    div = a // b
    return a - div * b

# 🧠 First Principle Derivation:
# - Only basic arithmetic operations are performed (2 ops).
# - Total Equation: T(n) = 2.
# - Rule: Drop additive constant, leaves 1.
# 🏆 Final Complexity -> O(1) (Constant)


# ==================================================================================
# 15. SUM OF DIGITS
# ==================================================================================
def sum_digits(num):
    while (num > 0):
        sum += num % 10
        num /= 10

# 🧠 First Principle Derivation:
# - Exactly like Problem 4, the number is shrinking by a factor of 10.
# - Loop runs for the number of digits in 'num'.
# 🏆 Final Complexity -> O(log n) (Logarithmic)


# ==================================================================================
# 16. RECURRENCE RELATION: T(n) = 3T(n-1)
# ==================================================================================
# Solution ->
# n = 3 -> t secs (Assume)
# n = 4 -> 3t secs
# n = 5 -> 9t secs
# n = 6 -> 27t secs

# Addition in Input -> Multiplication in Output
# Time complexity -> O(c^x) (Exponential)

# 🧠 First Principle Mathematical Derivation:
# T(n) = 3 * T(n - 1)
#      = 3 * [3 * T(n - 2)] = 3^2 * T(n - 2)
#      = 3^2 * [3 * T(n - 3)] = 3^3 * T(n - 3)
#      ... repeating 'k' times ...
#      = 3^k * T(n - k)
# We stop when n - k = 0 (Base Case), which means k = n.
#      = 3^n * T(0) = 3^n * 1
# 🏆 Final Complexity -> O(3^n) (Exponential)


# ==================================================================================
# 17. RECURRENCE RELATION: T(n) = 2T(n-1) - 1
# ==================================================================================
# 🧠 First Principle Mathematical Derivation:
# T(n) = 2T(n-1) - 1
#      = 2[2T(n-2) - 1] - 1 = 2^2 T(n-2) - 2 - 1
#      = 2^2[2T(n-3) - 1] - 2 - 1 = 2^3 T(n-3) - 2^2 - 2^1 - 2^0
#      ... repeating 'n' times ...
#      = 2^n * T(0) - (2^(n-1) + 2^(n-2) + ... + 2^1 + 2^0)
# (Note: The sum of geometric series 2^0 + 2^1 ... 2^(n-1) = 2^n - 1)
#      = 2^n - (2^n - 1)
#      = 2^n - 2^n + 1 = 1
# 🏆 Final Complexity -> O(1) (Constant)


# ==================================================================================
# 18. GENERATING POWER SETS
# ==================================================================================
# 🧠 First Principle Derivation:
# - A set of size 'n' has exactly 2^n possible subsets.
# - Example: {A, B} -> {}, {A}, {B}, {A,B} (Input 2 -> Output 4)
# - Example: {A, B, C} -> 8 subsets.
# Input ->   1   2   3   4  (Addition in input)         |
# output ->  1   2   4   8  (Multiplication in output)  | -> Pattern -> exponential
# - Since the algorithm must mathematically generate each subset, it must run 2^n times.
# 🏆 Final Complexity -> O(2^n) (Exponential)


# ==================================================================================
# 🚀                            END OF MASTERCLASS
# ==================================================================================
# "If you can calculate the Time Complexity of your code without running it, 
# you are great"
# 
# ✅ MILESTONE UNLOCKED: 
# You now possess the analytical vision to look at any 'for loop', 'while loop', 
# or 'recursive function' and instantly predict how it will behave when given 
# 1 Million data points. 
# 
# ⏭️ WHAT'S NEXT IN THE VAULT? 
# - Space Complexity (RAM optimization)
# - Core Data Structures (Arrays, Linked Lists, HashMaps)
# - Advanced Algorithmic Patterns (Two-Pointer, Sliding Window)
# 
# 🛡️ Keep building. Keep optimizing. 
# ==================================================================================

