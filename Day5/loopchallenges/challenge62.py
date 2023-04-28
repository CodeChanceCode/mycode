#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

answer= input("Which farm would you like?\n")
vegetables = ["carrots", "celery"]

for farm in farms:
    if answer in farm["name"]:
         for animal in farm["agriculture"]:
             if animal not in vegetables:
                print(animal)

