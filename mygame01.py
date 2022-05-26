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
  # This gives a brief description of current room
  print(rooms[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

# Player will have to answer the trivia question correctly in order to collect the item
def triviaFunction(triviaItem):
  print("---------------------------")
  print("To collect the prize you must answer the question correctly")
  print(triviaDict[triviaItem][0])
  answer= input(">")

  if answer.lower() == triviaDict[triviaItem][1]:
      print("Correct. Prize earned!!!")
  else:
      triviaFunction(triviaItem)

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Bedroom',
                  'item'  : 'key',
                  'description' : 'a very dark hall and must move with precaution. Making the wrong move could                                   be fatal so follow instructions carefully. South of this room is the
                                   kitchen. Going east will lead to dining room and west will be the bedroom',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'description': 'the real place where the magic happens. Grab a quick bite before continuing
                                  your adventure. Once you\'re satiated remember where you stand. West of this                                  room is the hall, north is the pantry and south is the garden where you will                                  go once you collect all the items',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
              },
            'Bedroom' : {
                  'east' : 'Hall',
                  'item' : 'flashlight',
              },
         }

triviaDict = {
        'flashlight' : ['According to greek mythology, who was the first woman on earth?', 'pandora'],
        'key' :        ['Which African country was formely known as Abyssinia', 'ethiopia'],
        'cookie' :     ['What was the first toy to be advertised on television', 'mr. potato head'],
        'potion' :     ['Which Shakespeare play is the longest', 'hamlet']}

         

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
    move = input('> ')

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
      triviaFunction(move[1])
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
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'flashlight' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
