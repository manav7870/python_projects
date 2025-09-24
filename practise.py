import pandas as pd

csv_file = pd.read_csv("data.csv")
print("CSV FILE: ")
print(csv_file)

a = csv_file.to_excel("exfile.xlsx",index = True)
print(a)

print("\nEXCEL FILE: ")
b = pd.read_excel("exfile.xlsx")
print(b)