import textwrap
wrapper = textwrap.TextWrapper(width=70)
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """
    Contains information on player in game: name, the current room
    they're in, and items in their inventory.
    """
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = [] if items is None else items

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def move_rooms(self, inp_dir):
        """
        Attempt to move into next room. If no room in that direction, will
        return error and prompt player to try another direction.
        """
        target_room = getattr(self.current_room, f'{inp_dir}_to')
        if target_room is None:
            print('WHOOPS! No room here, try another direction.')
            print('-'*80)
        else:
            self.current_room = target_room
            print(f'Now you are in the: {self.current_room.room_name}')
            [print(line) for line in wrapper.wrap(text=self.current_room.description)]
            print('\n')

    def add_item_inv(self, item_name):
        """
        Adds item from room into player's inventory.
        """
        self.items.append(item_name)

    def remove_item_inv(self, item_name):
        """
        Removes item from player's inventory if dropped.
        """
        self.items.remove(item_name)

    def print_inventory(self):
        """
        Prints items in player's inventory.
        """
        if len(self.items) == 0:
                print('You currently have no items.')
        else:
            for item in self.items:
                print(item)
