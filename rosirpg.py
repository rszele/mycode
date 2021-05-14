#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'north' : 'Broom Closet'
                  },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'Stranger',
                  'east'  :  'Bedroom',
          
                  },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
 
             'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'mace',
            }, 
            'Broom Closet': {
                  'south' : 'Hall',
                  'item'  : 'expended rounds',
           },
            'Bedroom'     : {
                'west'    : 'Kitchen',
                  'item'  : 'smoking gun',
           },


            
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Bedroom' and 'smoking gun' in inventory and 'expended rounds' in inventory:
    print('You escaped the house with the weaponry ... YOU WIN!')
    break


  if 'item' in rooms[currentRoom] and 'Stranger' in rooms[currentRoom]['item'] and "mace" in inventory:
    print('The Stranger has a knife... but YOU have Mace! You spray the Stranger in the face and he runs screaming into the wall. With a sickening crunch, he falls to the floor unconscious.')
    del rooms[currentRoom]['item']

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'Stranger' in rooms[currentRoom]['item']:
    print('A Stranger has got you... GAME OVER!')
    break


