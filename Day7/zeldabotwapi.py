#!/usr/bin/env python3

import requests

def main():
    entry_name = input("Enter the name of an entry from BOTW:\n>")
    formatted_entry_name = entry_name.replace(" ", "_")
    entry_data = requests.get(f"https://botw-compendium.herokuapp.com/api/v2/entry/{formatted_entry_name}")
    entry_data_obj = entry_data.json()

    if "data" in entry_data_obj:
        if entry_data["data"]:
            entry_data = entry_data["data"][0]
            # Print entry name and image URL
            print(f"{entry_data['name']} image- {entry_data['image']}")

            # Print some of the entry's attributes
            print(f"Description: {entry_data['description']}")
            print(f"Common locations: {entry_data['common_locations']}")
            print(f"Sell price: {entry_data['sell_price']} rupees")
            print(f"Category: {entry_data['category']}")
            print(f"Acquired from: {entry_data['acquired_from']}")

            if "cooking_effect" in entry_data:
                print(f"Cooking effect: {entry_data['cooking_effect']}")
            else:
                print("This entry is not a food item.")
        else:
            print(f"No entry found for {entry_name}")
    else:
        print(f"Error {entry_data['status']}: {entry_data['error']}")

if __name__ == "__main__":
    main()
