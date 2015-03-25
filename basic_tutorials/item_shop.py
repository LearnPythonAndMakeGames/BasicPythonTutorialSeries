"""
Item Shop
---------
This is an item shop that allows a player to purchase and sell to a
shop owner.

Requirements:
   * Inventory shall be available for both the shop and player
   * Random values shall be used for shop and player currency, items, item quantities, etc.
   * There shall be a fixed set of items that can be purchased and sold
   * Player shall be able to purchase items if they have the funds.
   * Player shall be able to sell items if they have an item and the shop has funds.

Design:
    Data:
        Items:
            Name
            Value (currency: random number -- between 10 and 100)
        Shop:
            Inventory of items (random number -- between 1 and 4)
            Starting currency (random number -- between 150 and 600)
        Player:
            Inventory of items (random number -- between 0 and 1)
            Starting currency (random number -- between 100 and 350)

    Functions:
        Main shopping:
            continue shopping question / loop
            purchase or sell control flow
            update on currencies and inventories

        Display:
            display inventories (for both player and shop)


Implementation:
    Hint #1 - a single while loop and complex if statement
    Hint #2 - a couple of dictionaries:  inventory, value...  pre-sorting
              when you index
    Hint #3 - only need to ask a single question and then interpret the
              player response as integer or string
    Hint #4 - Function definitions

    def display_inventory(message, inventory, values, count=0):
        '''Displays inventory

        Parameters:
            message - displays at the top of the inventory
            inventory - dictionary mapping item name to quantity
            values - dictionary mapping item name to item value
            count - where to start counting when enumerating
        '''

    def run_shop():
    '''Infinite shop loop or until player decides to quit'''

Test:
   * Inventory shall be available for both the shop and player
   * Random values shall be used for shop and player currency, items, item quantities, etc.
   * There shall be a fixed set of items that can be purchased and sold
   * Player shall be able to purchase items if they have the funds.
   * Player shall be able to sell items if they have an item and the shop has funds.

"""
import random


def display_inventory(message, inventory, values, count=0):
    '''Displays inventory

    Parameters:
        message - displays at the top of the inventory
        inventory - dictionary mapping item name to quantity
        values - dictionary mapping item name to item value
        count - where to start counting when enumerating
    '''
    print("-" * 40)
    print(message)
    print("-" * 40)
    for item_index, item_data in enumerate(sorted(inventory.items())):
        item_index = item_index + count
        item_name, item_quantity = item_data
        item_value = values.get(item_name, "SOLD OUT")
        if item_value == "SOLD OUT":
            print("{}: {} is {} and unavailable.".format(item_index, item_name, item_value))
        else:
            print("{}: {} costs {} gold and there are {} left.".format(item_index, item_name, item_value, item_quantity))
    print("-" * 40)


def run_shop():
    '''Infinite shop loop or until player decides to quit'''
    # Initializations
    # random.seed(0)

    item_names = ['sword', 'axe', 'dagger', 'shield',
                  'armor', 'tunic', 'boots']
    item_count = len(item_names)

    # Initialize the dictionaries
    item_values = {}  # associates item name to currency value
    shop_inventory = {}  # associates the item names to shop quantity
    player_inventory = {}  # associates the item names to player quantity
    for item_name in item_names:
        # setting the random data
        item_value = random.randint(10, 100)
        shop_quantity = random.randint(1, 4)
        player_quantity = random.randint(0, 1)
        # assigning keys to the random data
        item_values[item_name] = item_value
        shop_inventory[item_name] = shop_quantity
        player_inventory[item_name] = player_quantity

    # Set starting currency
    shop_currency = random.randint(150, 600)
    player_currency = random.randint(100, 350)

    # main
    continue_shopping = True
    print("Welcome to the Item Shop!")
    while continue_shopping is True:
        display_inventory(message="Shop Inventory",
                          inventory=shop_inventory,
                          values=item_values)
        display_inventory(message="Player Inventory",
                          inventory=player_inventory,
                          values=item_values,
                          count=item_count)
        print("The shop has {} gold left.".format(shop_currency))
        print("You have {} gold left.".format(player_currency))
        print("-"*40)

        item_value_keys = sorted(item_values.keys())
        answer = raw_input("What item would you like to sell/purchase? ")
        # handle the purchase of an item
        if answer.isdigit() and int(answer) < item_count:
            answer = int(answer)
            item_name = item_value_keys[answer]
            item_value = item_values[item_name]
            # Check to see if the purchase is possible
            if shop_inventory[item_name] <= 0:
                print("{} is unavailable.".format(item_name))
            elif item_value > player_currency:
                print("You do not have the funds to purchase {}.".format(item_name))
            else:
                # go ahead and purchase
                shop_currency = shop_currency + item_value
                player_currency = player_currency - item_value
                shop_inventory[item_name] = shop_inventory[item_name] - 1
                player_inventory[item_name] = player_inventory[item_name] + 1
                print("{} purchased for {} gold".format(item_name, item_value))

        # handle the sale of an item
        elif answer.isdigit() and int(answer) >= item_count:
            answer = int(answer)
            item_name = item_value_keys[answer - item_count]
            item_value = item_values[item_name]
            # Check to see if the sale is possible
            if player_inventory[item_name] <= 0:
                print("{} is unavailable.".format(item_name))
            elif item_value > shop_currency:
                print("Shop does not have the funds to purchase {}.".format(item_name))
            else:
                # go ahead and purchase
                player_currency = player_currency + item_value
                shop_currency = shop_currency - item_value
                player_inventory[item_name] = player_inventory[item_name] - 1
                shop_inventory[item_name] = shop_inventory[item_name] + 1
                print("{} sold for {} gold".format(item_name, item_value))

        # handle the 'q' to quit or anything not already handled
        else:
            if answer.lower().startswith(("n", "q")):
                continue_shopping = False
            elif answer.lower():  # is answer == '' or ""
                continue
            else:
                # couldn't find the item
                print("Could not find {}".format(answer))
                continue

run_shop()