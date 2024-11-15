import requests

def api_calls():
    base_url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'
    response = requests.get(url=base_url)
    data = response.json()
    # print(data)

    if data.get("success") and "data" in data:
        product_data = data["data"]
        print(f"Id : {product_data['id']}\nTitle : {product_data['title']}\nSuccess : {data['success']}\nBrand : {product_data['brand']}")
    else:
        raise Exception("Failed to fetch the data!")

def main():
    try:
        api_calls()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
