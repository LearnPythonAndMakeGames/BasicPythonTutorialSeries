"""
Challenge 03: Rat's Nose
------------------------

Requirements:
    Food:
       - types of food
       - vary in quality
       - vary in properties
       - quantity

    Recipe:
       - very specific combination of food
       - vary quality
       - vary in properties
       - quantity

    Rat Family:
       - health
       - eat food
       - each rat eats 50 grams of food a day
       - if a rat doesn't eat, they lose health

    Food receptacle:
       - contain food
       - random for what's contained

Implementation:

    * 100 Family Rats (100% health)
    * 10 Trash bins (random food distribution)
    * Food (5 - 20) in each bin

Testing:
"""
import sys
import random


def consume(food, current_health, max_health=100):
    """Consumes food and decrements health if food is unhealthy"""
    health_value = food.health
    current_health = current_health + health_value
    if current_health > max_health:
        current_health = max_health
    if current_health < 0:
        current_health = 0
    return current_health


def update_food_receptical(current_items={}, percent_remove=50):
    """Add or removes food to/from the food receptacle"""
    all_items = {}
    for name, value in yaml_load('item_data.yaml').iteritems():
        all_items[name] = Item(name, properties=value)
    percentage_of_items_touched = random.random() * 100
    percent_remove = percent_remove / 100.0
    number_of_items = len(all_items)
    num_items = int(float(number_of_items * percentage_of_items_touched) / 100)
    if num_items < 5:
        num_items = 5
    if num_items > 20:
        num_items = 20
    indices = set()
    while len(indices) < num_items:
        value = int(random.random() * number_of_items)
        indices.add(value)

    keys = sorted(all_items.keys())
    for idx, item_index in enumerate(indices):
        item_name = keys[item_index]
        item = current_items.get(item_name, all_items.get(item_name))
        removal = random.random() - percent_remove
        random_quantity = removal * (random.random() * 400)
        item.quantity = item.quantity + random_quantity
        qty = item.quantity
        rstring = "+" if removal > 0 else "-"
        if removal == 0:
            rstring = " "
        if item.quantity < 0:
            if item_name in current_items:
                current_items.pop(item_name)
        else:
            current_items[item_name] = item
    return current_items


def feed_rats(rats=[], food=None, food_needed=50, starvation=30):
    """Feeds the rats the food"""
    died = 0
    lived = 0
    for idx, rat in enumerate(rats):
        if food:
            qty = food.quantity
            health = food.health
            if qty >= food_needed:
                rat = rat + health
            else:
                ratio = (food_needed - qty) / float(food_needed)
                rat = rat + health * ratio - starvation * (1 - ratio)
        else:
            rat = rat - starvation
        if rat <= 0:
            rat = 0
            died += 1
        elif rat >= 100:
            lived += 1
            rat = 100
        else:
            lived += 1
        rats[idx] = rat
    print "{} rats lived.  {} rats died.".format(lived, died)


def display_menu():
    """Displays the menu"""
    print "'h' or '?' for this message"
    # create new recipe
    print "'c' to create a new recipe"
    # feed rats from food store
    print "'f' to feed rats"
    # list foods
    print "'l' to list foods available"
    # follow existing recipe
    print "'r' for recipes"
    # quit
    print "'q' to quit."
    # continue
    print "any other key to continue"


def display_recipes(recipes=[]):
    if not recipes:
        print "No recipes found."
        return
    for idx, recipe in enumerate(recipes):
        print "{:>4}: {}"


def display_foods(foods={}):
    for idx, food_name in enumerate(foods):
        food_value = foods[food_name]
        print "{:>4}: {} {}".format(idx, food_name, food_value)


def handle_input(game_round=0, rats=[], foods={}):
    """Handles player input"""
    player_input = raw_input("Round: {}> ".format(game_round))
    value = player_input.strip().lower()
    # Quit
    if value.startswith("q"):
        sys.exit()
    elif value.startswith(("h", "?")):
        display_menu()
    # Follow an existing recipe
    elif value.startswith("r"):
        game_round += handle_recipes(rats, foods)
    # Create a new recipe
    elif value.startswith("c"):
        game_round += handle_create_recipe(rats, foods)
    # List known recipes
    elif value.startswith("l"):
        display_foods(foods)
    # Feed rats with available foods
    elif value.startswith("f"):
        game_round += handle_feeding(rats, foods)
    # Next round
    elif value.startswith("n"):
        game_round += 1
    # Help
    else:
        pass
    return game_round


if __name__ == "__main__":
    from Item import Item
    from file_manipulation import yaml_load

    items = {}
    for name, value in yaml_load('item_data.yaml').iteritems():
        items[name] = Item(name, properties=value)

    current_items = {}
    rats = [100 for rat in xrange(100)]
    last_round = 0
    game_round = 1
    while game_round:
        living_rats = [r for r in rats if r > 0]
        num_living_rats = len(living_rats)
        rat_ave = int(float(sum(living_rats)) / num_living_rats)
        if rat_ave == 100:
            msg = "Round {}: {} rats and they're all hungry!"
            print msg.format(game_round, num_living_rats)
        else:
            msg = "Round {}: {} living rats with an average health of {}"
            print msg.format(game_round, num_living_rats, rat_ave)
        game_round = handle_input(game_round, rats, current_items)
        if game_round > last_round:
            update_food_receptical(current_items)
        last_round = game_round










