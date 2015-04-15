class Item(object):

    def __init__(self, name=None, value=None):
        self.name = 'item' if name is None else name
        numeric = (int, float, long)
        self.value = 0 if not isinstance(value, numeric) else value

    def __str__(self):
        return "{}({})".format(self.name, self.value)


item01 = Item('sword', 150)
print item01