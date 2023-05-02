def main():
    name = input("Please enter your name:\n>").title()
    year = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    signs = {
        0: ("Rat", "artistic, sociable, industrious, charming, and intelligent"),
        1: ("Ox", "strong, thorough, determined, loyal, and reliable"),
        2: ("Tiger", "courageous, enthusiastic, confident, charismatic, and a leader"),
        3: ("Rabbit", "vigilant, witty, quick-minded, and ingenious"),
        4: ("Dragon", "talented, powerful, lucky, and successful"),
        5: ("Snake", "wise, like to work alone, and determined"),
        6: ("Horse", "animated, active, and energetic"),
        7: ("Sheep", "creative, resilient, gentle, mild-mannered, and shy"),
        8: ("Monkey", "sharp, smart, curious, and mischievous"),
        9: ("Rooster", "hardworking, resourceful, courageous, and talented"),
        10: ("Dog", "loyal, honest, cautious, and kind"),
        11: ("Pig", "a symbol of wealth, honesty, and practicality")
    }
    sign = signs[(year - 4) % 12]
    print(f"{name}, your zodiac sign is {sign[0]}, you are {sign[1]}.")

main()

