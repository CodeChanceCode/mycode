#!/usr/bin/env python3

def main():

    print("Which Zelda: BOTW species are you?")
    print("Answer some questions and we will find out.")

    questions = [
        ("What is your favorite weapon?\n1. Sword 2. Spear 3. Scimitar 4. Hammer 5. Bow  6. No Weapon \nEnter 1, 2, 3, 4, 5 or 6: "),
        ("What is your preferred method of transportation?\n1. Horse 2. Swimming 3. Riding a Seal 4. Swimming 5. Flying 6. Walking \nEnter 1, 2, 3, 4, 5 or 6: "),
        ("What type of environment do you like?\n1. Mountains 2. Water 3. Desert 4. Dry and Hot 5. Sky 6. A little bit of everywhere \nEnter 1, 2, 3, 4, 5  or 6: ")
    ]

    species = {"Hylian" : 0, "Zora" : 0, "Gerudo" : 0, "Goron" : 0, "Rito" : 0, "Korok" : 0}

    questions_count = 0

    while questions_count < 3:
        question = questions[questions_count]
        answer = input(question)
        if answer == "1":
            species["Hylian"] += 1
        elif answer == "2":
            species["Zora"] += 1
        elif answer == "3":
            species["Gerudo"] += 1
        elif answer == "4":
            species["Goron"] += 1
        elif answer == "5":
            species["Rito"] += 1
        elif answer == "6":
            species["Korok"] += 1
        else:
            print("Invalid answer. Please enter a number between 1 and 6.")
        questions_count += 1

    result_species = max(species, species.key())

    print(f"Based on your answers, you are a {result_species}!")

main()
