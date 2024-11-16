import requests

def api_calls():
    base_url = 'https://api.freeapi.app/api/v1/kitchen-sink/http-methods/get'
    response = requests.get(url=base_url)
    data = response.json()
    # print(data)

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
