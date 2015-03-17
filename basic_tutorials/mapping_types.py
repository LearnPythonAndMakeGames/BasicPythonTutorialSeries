#!/usr/bin/env python

x = dict(apple="fruit", banana="fruit", carrot="vegetable", donut="junk food")

y = {'donut': 'junk food',
     'carrot': 'vegetable',
     'banana': 'fruit',
     'apple': 'fruit'}

array = ["apple", "banana", "carrot", "donut"]
array[0]

keys = x.keys()
for key in sorted(keys):
    """print key, x[key]"""

for item in sorted(x.items()):
    (key, value) = item
    key, value = item

for key, value in sorted(x.items()):
    """print key, value"""

for key, value in x.iteritems():
    """print key, value"""

healthy_food = x
del healthy_food["donut"]
healthy_food["fig"] = "fruit"
"""print healthy_food"""

# remove the fruits from the list
for key, value in x.items():
    if value == "fruit":
        del x[key]
print x


