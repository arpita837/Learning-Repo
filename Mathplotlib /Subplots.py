import matplotlib.pyplot as plt
import numpy as np

# Generating some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating subplots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Sine')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Cosine')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
