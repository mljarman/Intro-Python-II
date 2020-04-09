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

instructions = """
                In this game, navigate to different rooms using [n], [s], [e], [w].
                Press [q] to quit. Let's go!"""

# Make a new player object that is currently in the 'outside' room.
name = input("Enter player name: ")
if name == '':
    name = 'Guest'
print('-'*80)
print(f'Welcome, {name}!')
print('-'*80)
print(textwrap.dedent(instructions)[1:-1])
print('-'*80)
print('')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
player = Player(name, room['outside'])
curr_room = player.current_room
print(f'You are currently: {curr_room.name}')
# print room description
[print(line) for line in wrapper.wrap(text=curr_room.description)]
print('-'*80)


# * Waits for user input and decides what to do.
inp = None
directions = ['n', 's', 'e', 'w']
while inp != 'q':
    print('')
    print('-'*80)
    inp = str(input("Where to? Enter direction to go: "))

    # if player ends game:
    if inp == 'q':
        print('Thanks for playing!')
        exit(0)
    if inp not in directions:
        print('WHOOPS! Invalid direction.')
    else:
        player.move_rooms(inp)
        curr_room = player.current_room
        print(f'Now you are in the: {curr_room.name}')
        [print(line) for line in wrapper.wrap(text=curr_room.description)]
