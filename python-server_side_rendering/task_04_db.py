#!/usr/bin/python3
import json
import csv
import os
import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    try:
        with open("items.json") as f:
            data = json.load(f)

            items = data.get("items", [])
            return render_template("items.html", items=items)

    except FileNotFoundError:
        return "Items files not found", 400

    except json.JSONDecodeError:
        return "Error decoding JSON", 500


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        file_path = "products.json"
        if not os.path.exists(file_path):
            return render_template("product_display.html", error="file not found")

        products = read_json(file_path)
    
    elif source == "csv":
        file_path = "products.csv"
        if not os.path.exists(file_path):
            return render_template("product_display.html", error="file not found")

        products = read_json(file_path)

    elif source == "sql":
        products = read_sql()
        if products is None:
            return render_template("product_display.html", error="database error")
    
    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if int(p['id']) == product_id]
        if not products:
            return render_template(
                "product_display.html", error="Product not found"
                )

    return render_template("product_display.html", products=products)


# defining read_json and read_csv
def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def read_csv(file_path):
    products = []
    with open(file_path, mode="r", newline="", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)

    return products


def read_sql():
    try:
        with sqlite3.connect("products.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return render_template("product_display.html", products=products)

    except sqlite3.Error as e:
        return render_template("product_display.html", error="database error")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
