from flask import Flask, request, jsonify

app = Flask(__name__)

# Test users (synthetic data)
users = {
    "user1": "test123",
    "user2": "test123",
    "user3": "test123",
    "user4": "test123",
    "user5": "test123",
    "user6": "test123",
    "user7": "test123",
    "user8": "test123",
    "user9": "test123",
    "user10": "test123",
    "user11": "test123",
    "user12": "test123",
    "user13": "test123",
    "user14": "test123",
    "user15": "test123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"status": "success", "user": username}), 200
    else:
        return jsonify({"status": "invalid credentials"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)