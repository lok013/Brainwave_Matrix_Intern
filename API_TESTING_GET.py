import json

def api_calls():
    try:
        # Open the local JSON file
        with open('API_Data.json', 'r') as file:
            data = json.load(file)

        # Print the raw data to see the structure
        # print("Raw data from JSON file:", data)

    except FileNotFoundError:
        raise Exception("The file 'API_Data.json' was not found!")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON from the file!")

    # Check if the 'success' key exists and is True
    if data.get("success"):
        print("Success key is found and its value is:", data["success"])
    else:
        raise Exception("'success' key is missing or its value is not True!")

    # Now check if the 'users' key exists and access elements directly
    if "users" in data:
        # Access the first user directly
        user1 = data["users"][0]
        print(f"User ID: {user1['id']}, Name: {user1['name']}, Email: {user1['email']}")

        # Access the second user directly
        user2 = data["users"][1]
        print(f"User ID: {user2['id']}, Name: {user2['name']}, Email: {user2['email']}")
    else:
        raise Exception("'users' key is missing in the data!")

def main():
    try:
        api_calls()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
