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

from Item import Item
from Rat import Rat
from Recipe import Recipe

from file_manipulation import yaml_load


def consume(food, current_health, max_health=100):
    """Consumes food and decrements health if food is unhealthy"""
    health_value = food.health
    current_health = current_health + health_value
    if current_health > max_health:
        current_health = max_health
    if current_health < 0:
        current_health = 0
    return current_health


def update_food_receptical(foods={}, percent_remove=50, number=4):
    """Add or removes food to/from the food receptacle"""
    all_items = {}
    for name, value in yaml_load('item_data.yaml').iteritems():
        all_items[name] = Item(name, properties=value)
    percentage_of_items_touched = random.random() * 100
    percent_remove = percent_remove / 100.0
    number_of_items = len(all_items)
    num_items = int(float(number_of_items * percentage_of_items_touched) / 100)
    if num_items < number:
        num_items = number
    if num_items > 20:
        num_items = 20
    indices = set()
    while len(indices) < num_items:
        value = int(random.random() * number_of_items)
        indices.add(value)

    keys = sorted(all_items.keys())
    for idx, item_index in enumerate(indices):
        item_name = keys[item_index]
        item = foods.get(item_name, all_items.get(item_name))
        removal = random.random() - percent_remove
        random_quantity = removal * (random.random() * 400)
        item.quantity = item.quantity + random_quantity
        qty = item.quantity
        rstring = "+" if removal > 0 else "-"
        if removal == 0:
            rstring = " "
        if item.quantity < 0:
            if item_name in foods:
                foods.pop(item_name)
        else:
            foods[item_name] = item
    return foods


def update_rat_health(rats=[]):
    for rat in rats:
        if not rat.was_fed():
            rat.starve()
        else:
            rat.reset_feed()


def feed_rats(rats=[], food=None, food_needed=50, starvation=30):
    """Feeds the rats the food"""
    died = 0
    lived = 0
    for idx, rat in enumerate(rats):
        if food:
            qty = food.quantity
            health = food.health
            if qty >= food_needed:
                rat.health = rat.health + health
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


def display_recipes(recipes=[]):
    if not recipes:
        print "No recipes found."
        return
    for idx, recipe in enumerate(recipes):
        print "{:>4}: {}".format(idx, recipe)


def display_foods(round=0, foods={}):
    for idx, food_name in enumerate(foods):
        food = foods[food_name]
        food_value = int(food.quantity)
        print "{:>4}: {} {} grams".format(idx, food_name, food_value)


def handle_input(game_round=0, rats=[], foods={}, recipes={}):
    """Handles player input"""
    print "'?' for help"
    player_input = raw_input("Round {}> ".format(game_round))
    value = player_input.strip().lower()
    # Quit
    if value.startswith("q"):
        sys.exit()
    elif value.startswith(("h", "?")):
        display_menu()
    # Follow an existing recipe
    elif value.startswith("r"):
        game_round += handle_recipes(game_round, rats, foods, recipes)
    # Create a new recipe
    elif value.startswith("c"):
        game_round += handle_create_recipe(game_round, rats, foods, recipes)
    # List known recipes
    elif value.startswith("l"):
        display_foods(foods)
    # Feed rats with available foods
    elif value.startswith("f"):
        game_round += handle_feeding(game_round, rats, foods, recipes)
    # Next round
    elif value.startswith("n"):
        game_round += 1
    # Help
    else:
        pass
    return game_round


def handle_create_recipe(game_round, rats, foods, recipes):
    """Creates a recipe"""
    display_foods(foods)
    idx = len(foods)
    print "{:>4}: {}".format(idx, "Back")
    player_input = raw_input("Round {}> ".format(game_round))
    value = player_input.strip().lower()
    return game_round


def handle_feeding(game_round, rats, foods, recipes):
    """Handles feeding of rats"""
    return game_round


def handle_recipes(game_round, rats, foods, recipes):
    """Handles creating a food"""
    display_recipes(recipes)
    idx = len(recipes)
    print "{:>4}: {}".format(idx, "Back")
    player_input = raw_input("Round {}: Use which recipe? ".format(game_round))
    value = player_input.strip().lower()
    if value != idx:
        pass
    return game_round


if __name__ == "__main__":

    items = {}
    for name, value in yaml_load('item_data.yaml').iteritems():
        items[name] = Item(name, properties=value)

    recipes = {}
    for name, value in yaml_load('recipe_Data.yaml').iteritems():
        ingredients = value.get('ingredients', {})
        steps = value.get('steps', [])
        recipes[name] = Recipe(name, ingredients=ingredients, steps=steps)

    foods = {}
    rats = [Rat() for rat in xrange(100)]
    last_round = 1
    game_round = 1
    # Set the initial conditions for the food receptical
    #  Guarantee at least 8 items at the start.
    update_food_receptical(foods, percent_remove=0, number=8)
    while game_round:
        living_rats = [r.health for r in rats if r.health > 0]
        num_living_rats = len(living_rats)
        if num_living_rats > 0:
            rat_ave = int(float(sum(living_rats)) / num_living_rats)
        else:
            rat_ave = 0
        if rat_ave == 100:
            msg = "Round {}: {} rats and they're all hungry!"
            print msg.format(game_round, num_living_rats)
        elif num_living_rats > 0:
            msg = "Round {}: {} living rats with an average health of {}"
            print msg.format(game_round, num_living_rats, rat_ave)
        else:
            msg = "Round {}: All the rats are dead.  Game over."
            print msg.format(game_round)
            sys.exit()
        game_round = handle_input(game_round, rats, foods, recipes)
        while last_round < game_round:
            update_rat_health(rats)
            last_round += 1
