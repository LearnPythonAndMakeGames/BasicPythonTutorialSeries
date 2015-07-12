#!/usr/bin/env python
from Item import Item


class Food(Item):
    """Food Class

    >>> from Item import yaml_load
    >>> filepath = "food_item_data.yaml"
    >>> foods = {}
    >>> for food_name, food_data in yaml_load(filepath).iteritems():
    ...    food = Food(food_name, weight=1, quantity=1, **food_data)
    ...    foods[food_name] = food
    >>> print foods.get('baking soda')
    <Food baking soda [1 gram]>
    """

    field_filepath = "food_property_data.yaml"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # i = Item("test")
    # i.weight = 10
    # print i.weight
