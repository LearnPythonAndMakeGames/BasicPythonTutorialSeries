items = [
    ('sword', 100),
    ('boots', 30),
    ('armor', 50),
    ('gloves', 20),
    ('shield', 45),
]

sword = items[0]  # grabs first element
sword = items[-5]  # grabs fifth element from the end
sword_value = sword[-1]  # grabs last element

defensive_items = items[1:]  # grabs all elements after the first one
body_items = items[1:-1]  # excludes the first and last element

# items.append(('axe', 110))  # adds a new element to the list
items.insert(1, ('axe', 110))

# find the sword in the list
sword_index = items.index(('sword', 100))
sword = items[sword_index]  # assigns sword to sword in items


axe_index = items.index(('axe', 110))  # finds axe in the list
axe = items.pop(axe_index)  # removes axe from the list

boots_index = items.index(('boots', 30))
del items[boots_index]

for item_index, each_item in enumerate(sorted(items)):
    item_name, item_value = each_item
    # print "{0}: {1} --> {2} gold".format(item_index, item_name, item_value)

# sort based on cost
sorted_by_value = []
for each_item in items:
    item_name, item_value = each_item
    sorted_by_value.append((item_value, item_name))

for item_index, each_item in enumerate(reversed(sorted(sorted_by_value))):
    item_value, item_name = each_item
    print "{0}: {1} --> {2} gold".format(item_index, item_name, item_value)


