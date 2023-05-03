#!/usr/bin/env python
"""Zelda BOTW Equipment"""

import json
import random
import requests
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/equipment")
def list_equipment():
    if request.method == "POST":
        filter_type = request.form.get("filter", "all")
    else:
        filter_type = request.args.get("filter", "all")

    url = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
    response = requests.get(url)
    data = response.json()

    if filter_type == "attack":
        filtered_equipment = [item for item in equipment if "attack" in item and item["attack"] > 0 and item["defense"] == 0]
    elif filter_type == "defense":
        filtered_equipment = [item for item in equipment if "defense" in item and item["defense"] > 0 and item["attack"] == 0]
    else:
        filtered_equipment = data["data"]    
    
    return render_template("equipment.html", equipment=filtered_equipment)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2224)
