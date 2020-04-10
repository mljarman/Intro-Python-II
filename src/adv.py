from room import Room
from player import Player
from item import Item
import textwrap

# for reading long lines of text:
wrapper = textwrap.TextWrapper(width=70)

# declare all the rooms

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

items = {
    'Gnome': Item("Gnome", "Jasper comes to life and lights the path with his lantern."),
    'Beans': Item("Beans", "Professor Copperfield's Miracle Legumes."),
}


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
                You can pick items with [take] [item name] or leave it behind with
                [drop] [item name]. To see what you've got in your collection, [i]
                or [inventory]. To quit, [q]. Let's go!"""

# add items to rooms:
room['foyer'].add_item_room(items['Gnome'])
room['narrow'].add_item_room(items['Beans'])
room['overlook'].add_item_room(items['Gnome'])


# make a new player object that is currently in the 'outside' room:
name = input("Enter player name: ")
# if no name given, use Guest:
if name == '':
    name = 'Guest'
print(f'Welcome, {name}!')
print('-'*80)
# print instructions on how to play:
print(textwrap.dedent(instructions)[1:-1])
print('-'*80)
print('')


# prints the current room name
player = Player(name, room['outside'])
curr_room = player.current_room
print(f'You are currently: {curr_room.room_name}')
# * Prints the current description (the textwrap module might be useful here).
[print(line) for line in wrapper.wrap(text=curr_room.description)]
print('-'*80)


# loop: waits for user input and decides what to do.
inp = ""
while inp!= 'q':
    directions = ['n', 's', 'e', 'w']
    accepted_commands = ['n', 's', 'e', 'w', 'i', 'inventory', 'q']
    print('')
    print('-'*80)
    inp = input("What would you like to do? ").split()
    print('-'*80)
    # if player ends game:
    if len(inp) == 1:
        inp = inp[0]
        if inp == 'q':
            print('Thanks for playing!')
            exit(0)
        if inp in directions:
            # move to new room or say no room exists:
            player.move_rooms(inp)
            # print items in room or say no items in room:
            player.current_room.check_for_items()
        if inp == 'i' or inp == 'inventory':
            # print player's inventory:
            player.print_inventory()
        else:
            if inp not in accepted_commands:
                print('WHOOPS! Invalid entry')

    elif len(inp) == 2:
        verb, item_inp = inp[0], inp[1]
        if verb == 'take':
            # player to pick up items:
            if items[item_inp] in player.current_room.items:
                # add to player's inventory:
                player.add_item_inv(item_inp)
                # prompt pick up message:
                items[item_inp].on_take()
                # remove item from the room's inventory:
                player.current_room.remove_item_room(items[item_inp])
            else:
                print('WHOOPS! That item is not here')
        if verb == 'drop':
            # player to drop items:
            if item_inp in player.items:
                # remove item from player's inventory:
                player.remove_item_inv(item_inp)
                # prompt dropped message:
                items[item_inp].on_drop()
                # add item to current room's inventory:
                player.current_room.add_item_room(items[item_inp])
            else:
                print("WHOOPS! You don't have that item")
        else:
            if verb not in ['take', 'get']:
                print('WHOOPS! Try again.')
