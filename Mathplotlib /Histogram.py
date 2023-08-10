import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Random data

plt.hist(data, bins=20, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()
