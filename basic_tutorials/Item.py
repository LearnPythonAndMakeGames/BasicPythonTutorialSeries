
class Item(object):
    """Base Item object"""

    def __init__(self, name='', value=0, quantity=1):
        """Initializes object"""
        self.name = name
        self.value = value
        self.quantity = quantity

    def __repr__(self):
        """Representation of the object"""
        name = self.name
        value = self.value
        qty = self.quantity
        representation = "<Item {}x '{}' @ {}>".format(qty, name, value)
        return representation

    def sell(self, quantity=1):
        """Reduces quantity by 1"""
        if self.quantity - quantity < 0:
            print "ERROR: Cannot reduce {} below zero.".format(self)
        else:
            self.quantity = self.quantity - quantity

    def buy(self, quantity=1):
        self.quantity = self.quantity + quantity


item = Item("sword", 100)
print item
item.sell(2)
print item
item.sell()
print item
item.buy()
print item
item.buy(4)
print item
