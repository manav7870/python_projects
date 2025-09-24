import matplotlib.pyplot as plt
import numpy as np

#Generate random data (e.g. , student test scores)
data = np.random.normal(loc=70, scale=10, size=1000)

#Create histogram
plt.hist(data, bins=50, color='blue', edgecolor='black', alpha=0.7)

#Customize the plot
plt.xlabel("Test Scores") #X-axis label
plt.ylabel("Frequency") #Y-axis label
plt.title("Distribution of Student test scores") #Title
plt.grid(axis='y', linestyle='--', alpha=0.7) #Grid for better readability

#show the plot
plt.show()

