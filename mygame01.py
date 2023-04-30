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
    ''')

def showStatus():
    """determine the current status of the player"""
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # CJ- print the move count
    print('Moves:', move_count)
    print('Inventory:', inventory)
    #CJ-ADDED FOR LOOP TO SHOW MULTIPLE ITEMS
    if "items" in rooms[currentRoom]:
        for item in rooms[currentRoom]['items']:
            print('You see ' + item)
    print("---------------------------")

inventory = []

rooms = {

            'Kitchen' : {
                  'north' : 'Pantry',
                  'east'  : 'Dining Room',
                  'items'  : ['knife', 'spatula']
                },

            'Pantry' : {
                  'south' : 'Kitchen',
                  'items' : ['sugar', 'beef', 'cheese']
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'south': 'Garden',
                  'items' : ['tablecloth', 'plates', "glasses", "silverware"],
                  'event' : None
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'items' : ['tomato', 'basil', 'shears']
            }
         }

#CJ- A dictionary that contains descriptions for the items
item_descriptions = {
    'knife' : "A sharp knife for cutting.",
    'spatula' : "A spatula for flipping or stirring.",
    'sugar': 'Sugar to sweeten your dishes.',
    'beef': 'Looks like some good ground beef.',
    'tablecloth': 'An elegant tablecloth for setting the table.',
    'plates': 'Fine china plates for serving your dishes.',
    'glasses': 'Crystal glasses for serving drinks.',
    'tomato': 'Ripe tomato from the garden.',
    'basil': 'Fragrant basil, freshly picked.',
    'shears': 'Useful shears for harvesting fresh ingredients.',
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
    if move_count == 15:
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

    #CJ- added new verb that allows you to cook pasta once all the ingredients are in inventory and in kitchen
    if move[0] == 'cook':
        if move[1] == 'pasta':
            required_ingredients = ['beef', 'sugar', 'cheese', 'tomato', 'noodle', 'basil']
            if all(ingredient in inventory for ingredient in required_ingredients):
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
        print("You took too long to prepare the meal... The food critic has left. YOU LOSE!")
        break
    


    ## Define how a player can win
    if currentRoom == 'Dining Room' and rooms[currentRoom]['event'] == 'food critic' and 'pasta' in inventory:
        print('You served the critic a delicious pasta dish with some tasty wine.... YOU WIN!')
        break

#Add count of how many "moves" the player has made. COMPLETE
#Find a way to have multiple items inside the same room. COMPLETE
#Find a way to add descriptions to items that display when the item is picked up. COMPLETE
#Add a way to lose that implements a total amount of moves. COMPLETE
#Add a way to announce that the food critic has arrived in the Dining Room after x amount of moves. Complete
#Add a way to cook items in the kitchen and receive a dish from them.