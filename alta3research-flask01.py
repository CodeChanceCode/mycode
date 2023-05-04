#!/usr/bin/env python
"""Zelda BOTW Equipment"""

import json
import random
import requests
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/equipment", methods=["GET","POST"])
def list_equipment():
    if request.method == "POST":
        filter_type = request.form.get("filter", "all")
    else:
        filter_type = request.args.get("filter", "all")

    url = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
    response = requests.get(url)
    data = response.json()

    if filter_type == "attack":
        filtered_equipment = [item for item in data["data"] if "attack" in item and item["attack"] > 0 and item["defense"] == 0]
    elif filter_type == "defense":
        filtered_equipment = [item for item in data["data"] if "defense" in item and item["defense"] > 0 and item["attack"] == 0]
    else:
        filtered_equipment = data["data"]    
    
    random_item = random.choice(filtered_equipment)

    if filter_type == "attack":
        return render_template("equipment.html", equipment=random_item, filter_type="attack")
    elif filter_type == "defense":
        return render_template("equipment.html", equipment=random_item, filter_type="defense")

    return render_template("equipment.html", equipment=random_item)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2224, debug=True)
