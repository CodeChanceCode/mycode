#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/search"

def equipment(data):
    for item in data:
        print("Name:", item["name"])
        print("Description:", item["description"])
        if "attack" in item and item["attack"] > 0:
            print("Attack:", item["attack"])
        if "defense" in item and item["defense"] > 0:
            print("Defense:", item["defense"])
        print("\n")

def main():
    keyword = input("Enter a keyword to search for equipment items: ")
    search = {"keyword": keyword}
    response = requests.post(URL, json=search)

    equipment_data = response.json()
    if equipment_data:
        equipment(equipment_data)
    else:
        print("No equipment items found.")
    

if __name__ == "__main__":
    main()