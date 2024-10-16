#!/usr/bin/python3
"""Techniques for API Security and Authentication"""


from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import os
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

"""Initializing"""
app = Flask(__name__)
auth = HTTPBasicAuth()

"""Dictionnary structure used to store users
data in memory with hashed password"""
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash(""),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash(""),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """HTTPBasicAuth instance to first protect routes"""
    if username in users and (check_password_hash
                              (users.get(username), password)):
        return username
    return None


"""Public route for 'Welcome' endpoint """


@app.route("/", methods=["GET"])
def home():
    """function returning welcome message accessing home route"""
    return "Welcome!"


"""Protected route with basic authentification required"""


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


"""Set secret key outside the code while seting up JWT in flask """
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)


"""Public route with the user login required"""


@app.route("/login", methods=["POST"])
def login():
    """defines the token creating process with a provided payload"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"error": "wrong password or username"}), 401

    user = users.get(username)

    if user and check_password_hash(user, password):
        payload = {
            "username": username,
            "role": user.role,
        }
        access_token = (create_access_token
                        (identity=username, additional_claims=payload))
        return jsonify(access_token=access_token)

    return jsonify({"error": "wrong password or username"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"message": "User not found"}), 401

    if users[current_user]["role"] != "admin":
        return jsonify({"message": "Admin access required"}), 403
    else:
        return jsonify({"message": "Admin Access: Granted"})


if __name__ == "__main__":
    app.run(debug=True)
