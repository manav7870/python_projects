import matplotlib.pyplot as plt

#Sample Data
x = [1,2,3,4,5] #X-axis values
y= [10,20,30,40,50] #Y-axis Values

# Create a line plot
plt.plot(x,y,marker='o', linestyle='-',color='b', linewidth=2, markersize=8,label="Sales Trend")

#Customize the plot
plt.xlabel("Days") #X-axis label
plt.ylabel("Sales") #Y-axis label
plt.title("Sales over time") #Title
plt.legend() #Show legend
plt.grid(True) #Show grid

#Show the plot
plt.show()
