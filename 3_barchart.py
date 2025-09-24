import matplotlib.pyplot as plt

#Sample data (Categories and Values)
categories = ["Apple", "Banana", "Orange","Grapes"]
values = [50,80,90,60]

#Create a bar chart
plt.bar(categories, values, color=['red', 'yellow', 'orange', 'purple'], edgecolor='black')

# Customize the chart
plt.xlabel("Fruits") # X-axis label
plt.ylabel("Quantity Sold") # Y-axis label
plt.title("Fruit Sales Data") # Chart Title
plt.grid(axis='y', linestyle='--',alpha=0.1) # add horizontal grid lines

# Show the plot
plt.show()