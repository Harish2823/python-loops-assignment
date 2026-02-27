import numpy as np
import time
np_array = np.arange(1, 50001)
py_list = list(range(1, 50001))

start_np = time.time()
np_sum = np.sum(np_array)
end_np = time.time()
np_time = end_np - start_np

start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()

py_time =end_py - start_py
speed_ratio = py_time / np_time if np_time != 0 else float('inf')

print("Numpy sum: ", np_sum)
print("Python sum: ", py_sum)
print(f"Numpy time: {np_time:.4f} seconds")
print(f"Python time: {np_time:.4f} seconds")
print(f"Numpy is {speed_ratio:.1f}x faster")
