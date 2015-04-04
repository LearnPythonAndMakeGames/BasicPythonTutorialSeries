items = [
    ('sword', 100),
    ('boots', 30),
    ('armor', 50),
    ('gloves', 20),
    ('shield', 45),
]
sword_value = items[0][1]

items = dict(items)

for item_name, item_value in items.items():
    print "{} --> {} gold".format(item_name, item_value)

sword_value = items['sword']
print sword_value

del items['sword']
for item_name, item_value in items.items():
    print "{} --> {} gold".format(item_name, item_value)

items_list = items.items()
for item_name, item_value in items_list:
    print "{} --> {} gold".format(item_name, item_value)

for item_name, item_value in items.iteritems():
    print "{} --> {} gold".format(item_name, item_value)

print '-' * 50
items['axe'] = 60
for item_name in sorted(items):
    item_value = items[item_name]
    print "{} --> {} gold".format(item_name, item_value)

print '-' * 50
keys = ['sword', 'axe']
for each_item in keys:
    item_value = items.get(each_item, "SOLD OUT")
    print "{} --> {}".format(each_item, item_value)
