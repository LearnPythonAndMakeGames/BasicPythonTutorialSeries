class Item(object):
    """Base Item Class"""

    # Commonly used dunders
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        """Representation of the class"""
        class_name = self.__class__.__name__
        return "<{}({}) '{}'>".format(class_name, self.value, self.name)

    def __str__(self):
        """String representation"""
        return "{}: {}".format(self.name, self.value)

    def __call__(self):
        """Displays all of the dictionary information"""
        for d in sorted(dir(item01)):
            print "{}: {}".format(d, str(getattr(item01, d)))

    # Comparison dunders
    def __eq__(self, other):
        """compares self to other for equivalence

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 == item02
        False
        >>> item01 == 150
        True
        """
        equal = None
        accepted_types = (int, float)
        if hasattr(other, 'value'):
            equal = self.value == other.value
        elif isinstance(other, accepted_types):
            equal = self.value == other
        return equal

    def __ne__(self, other):
        """Compares self to other for non-equivalence

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 != item02
        True
        >>> item01 != 150
        False
        """
        return not self.__eq__(self, other)

    def __lt__(self, other):
        """Compares self to other:  self less than other

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 < item02
        False
        >>> item01 < 150
        False
        """
    def __gt__(self, other):
        """Compares self to other:  self greater than other

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 > item02
        True
        >>> item01 > 150
        False
        """
    def __le__(self, other):
        """Compares self to other:  self less than or equal to other

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 <= item02
        False
        >>> item01 <= 150
        True
        """
    def __ge__(self, other):
        """Compares self to other:  self greater than or equal to other

        >>> item01 = Item("sword", 150)
        >>> item02 = Item("axe", 100)
        >>> item01 >= item02
        True
        >>> item01 >= 150
        True
        """

    # Attribute access dunders
    def __getattribute__(self, name):
        """Retrieves an attribute called 'name' from the dictionary"""

    def __getattr__(self, name):
        """Only called if name does not exist on self"""

    def __setattr__(self, name, value):
        """Allows you to set the attribute named 'name' with 'value'"""

    def __delattr__(self, name):
        """This allows you to remove objects within the self instance"""

    def __getitem__(self, key):
        """grabs the attribute by key

        print item01['name']
        """
        return self.__dict__.get(key, None)

    def __setitem__(self, key, value):
        """sets the attribute key by value

        print item01['name'] = 'Long Sword'
        """
        if key in self.__dict__:
            self.__dict__[key] = value

    def __delitem__(self, key):
        """delete the attribute by key"""
        if key in self.__dict__:
            del self.__dict__[key]

    # Iterable dunders
    def __iter__(self):
        """Iterates over data within the Item

        Usage:
        for item_key, item_value in item01:
            print item_key, item_value
        """
        for key, value in self.__dict__.iteritem():
            yield key, value

    def __contains__(self, key):
        """Checks self for key

        Usage:
        print "name" in item01
        """
        return key in self.__dict__


if __name__ == "__main__":
    item01 = Item("sword", 150)
    # item01()
    item02 = Item("axe", 100)
    print item01 != 150
    item01["name"] == item01.name

    for key, value in item01:
        print key, value

    if "name" in item01:
        print item01['name']
