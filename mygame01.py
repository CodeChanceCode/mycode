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
      cook [dish]
      set [item]
      look around
    ''')

def showStatus():
    """determine the current status of the player"""
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # CJ- print the move count
    print('Moves:', move_count)
    print('Inventory:', inventory)
    print("---------------------------")
    #CJ-ADDED FOR LOOP TO SHOW MULTIPLE ITEMS
    if "items" in rooms[currentRoom]:
        for item in rooms[currentRoom]['items']:
            print('You see ' + item)
    print("---------------------------")
    if 'event' in rooms[currentRoom] and rooms[currentRoom]['event'] is not None:
        print('Event: ' + rooms[currentRoom]['event'])        
        print("---------------------------")

inventory = []

rooms = {

            'Kitchen' : {
                  'north' : 'Pantry',
                  'east'  : 'Dining Room',
                  'down' : 'Wine Cellar',
                  'items' : ['knife', 'spatula', 'recipe book']
                },

            'Pantry' : {
                  'south' : 'Kitchen',
                  'items' : ['sugar', 'beef', 'cheese', 'noodles']
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'south': 'Garden',
                  'items' : [],
                  'event' : None,
                  'table' : [],
                  'furniture' : ['table']
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'items' : ['tomato', 'basil', 'shears']
            },
            'Wine Cellar' : {
                  'up'   : 'Kitchen',
                  'items': ['wine']
            }
         }

#CJ- A dictionary that contains descriptions for the items
item_descriptions = {
    'knife' : "A sharp knife for cutting.",
    'spatula' : "A spatula for flipping or stirring.",
    'sugar': 'Sugar to sweeten your dishes.',
    'beef': 'Looks like some good ground beef.',
    'tomato': 'Ripe tomato from the garden.',
    'basil': 'Fragrant basil, freshly picked.',
    'shears': 'Useful shears for harvesting fresh ingredients.',
    'recipe book' : 'A recipe book with one recipe: Pasta.',
    'wine' : 'A bottle of wine, pairs well with pasta.',
    'noodles' : 'Some handmade noodles for pasta.'
}

# start the player in the Pantry
currentRoom = 'Kitchen'

#CJ-start the player with zero moves
move_count = 0

#CJ- a max move limit 
max_moves = 30

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
    #CJ changed to maxsplit         
    move = move.lower().split(maxsplit=1)

    #CJ-move_count goes up one after move is made
    move_count += 1

    #CJ-the food critic arrives after so many moves
    if move_count >= 10 and rooms['Dining Room']['event'] is None:
        rooms['Dining Room']['event'] = 'food critic'
        print("The food critic has arrived in the Dining Room! Hopefully you've started cooking their meal...")

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
    #CJ- add only being able to get tomato or basil if they have shears first
    if move[0] == 'get' :
        if move[1] in ['tomato', 'basil'] and 'shears' not in inventory:
            print(f"You need shears to get the {move[1]}!")
        elif "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
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
    
    #CJ-shows the interactable furniture in the current room
    if move[0] == 'look':
        if move[1] == 'around':
            if 'furniture' in rooms[currentRoom]:
                print("You look around and see the following furniture:")
                for furniture in rooms[currentRoom]['furniture']:
                    print(furniture)
        else:
            print("There is no usable furniture in this room.")

    #CJ-new verb that allows you to set items on table in dining room, also adds more time to the moves count if you set wine down first
    if move[0] == 'set':
        if currentRoom == 'Dining Room':
            if move[1] in inventory and move[1] in ['pasta', 'wine']:
                # Place the item on the table and remove it from the inventory
                rooms[currentRoom]['table'].append(move[1])
                inventory.remove(move[1])
                print(f"{move[1]} has been placed on the table.")
                if move[1] == 'wine':
                    max_moves += 10
                    print("The food critic is enjoying the wine, you have more time to prepare the meal!")
            elif move[1] not in ['pasta', 'wine']:
                print("You can only place pasta or wine on the table.")
            else:
                print(f"You don't have {move[1]} in your inventory!")
        else:
            print("You can only place items on the table in the Dining Room.")

    #CJ- added new verb that allows you to cook pasta once all the ingredients are in inventory and in kitchen
    if move[0] == 'cook':
        if move[1] == 'pasta':
            required_ingredients = ['beef', 'sugar', 'cheese', 'tomato', 'noodles', 'basil']
            if all(ingredient in inventory for ingredient in required_ingredients): #CJ - checks if ALL conditions are true for both lists
                if currentRoom == 'Kitchen':
                    print("You cooked a delicious pasta dish!")
                    inventory.append('pasta')
                    for ingredient in required_ingredients:
                        inventory.remove(ingredient)
                else:
                    print("You can only cook pasta in the Kitchen.")
            else:
                print("You don't have all the ingredients to cook pasta.") 

    ##Define how the player can lose
    if rooms['Dining Room']['event'] == 'food critic' and move_count > max_moves:
        print("You took too long to prepare the meal... The food critic has left... YOU LOSE!")
        break
    

    ## Define how a player can win
    if currentRoom == 'Dining Room' and rooms[currentRoom]['event'] == 'food critic' and 'pasta' in rooms['Dining Room']['table']:
        print('You served the critic a delicious pasta dish with some tasty wine.... YOU WIN!')
        break

#Add count of how many "moves" the player has made. COMPLETE
#Add a way to have multiple items inside the same room. COMPLETE
#Add a way to add descriptions to items that display when the item is picked up. COMPLETE
#Add a wine cellar room that you go up or down for that extends the time the food critic is is willing at to wait. COMPLETE
#Add a way to lose that implements a total amount of moves. COMPLETE
#Add a way to announce that the food critic has arrived in the Dining Room after x amount of moves. Complete
#Add a way to cook items in the kitchen and receive a dish from them. complete
#Add a way to only be able to get the tomato and basil if you have the shears in your inventory. complete
#Add a way to 'look around' a room to see what interactable furniture there is. complete
#Add a way to display all the ways you can "go" while in a room- not complete