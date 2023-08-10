import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 30, 12, 8, 25]

plt.bar(categories, values, color='green')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot')
plt.grid(True)
plt.show()
