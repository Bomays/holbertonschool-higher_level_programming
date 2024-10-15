#!/usr/bin/python3
"""A first Flask API """


from flask import Flask, jsonify, request

"""from collections import OrderedDict"""

app = Flask(__name__)

"""app.config['JSON_SORT_KEYS'] = False
Disable JSON key sorting as alphabetical as OrderedDict"""


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
def get_user(username):
    """Return the user object for the given username"""
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the dict."""
    data = request.get_json()
    username = data.get(username)

    if not username:
        return jsonify({"error": "Username is required"}), 400

    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = new_user

    return jsonify({"message": "User added", "user": new_user}), 200


if __name__ == "__main__":
    app.run(debug=True)
"""debug=True for flask automatisation and detailed errors"""
