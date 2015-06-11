from file_manipulation import yaml_load


class Recipe(object):

    """Base recipe object"""

    actions = dict((name, value)
                   for name, value
                   in yaml_load('action_data.yaml').iteritems())

    def __init__(self, name, steps=[], ingredients={}, item_name=None):
        # Stores name, item name, ingredients and steps for a recipe
        self.name = name
        self.item_name = item_name or name
        self.ingredients = ingredients
        self.steps = steps

    def add_step(self, action, items=[], duration=None):
        """Adds a step to the recipe"""
        # set default duration
        if duration is None:
            duration = self.actions.get(action, 0)
        # create equivalent item from this step
        new_item = None
        for item in items:
            if new_item is None:
                new_item = item
            else:
                new_item += item
        # update duration with item information
        if new_item is not None:
            duration = duration * new_item.quantity
        duration = duration
        # add to steps property
        self.steps.append((action, items, duration))

    def follow(self):
        """Creates a item from the recipe"""
        items = []
        duration = 0
        # Capture all items and duration information from steps
        for action, action_items, action_duration in self.steps:
            items.extend(action_items)
            duration += action_duration
        # Iterate over steps to create finalized item
        new_item = None
        for item in items:
            if new_item is None:
                new_item = item
            else:
                new_item += item
        if new_item is not None:
            new_item.name = self.item_name
        # Return finalized item
        return new_item, duration

    def __repr__(self):
        cname = self.__class__.__name__
        name = self.name
        item, duration = self.follow()
        health = item.health
        if abs(health) > 1:
            health = int(health)
        time_data = [(60, "sec"), (60, "min"),  (24, "hour"),
                     (30, "day"), (12, "month"), (100, "year"),
                     (10, "century"), (1000, "millenia"), (10, "age"),
                     (10, "epoch"), (10, "period"), (10, "era"), (1, "eon")]
        time_string = ""
        identifier = "{}:{}".format(name, health)
        for val, name in time_data:
            if duration >= val:
                duration = duration / float(val)
            else:
                if duration > 1:
                    duration = int(duration)
                time_string = "[{} {}]".format(duration, name)
                break
        time_string = " {}".format(time_string) if time_string else ""
        string = "<{} {}{}>".format(cname, identifier, time_string)
        return string


if __name__ == "__main__":
    from Item import Item
    import yaml

    filepath = "recipe_data.yaml"
    recipe_data = yaml_load(filepath)

    filepath = "item_data.yaml"
    items = dict((name, Item(name=name, properties=prop))
                 for name, prop in yaml_load(filepath).iteritems())

    recipes = {}
    for recipe_name in recipe_data:
        recipe = recipe_data[recipe_name]
        ingredients = recipe.get("ingredients", {})
        steps = recipe.get("steps", [])
        recipe = Recipe(recipe_name)
        for step in steps:
            for action, data in step.items():
                step_items = []
                step_duration = None
                if isinstance(data, (tuple, list)):
                    step_items = [items.get(item)
                                  for item in data
                                  if item in items]
                elif isinstance(data, (int, float)):
                    step_duration = data
                recipe.add_step(action, step_items, step_duration)
        item, duration = recipe.follow()
        print recipe
        if item:
            items[item.name] = item
            recipes[recipe.name] = recipe
