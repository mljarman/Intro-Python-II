from room import Room
from player import Player
from item import Item
import textwrap


wrapper = textwrap.TextWrapper(width=70)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

instructions = """In this game, navigate to different rooms using 'n', 's', 'e',
               or 'w', picking up items along the way. Press 'q' to quit.
               Let's go!"""

def navigate(current_room, direction):
    pass
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Enter player name: ")
if name == '':
    name = 'Guest'
print(f'Welcome, {name}!\n')
[print(line) for line in wrapper.wrap(text=instructions)]
print('\n')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
player = Player(name, room['outside'])
print(f'You are currently: {player.current_room}')
curr_room = player.current_room
# will always be outside initially so print that description:
[print(line) for line in wrapper.wrap(text=player.current_room.description)]
print('\n')

# If the user enters a cardinal direction, attempt to move to the room there.
""" NEED TO CONDENSE THIS"""
# * Waits for user input and decides what to do.
inp = None
while inp != 'q':
    inp = str(input("Where to? Enter direction to go: "))
    # if player ends game:
    if inp == 'q':
        print('Thanks for playing!')
        exit(0)
    if inp == 'n':
        if player.current_room.n_to == None:
            print('\n Whoops! Try again.\n')
        else:
            player.current_room = player.current_room.n_to
            print(player.current_room, '\n')
    elif inp == 's':
        if player.current_room.s_to == None:
            print('\n Whoops! Try again.\n')
        else:
            player.current_room = player.current_room.s_to
            print(player.current_room, '\n')
    elif inp == 'e':
        if player.current_room.e_to == None:
            print('\n Whoops! Try again.\n')
        else:
            player.current_room = player.current_room.e_to
            print(player.current_room, '\n')
    elif inp == 'w':
        if player.current_room.w_to == None:
            print('\n Whoops! Try again.\n')
        else:
            player.current_room = player.current_room.w_to
            print(player.current_room, '\n')
