from flask import Flask, jsonify, request

app = Flask(__name__)

# User data storage
users = []

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists'}), 400

    # Create a new user
    user = {'username': username, 'password': password}
    users.append(user)

    return jsonify({'message': 'Registration successful'}), 200

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find user by username and password
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)

    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# List users endpoint
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users), 200

# Delete user endpoint
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)

    if user:
        users.remove(user)
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# API endpoint
@app.route('/api', methods=['GET'])
def api_endpoint():
    # Your API logic here
    # Perform any necessary data processing or actions

    # Return API response
    api_data = {'message': 'This is the API endpoint'}
    return jsonify(api_data), 200

if __name__ == '__main__':
    app.run(debug=True)
