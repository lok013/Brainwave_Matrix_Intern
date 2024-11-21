# chatgpt
import requests

def api_delete():
    # Replace with the actual URL of the resource to delete
    base_url = 'https://api.example.com/resource/123'  # Example URL with resource ID 123
    
    # Sending DELETE request
    response = requests.delete(url=base_url)
    
    if response.status_code == 200:
        print("Resource deleted successfully.")
    else:
        print(f"Failed to delete the resource. Status code: {response.status_code}")

def main():
    api_delete()

if __name__ == "__main__":
    main()
