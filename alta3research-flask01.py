#!/usr/bin/env python
"""Zelda BOTW Equipment"""

import json
import random
import requests
from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/equipment", methods=["GET","POST"])
def list_equipment():
    
    filter_type = request.form.get("filter", "all")

    url = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
    response = requests.get(url)
    data = response.json()

    filtered_equipment = [
        item for item in data["data"]
        if (filter_type == "attack" and (item.get("attack") or 0) > 0 and (item.get("defense") or 0) == 0) or
           (filter_type == "defense" and (item.get("defense") or 0) > 0 and (item.get("attack") or 0) == 0)
    ]
    
    random_item = random.choice(filtered_equipment)

    return render_template("random_equipment.html", equipment=random_item, filter_type=filter_type)

@app.route("/search", methods=["GET", "POST"])
def search_equipment():
    if request.method == "POST":
        keyword = request.json.get("keyword", "").lower()
    else:
        keyword = request.args.get("keyword", "").lower()

    if not keyword:
        return jsonify({"error": "No keyword provided. Please provide a keyword to search for equipment items."})

    url = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
    response = requests.get(url)
    data = response.json()

    matching_items = [
        item for item in data["data"]
        if keyword in item["name"].lower() or keyword in item["description"].lower()
    ]

    return jsonify(matching_items)
    
@app.route("/search_results", methods=["GET"])
def search_results():
    keyword = request.args.get("keyword", "").lower()
    matching_items = search_equipment().json
    return render_template("search_result.html", search_results=matching_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2224, debug=True)
