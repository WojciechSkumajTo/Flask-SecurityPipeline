from flask import Flask, jsonify, request

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)

# Endpoint główny
@app.route('/')
def index():
    return jsonify({"message": "Hello, OWASP ZAP!"})

# Endpoint do logowania
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    if username == 'admin' and password == 'password':
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Endpoint dla użytkownika
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {1: {"name": "John Doe"}, 2: {"name": "Jane Doe"}}
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Uruchamianie aplikacji
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
