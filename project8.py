#Fetch and process API data

import json
import requests

# API endpoint
url = "https://randomuser.me/api/?results=5"

#Fetch data from API
response = requests.get(url)

#Check if request is successful

if response.status_code == 200:
    data = response.json()
    print("API data fetched successfully!!")

    #Print fetched data
    print(json.dumps(data,indent=4)) #All the fetched data of API will show in terminal

    #Process data
    users=[]
    for user in data['results']:
        users.append({
            "name":f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
            })

    #Save processed data to JSON
    with open("users.json","w") as f:
        json.dump(users,f,indent=4)

        print("\nProcessed data saved sucessfullly!!")
else:
    print(f"Error {response.status_code}! Unable to fetch data")

