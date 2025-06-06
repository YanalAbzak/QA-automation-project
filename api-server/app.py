from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}
counter = 1

@app.route("/users", methods=["POST"])
def create_user():
    global counter
    data = request.json
    data["id"] = counter
    users[counter] = data
    counter += 1
    return jsonify(data), 201

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    user.update(data)
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return "", 204
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)