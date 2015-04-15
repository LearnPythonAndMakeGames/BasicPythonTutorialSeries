import logging

logger = logging.getLogger('example')

# CRITICAL - 50
# ERROR - 40
# WARNING - 30
# INFO - 20
# DEBUG - 10
format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format=format, level=logging.WARNING)


class Item(object):
    """Base Item class"""

    def __init__(self, name, value):
        self.name = name
        self.value = value
        logger.debug("Item created: '{}({})'".format(self.name, self.value))

    def buy(self, quantity=1):
        """Buys item"""
        logger.debug("Bought item: '{}'".format(self.name))

    def sell(self, quantity=1):
        """Sells item"""
        logger.warn("Sold item: '{}'".format(self.name))

items = []
for index in xrange(100):
    items.append(Item('sword_'+str(index), 100))

for item in items:
    item.buy()

for item in items:
    item.sell()