#!/usr/bin/python3
"""You are a chef on a mission to cook a delicious 
meal for a food critic who will be visiting your restaurant."""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    CHEF GAME
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # CJ- print the move count
    print('Moves:', move_count)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    #CJ-ADDED FOR LOOP TO SHOW MULTIPLE ITEMS
    if "items" in rooms[currentRoom]:
        for item in rooms[currentRoom]['items']:
            print('You see a ' + item)
    print("---------------------------")

inventory = []

rooms = {

            'Kitchen' : {
                  'north' : 'Pantry',
                  'east'  : 'Dining Room',
                  'items'  : ['knife', 'spatula']
                },

            'Pantry' : {
                  'south' : 'kitchen',
                  'items'  : ['flour', 'sugar', 'egg', 'butter']
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'south': 'Garden',
                  'items' : ['tablecloth', 'plates', "glasses"]
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'items' : ['tomato', 'basil', 'shovel', 'shears']
            }
         }

#CJ- A dictionary that contains descriptions for the items
item_descriptions = {}

# start the player in the Pantry
currentRoom = 'Pantry'

#CJ-start the player with zero moves
move_count = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #CJ-move_count goes up one after move is made
    move_count += 1

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
            #add the item to their inventory
            inventory.append(move[1])
            print(move[1] + ' got!')
            #CJ- checking if item is in item description dict
            if move[1] in item_descriptions:
                print(item_descriptions[move[1]])
            #CJ- removes the specific item instead of deleting the all items
            rooms[currentRoom]['items'].remove(move[1])
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break


    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

#Add count of how many "moves" the player has made. COMPLETE
#Find a way to have multiple items inside the same room. COMPLETE
#Find a way to add descriptions to items that display when the item is picked up. COMPLETE

