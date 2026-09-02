# 🚀 DSA Vault: Algorithmic Complexity

**Core Concept:** We evaluate algorithms based on their worst-case scalability (Big O) as input size grows to infinity, completely ignoring hardware speed.

## 📊 Big-O Hierarchy (Best to Worst)
| Complexity | Big O Notation | Real-World Example |
| :--- | :--- | :--- |
| **Constant** | `O(1)` | Array Indexing `arr[0]` |
| **Logarithmic** | `O(log n)` | Binary Search |
| **Linear** | `O(n)` | Linear Search / Single Loop |
| **Linearithmic** | `O(n log n)` | Merge Sort / Quick Sort |
| **Quadratic** | `O(n²)` | Nested Loops / Bubble Sort |
| **Exponential** | `O(cⁿ)` | Pure Recursive Fibonacci |

## 🧠 First-Principle Derivation Rules
1. **Drop Additive Constants:** `O(n + 5)` ➔ `O(n)`
2. **Drop Multiplicative Constants:** `O(3n)` ➔ `O(n)`
3. **Keep the Dominating Term:** `O(n² + n)` ➔ `O(n²)`

> **📂 Deep Dive Reference:** For the complete 18 step-by-step mathematical derivations and ASCII graphs, refer to my script: `time_complexity.py`