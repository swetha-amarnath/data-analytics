import matplotlib.pyplot as plt

Test = ["Cycle test-1", "Cycle test-2", "Cycle test-3", "Cycle test-4"]
Marks = [89.8, 95.3, 68.8, 100]

# Generating the y positions. Later, we'll use them to replace them with labels.
y_positions = range(len(Test))

# Creating our bar plot
plt.bar(y_positions, Marks)
plt.xticks(y_positions, Test)
plt.ylabel("Percentage (%)")
plt.title("Annual cycle test performance")
plt.show()