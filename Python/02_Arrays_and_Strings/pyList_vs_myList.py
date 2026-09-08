MyList = __import__("01_array_fundamentals").MyList
import time
import numpy as np

N = 1000000
print(f"--- Benchmarking for {N} items ---")

# 1. Python Default List
start = time.perf_counter()
py_list = list(range(N))
py_sum = sum(py_list)
py_time = time.perf_counter() - start
print(f"Python List Time: {py_time:.4f} seconds")

# 2. MyList (Custom Engine - using fixed capacity feature!)
start = time.perf_counter()
my_list = MyList(*(range(N)), capacity=N) 
my_sum = my_list.sum()
my_time = time.perf_counter() - start
print(f"MyList Time:      {my_time:.4f} seconds")

# 3. NumPy Array
start = time.perf_counter()
np_arr = np.arange(N)
np_sum = np.sum(np_arr)
np_time = time.perf_counter() - start
print(f"NumPy Time:       {np_time:.4f} seconds")