class Item(object):

    def __init__(self, name=None, value=None):
        self.name = 'item' if name is None else name
        self.value = 0 if value is None else value

    def __repr__(self):
        class_name = self.__class__.__name__
        return "<{} {}({})>".format(class_name, self.name, self.value)

    def __str__(self):
        return "{}({})".format(self.name, self.value)

items = []
for idx in xrange(100):
    items.append(Item("sword_"+str(idx), 150 + idx))

item_string = [
    "{}: {}".format(item.name, item.value)
    for item in items
    if item.value > 200
    if item.value <= 210
    ]

print item_string