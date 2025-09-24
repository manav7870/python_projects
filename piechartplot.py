import matplotlib.pyplot as plt

#Data : Fruit Sales Distribution

labels= ["Apple", "Banana", "Orange", "Grapes"]
sizes= [30, 25, 20, 25]
colors= ['red', 'yellow', 'orange', 'purple']

#Create a pie chart

plt.pie(sizes, labels=labels, autopct= '%1.1f%%', colors= colors, startangle= 30, wedgeprops= {'edgecolor': 'black'})

#Add Title
plt.title("Fruits Sales Distribution")

plt.show()