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
