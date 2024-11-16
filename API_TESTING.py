import requests

def api_calls():
    base_url = 'https://api.freeapi.app/api/v1/kitchen-sink/http-methods/put'
    payload = {'connection': 'none'}  # Example payload, you may adjust it as needed
    response = requests.put(url=base_url, json=payload)  # Use PUT instead of GET
    try:
        data = response.json()  # Attempt to parse the response as JSON
        print(data)

        if data.get("success") and "data" in data:
            product_data = data["data"]
            print(f"Method : {product_data['method']}\nSomething : {product_data['headers']['connection']}")
        else:
            raise Exception("Failed to fetch the data!")
    except ValueError:
        print("Error: Response is not in valid JSON format.")

def main():
    try:
        api_calls()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
