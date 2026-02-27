import numpy as np
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("shape: ", scores.shape)
print("Total elements: ", scores.size)
print("Highest score: ", np.max(scores))
print("Lowest score: ", np.min(scores))
print("Range: ", np.ptp(scores))