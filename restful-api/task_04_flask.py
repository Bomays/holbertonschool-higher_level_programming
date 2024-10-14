#!/usr/bin/python3
"""A first Flask API """


from pkgutil import get_data
from flask import Flask, jsonify, request

app = Flask(__name__)


users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}


@app.route("/", methods=["GET"])
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data", methods=["GET"])
def get_json_data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "<p>OK</p>"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error":"Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return jsonify({"message": "User added"}), 200


if __name__ == "__main__":
    app.run(debug=True)
"""debug=True for flask automatisation and detailed errors"""
