class Shop(object):
    """Base Shop object"""

    def __init__(self, name='', inventory={}, currency=450):
        """Initializes object"""
        self.name = name
        self.inventory = inventory
        self.currency = currency

    def __repr__(self):
        """Representation of the object"""
        representation = "<Shop>"
        return representation

    def sell(self, quantity=1):
        """Reduces quantity by 1"""

    def buy(self, quantity=1):
        """Buys item"""

