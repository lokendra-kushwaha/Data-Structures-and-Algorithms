# Time Complexity & Big O Notation

## What is Time Complexity?
Time complexity is not about measuring the exact time (in seconds) an algorithm takes to run. Instead, it measures **how the runtime grows as the size of the input (`n`) increases**.

## Big O Notation
Big O notation is used to describe the **worst-case scenario** (upper bound) of an algorithm's runtime. It focuses on the dominant term and ignores constants.

### Common Time Complexities (From Best to Worst)

| Notation | Name | Example | Description |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant Time | Accessing an array element `arr[0]` | Runtime stays the same regardless of input size. |
| **O(log n)** | Logarithmic Time | Binary Search | Input is halved in each step. Very efficient. |
| **O(n)** | Linear Time | Traversing an array (a simple `for` loop) | Runtime grows proportionally with the input size. |
| **O(n log n)** | Linearithmic Time | Merge Sort, Quick Sort | Often the best possible time for sorting algorithms. |
| **O(n²)** | Quadratic Time | Bubble Sort, Nested loops | Runtime grows exponentially. Bad for large inputs. |
| **O(2ⁿ)** | Exponential Time | Recursive Fibonacci | Runtime doubles with each addition to the input. |
| **O(n!)** | Factorial Time | Traveling Salesperson Problem | Extremely slow, unfeasible for large `n`. |

## Complexity Growth Visualization

Here is the exact growth visualization you referenced, showing how quickly numbers blow up for different complexities:

### Complexity Growth Table Data

| CLASS | n=10 | = 100 | = 1000 | = 1000000 |
| :--- | :--- | :--- | :--- | :--- |
| **O(1)** | 1 | 1 | 1 | 1 |
| **O(log n)** | 1 | 2 | 3 | 6 |
| **O(n)** | 10 | 100 | 1000 | 1000000 |
| **O(n log n)** | 10 | 200 | 3000 | 6000000 |
| **O(n^2)** | 100 | 10000 | 1000000 | 1000000000000 |
| **O(2^n)** | 1024 | 1267650600228229... | 1071508607186267... | <span style="color:red">**Good luck!!**</span> |

## Golden Rules for Calculating Big O
1. **Drop the Constants:** `O(2n)` becomes `O(n)`. `O(500)` becomes `O(1)`.
2. **Drop Non-Dominant Terms:** `O(n² + n + 5)` becomes `O(n²)`, because as `n` gets very large, the `n²` term dominates the runtime.