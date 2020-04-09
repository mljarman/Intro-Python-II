class Item:
    """
    Contains information about items that are found in rooms and can
    be taken or dropped by players: name, description
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_to_room(self, name):
        """
        Add item to room.
        """
        self.items.append(add_to_room)

    def add_to_inventory(self, name):
        """
        Add item to player's inventory.
        """
        self.inventory.append(add_to_inventory)
