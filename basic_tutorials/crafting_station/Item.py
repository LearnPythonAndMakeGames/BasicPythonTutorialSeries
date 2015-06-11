from file_manipulation import yaml_load


class Item(object):

    """Basic item"""

    property_fields = dict((name, value)
                           for name, value
                           in yaml_load('property_data.yaml').iteritems())

    @property
    def health(self):
        quantity = 0
        health_value = 0.0
        count = len(self)
        for prop_name, prop_value in self.iteritems():
            start, end = self.property_fields.get(prop_name, (0, 0))
            prop_value = prop_value / count
            if start <= prop_value <= end:
                health_value += abs(prop_value)
            else:
                prop_delta = end - start
                if start < 0:
                    prop_delta = prop_delta / 2.0
                shifted_value = float(prop_value) + start
                multiplier = shifted_value / prop_delta
                multiplied_value = float(prop_value) * multiplier
                health_value -= abs(multiplied_value)
        if quantity > 1:
            health_value = health_value / self.quantity
        return health_value

    def __init__(self, name, quantity=1, properties=None):
        self.name = name
        self.quantity = quantity
        self.properties = properties if properties is not None else {}

    def __getitem__(self, name):
        """"""
        return self.get(name)

    def __setitem__(self, name, value):
        """"""
        if name in self.property_fields:
            self.properties[name] = value

    def __iter__(self):
        for key in self.properties:
            yield key

    def iteritems(self):
        for key, value in self.properties.iteritems():
            yield key, value

    def __len__(self):
        return len(self.properties)

    def get(self, name, default=None):
        value = self.properties.get(name, default)
        return value

    def __repr__(self):
        """Representation of item"""
        string = "<{} {}:{} [{} {}]>"
        cname = self.__class__.__name__
        qty = self.quantity
        if abs(qty) > 1:
            qty = int(qty)
        grams = "grams" if self.quantity > 1 else "gram"
        health = self.health
        if abs(health) > 1:
            health = int(health)
        return string.format(cname, self.name, health, qty, grams)

    def __add__(self, other):
        item = self
        if isinstance(other, Item):
            properties = set(p for p in self)
            properties.update(set(p for p in other))
            new_props = {}
            for prop_name in properties:
                count = 0
                if prop_name in self:
                    count += 1
                if prop_name in other:
                    count += 1
                val = self.get(prop_name, 0) + other.get(prop_name, 0)
                val = val / 2.0
                new_props[prop_name] = val
            if new_props:
                new_name = "_".join((self.name, other.name))
                new_qty = sum([self.quantity, other.quantity])
                item = Item(new_name, new_qty, new_props)
        return item

if __name__ == "__main__":
    filepath = "item_data.yaml"
    with open(filepath, 'r') as fd:
        items = dict((name, Item(name=name, properties=prop))
                     for name, prop in yaml_load(fd).iteritems())

    new_item = items['coffee'] + items['vinegar']
    print new_item
