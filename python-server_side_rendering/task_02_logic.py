#!/usr/bin/python3
"""Flask application that displays items loaded from a JSON file."""

import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    """Render a simple home page."""
    return "<h1>Welcome to My Flask App</h1>"


@app.route("/items")
def items():
    """Load items from JSON and render the items page."""
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    item_list = data.get("items", [])

    return render_template("items.html", items=item_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
