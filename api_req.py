







import requests

BASE_URL = "https://api.test.com"

def register(username, password):
    register_url = f"{BASE_URL}/register"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(register_url, json=data)
    return response.json()

def login(username, password):
    login_url = f"{BASE_URL}/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, json=data)
    return response.json()

def create_user(token, username, password):
    create_user_url = f"{BASE_URL}/users"
    data = {
        "username": username,
        "password": password
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(create_user_url, json=data, headers=headers)
    return response.json()

def list_users(token):
    list_users_url = f"{BASE_URL}/users"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(list_users_url, headers=headers)
    return response.json()

# Delete user function
def delete_user(token, user_id):
    delete_user_url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(delete_user_url, headers=headers)
    return response.json()

username = "username"
password = "password"

register_response = register(username, password)
print("Register Response:", register_response)

login_response = login(username, password)
print("Login Response:", login_response)

token = login_response["data"]["token"]

new_username = "new_user"
new_password = "new_password"
create_user_response = create_user(token, new_username, new_password)
print("Create User Response:", create_user_response)

list_users_response = list_users(token)
print("List Users Response:", list_users_response)

user_id_to_delete = 1  # Assuming user ID 1 needs to be deleted
delete_user_response = delete_user(token, user_id_to_delete)
print("Deleted:", delete_user_response)





