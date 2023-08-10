import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 15, 30]
colors = ['blue', 'green', 'yellow', 'red']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')
plt.show()
