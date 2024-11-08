import json
import csv
import os
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

    file_path = ""

    if source == "json":
        file_path = "products.json"

    elif source == "csv":
        file_path = "products.csv"

    else:
        return render_template("product_display.html", error="Wrong source")


    if not os.path.exists(file_path):
        return render_template("product_display.html", error="File not found")

    if source == "json":
        products = read_json(file_path)
    else:
        products = read_csv(file_path)

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found")

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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
