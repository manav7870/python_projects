#Read and write JSON file
import json

with open("data.json","r") as f:
    data = json.load(f)
    print("Original Data: ")
    print(data)

# Modify or add data 
data["Year"]="1st"

# Write to a new json file
with open("updated_data.json","w") as f:
    json.dump(data,f,indent=2)
print("\nUpdated JSON Saved!!")
