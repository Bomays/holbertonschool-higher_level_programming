#!/usr/bin/python3
"""A first Flask API """


from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}


@app.route("/", methods=["GET"])
def home():
    """Return welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_json_data():
    """Return a list of usernames in JSON format"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return status message"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def user_profile(username):
    """Return the user object for the given username"""
    profile = users.get(username)

    if not profile:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(profile)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the dict."""
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        user_data = {
            "username": username,
            "name": user_data.get("name"),
            "age": user_data.get("age"),
            "city": user_data.get("city"),
        }

    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
"""debug=True for flask automatisation and detailed errors"""
