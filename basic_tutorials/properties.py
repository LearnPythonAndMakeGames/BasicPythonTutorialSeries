class Item(object):
    """Base Item Class"""

    @property
    def name(self):
        if not hasattr(self, '_name'):
            self._name = ''
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __init__(self, name='', value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.name, self.value)


item_01 = Item(name="sword", value=150)
item_02 = Item(name="axe", value=100)

print item_01
print item_02
