# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """
    Contains information of different rooms in game: name, description,
    items (if any) and directions.
    """
    def __init__(self, room_name, description, items=None):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [] if items is None else items

    def __str__(self):
        return f'{self.room_name}, {self.description}, {self.items}'

    def add_item_room(self, item_name):
        """
        Adds item into room for player to pick up.
        """
        self.items.append(item_name)

    def remove_item_room(self, item_name):
        """
        If player adds item to their inventory, removes item from room.
        """
        self.items.remove(item_name)

    def check_for_items(self):
        """
        Upon entering room, checks to see if there are items and prints item
        and its description or message saying no items.
        """
        if len(self.items) == 0:
            print('No items in this room, keep looking!')
        else:
            print('Items available:')
            for item in self.items:
                print(item.item_name)
