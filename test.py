import requests

def api_calls():
    base_url = 'https://jsonplaceholder.typicode.com/posts/1'  # Update post with ID 1
    payload = {'title': 'Updated Title','body': 'This is the updated body content', 'userId': 1}
    
    response = requests.put(url=base_url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("Updated Data:", data)
    else:
        print("Failed to update the resource. Status Code:", response.status_code)

def main():
    try:
        api_calls()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
