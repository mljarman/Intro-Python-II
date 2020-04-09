# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """
    Contains information on player in game: name, the current room
    they're in, and items in their inventory.
    """
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def move_rooms(self, inp_dir):
        target_room = self.current_room.__dict__[f'{inp_dir}_to']
        if target_room is None:
            print('WHOOPS! No room here, try another direction.')
        else:
            self.current_room = target_room
