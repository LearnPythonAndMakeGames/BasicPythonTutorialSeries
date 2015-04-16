import uuid


class Item(object):
    """Base Item Class"""

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.uid = uuid.uuid4()

    def __eq__(self, other):
        attributes = ['uid']
        comparisons = []
        for attr in attributes:
            self_attr = getattr(self, attr)
            other_attr = getattr(other, attr, other)
            comparisons.append(self_attr == other_attr)
        comparison = all(comparisons)
        return comparison

    def __str__(self):
        return "{}: {}".format(self.name, self.value)


item01 = Item("sword", 150)
item02 = Item("sword", 150)

print "{} == {} | {}".format(item01, item02, item01 == item02)
