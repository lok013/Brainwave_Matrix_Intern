import requests
import json  # For saving data in JSON format

BASE_URL = "https://api.socialverseapp.com"
API_KEY = "flic_1e01009f9c1a54706f385bcc1993a08fd9647ba8f499572d280654d1c03c47bf"

headers = {
    'Flic-Token': API_KEY
}

# Function to get all viewed posts
def get_all_viewed_posts():
    url = f"{BASE_URL}/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching viewed posts: {response.status_code}")
        return None

# Function to get all liked posts
def get_all_liked_posts():
    url = f"{BASE_URL}/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching liked posts: {response.status_code}")
        return None

# Function to get all user ratings
def get_all_user_ratings():
    url = f"{BASE_URL}/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user ratings: {response.status_code}")
        return None

# Function to get all posts
def get_all_posts():
    url = f"{BASE_URL}/posts/summary/get?page=1&page_size=1000"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching posts: {response.status_code}")
        return None

# Function to get all users
def get_all_users():
    url = f"{BASE_URL}/users/get_all?page=1&page_size=1000"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching users: {response.status_code}")
        return None

# Fetching data from all endpoints
def fetch_all_data():
    viewed_posts = get_all_viewed_posts()
    liked_posts = get_all_liked_posts()
    user_ratings = get_all_user_ratings()
    posts = get_all_posts()
    users = get_all_users()

    return {
        "viewed_posts": viewed_posts,
        "liked_posts": liked_posts,
        "user_ratings": user_ratings,
        "posts": posts,
        "users": users
    }

# Main execution
if __name__ == "__main__":
    all_data = fetch_all_data()

    # Save data to files or process further
    if all_data:
        print("Fetched all data successfully!")
        # Write the data to JSON files, ensuring Unicode is handled correctly
        with open("viewed_posts.json", "w", encoding="utf-8") as f:
            json.dump(all_data["viewed_posts"], f, ensure_ascii=False, indent=4)
        with open('liked_posts.json', 'w', encoding="utf-8") as f:
            json.dump(all_data["liked_posts"], f, ensure_ascii=False, indent=4)
        with open('user_ratings.json', 'w', encoding="utf-8") as f:
            json.dump(all_data["user_ratings"], f, ensure_ascii=False, indent=4)
        with open('posts.json', 'w', encoding="utf-8") as f:
            json.dump(all_data["posts"], f, ensure_ascii=False, indent=4)
        with open('users.json', 'w', encoding="utf-8") as f:
            json.dump(all_data["users"], f, ensure_ascii=False, indent=4)
    else:
        print("Error: Failed to fetch data.")
