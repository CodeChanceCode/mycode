#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/search"

def equipment(data):
    for item in data:
        print("Name:", item["name"])
        print("Description:", item["description"])
        if "attack" in item:
            print("Attack:", item["attack"])
        if "defense" in item:
            print("Defense:", item["defense"])
        print("\n")

def main():
    keyword = input("Enter a keyword to search for equipment items: ")
    search = {"keyword": keyword}
    resp = requests.post(URL, json=search)

    if resp.status_code == 200:
        equipment_data = resp.json()
        if equipment_data:
            equipment(equipment_data)
        else:
            print("No equipment items found.")
    else:
        print("Error occurred while fetching the data.")

if __name__ == "__main__":
    main()