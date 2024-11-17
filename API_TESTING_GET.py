import json

def api_calls():
    # Open the local JSON file
    try:
        with open('API_Data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception("The file 'API_Data.json' was not found!")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON from the file!")

    # Check if the necessary keys exist in the data
    if data.get("success") and "data" in data:
        product_data = data["data"]
        print(f"Method : {product_data['method']}\nConnection : {product_data['headers']['connection']}")
    else:
        raise Exception("Failed to fetch the data!")

def main():
    try:
        api_calls()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
