class Item:
    """
    Contains information about items that are found in rooms and can
    be taken or dropped by players: name, description
    """
    def __init__(self, item_name, description):
        self.item_name = item_name
        self.description = description

    def __str__(self):
        return f'{self.item_name}, {self.description}'

    def on_take(self):
        print(f'You picked up the {self.item_name}')
        print(self.description)

    def on_drop(self):
        print(f'You dropped the {self.item_name}')
