class Item(object):
    """Base Item class

    Usage:
    >>> item01 = Item("sword", 150)
    >>> print item01
    <Item sword(150)>
    """

    def __init__(self, name=None, value=None):
        numeric = (int, float, long)
        self.name = "item" if not isinstance(name, basestring) else name
        self.value = 0 if not isinstance(value, numeric) else value

    def __repr__(self):
        class_name = self.__class__.__name__
        name = self.name
        value = self.value
        return "<{} {}({})>".format(class_name, name, value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()