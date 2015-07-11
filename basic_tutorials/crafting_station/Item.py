#!/usr/bin/env python
import yaml


def yaml_load(filepath):
    """Loads yaml file and returns data"""
    with open(filepath, 'r') as fd:
        return yaml.load(fd)


class Item(object):
    """Item Class

    Doctest:
    >>> item_data = [
    ...    ('iron hilt', {'weight': 400, 'damage': 5}),
    ...    ('Valyrian steel', {'weight': 900, 'damage': 8}),
    ...    ('leather strips', {'weight': 150, 'damage': 1})
    ... ]
    >>> items = dict((item_name, Item(name=item_name, **item_values))
    ...               for item_name, item_values in item_data)
    >>> item = items['iron hilt'] + items['Valyrian steel'] + 5*items['leather strips']
    >>> item.name = "Longclaw"
    >>> print item
    <Item Longclaw [1450 grams]>
    >>> print item.value
    0.5
    >>> print items['iron hilt'].value
    0.497222222222
    >>> print items['Valyrian steel'].value
    0.504444444444
    >>> print items['leather strips'].value
    1.7
    """
    field_filepath = "item_property_data.yaml"
    fields = dict((name, value)
                  for name, value in yaml_load(field_filepath).iteritems())

    @property
    def value(self):
        """Intrinsic value of item"""
        value = 0.0
        prop_count = len(self)
        for prop_name, prop_value in self.iteritems():
            start, end = self.fields.get(prop_name, (0, 0))
            if isinstance(prop_value, (int, float)):
                prop_value = prop_value / prop_count
                if start <= prop_value <= end:
                    value += abs(prop_value)
                else:
                    delta = end - start
                    if start < 0:
                        delta = delta / 2.0
                    shift_value = float(prop_value) + start
                    multiplier = shift_value / delta
                    multiplied_value = float(prop_value) * multiplier
                    value += abs(multiplied_value)
        weight = self.get('weight', 1)
        qty = self.get('quantity', 1)
        weight = 1 if weight == 0 else weight
        value = (value / weight) * qty
        return value

    def __mul__(self, other):
        """Increases quantity

        >>> item = Item("mul test")
        >>> print item.quantity
        None
        >>> item * 5
        >>> print item.quantity
        5
        """
        if isinstance(other, int):
            self.quantity = other

    def __rmul__(self, other):
        """Increases quantity

        >>> item = Item("rmul test")
        >>> print item.quantity
        None
        >>> 5 * item
        >>> print item.quantity
        5
        """
        if isinstance(other, int):
            self.quantity = other

    def __getattr__(self, key):
        """Returns properties dictionary values as if they
        were properties on the class.

        >>> item = Item("getattr test", weight=10)
        >>> w1 = item['weight']
        >>> w2 = item.get('weight')
        >>> w3 = item.weight
        >>> assert(w1 == w2)
        >>> assert(w2 == w3)
        >>> assert(w1 == 10)
        """
        value = self.__dict__.get("properties", {}).get(key)
        return value

    def __setattr__(self, key, value):
        """Sets properties dictionary values as if they
        were properties on the class.

        >>> item = Item("getattr test", weight=10)
        >>> w1 = item['weight']
        >>> w2 = item.get('weight')
        >>> w3 = item.weight
        >>> assert(w1 == w2)
        >>> assert(w2 == w3)
        >>> assert(w1 == 10)
        >>> item.weight = 11
        >>> assert(item.weight == 11)
        """
        if key in self.fields:
            self.properties[key] = value
        else:
            super(Item, self).__setattr__(key, value)

    def __getitem__(self, prop_name):
        """Duplicates the getitem from a dictionary

        Doctest:
        >>> item = Item("setitem test", weight=10, materials=['leather', 'steel', 'iron'])
        >>> print item['weight']
        10
        >>> item['weight'] = 11
        >>> print item.weight
        11
        >>> item['materials'] = ['h20']
        >>> print item['materials']
        None
        """
        value = self.__dict__['properties'].get(prop_name)
        return value

    def __setitem__(self, prop_name, prop_value):
        """Duplicates the setitem from a dictionary

        Doctest:
        >>> item = Item("setitem test", weight=10, materials=['leather', 'steel', 'iron'])
        >>> print item.get('weight', 12)
        10
        >>> item['weight'] = 11
        >>> print item.get('weight', 12)
        11
        >>> item['materials'] = ['h20']
        >>> print item.get('materials', [])
        []
        """
        if prop_name in self.fields:
            self.properties[prop_name] = prop_value

    def __iter__(self):
        """Return in iterator which iterates through the properties

        Doctest:
        >>> item = Item("iter test", weight=10, materials=['leather', 'steel', 'iron'])
        >>> for prop_name in item:
        ...     print "{}".format(prop_name)
        weight
        """
        iterator = self.properties
        for key in iterator:
            yield key

    def iteritems(self):
        """Returns an iterator over the key, value of the properties

        Doctest:
        >>> item = Item("iteritem test", weight=10, materials=['leather', 'steel', 'iron'])
        >>> for prop_name, prop_value in item.iteritems():
        ...     print "{}: {}".format(prop_name, prop_value)
        weight: 10
        """
        iterator = self.properties.iteritems()
        for key, value in iterator:
            yield key, value

    def __len__(self):
        """Returns the number of properties in an item

        Doctest:
        >>> item = Item("len_test")
        >>> len(item)
        0
        >>> item.properties['weight'] = 0
        >>> len(item)
        1
        """
        return len(self.properties)

    def get(self, prop_name, default_value=None):
        """Returns property value if the prop_name is available or
        returns the default value.

        Doctest:
        >>> item = Item("get test", materials=['leather', 'iron', 'steel'], weight=10)
        >>> damage = item.get('damage')
        >>> print damage
        None
        >>> materials = item.get('materials')
        >>> print materials
        None
        >>> weight = item.get('weight')
        >>> print weight
        10
        """
        value = self.properties.get(prop_name, default_value)
        return value

    def __init__(self, name, **properties):
        """Initializes Item"""
        self.name = name
        self.properties = {}
        for prop_name, prop_value in properties.iteritems():
            if prop_name in self.fields:
                self.properties[prop_name] = prop_value

    def __add__(self, other):
        """Adds Item to other"""
        props = dict((k, v) for k, v in self.properties.iteritems())
        new_item = Item(self.name, **props)
        if isinstance(other, Item):
            other_props = other.properties
            properties = set(prop_name for prop_name in props)
            properties.update(set(prop_name for prop_name in other_props))
            for prop_name in properties:
                # TODO:  Update for more types
                prop_value = None
                self_value = props.get(prop_name, prop_value)
                other_value = other_props.get(prop_name, prop_value)
                if not isinstance(self_value, type(other_value)):
                    prop_value = self_value
                    if self_value is None:
                        prop_value = other_value
                else:
                    prop_value = self_value + other_value
                props[prop_name] = prop_value
            for prop_name in props:
                new_item.properties[prop_name] = props[prop_name]
        return new_item

    def __repr__(self):
        """Returns representation of the Item
        Example:  <Item Longclaw [1450 grams]>
        """
        weight = self.get("weight", 0)
        return "<Item {} [{} grams]>".format(self.name, weight)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # i = Item("test")
    # i.weight = 10
    # print i.weight
