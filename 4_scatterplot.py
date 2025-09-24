import matplotlib.pyplot as plt
import numpy1 as np

#Sample data: X (study hours) and Y (test scores)
study_hours = [1,2,3,4,5,6,7,8,9,10]
test_scores = [50,55,65,70,72,78,80,85,88,95]

#Create scatter plot
plt.scatter(study_hours, test_scores, color='blue', marker='o', edgecolors='black', s=100, label="Students")

#Customize the plot
plt.xlabel("Study Hours") #X-axis label
plt.ylabel("Test Scores") #Y-axis label
plt.title("Study Hours vs Test Scores") #Add grid lines

#Show the plot
plt.show()