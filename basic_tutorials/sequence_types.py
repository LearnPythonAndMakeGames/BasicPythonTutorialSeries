#!/usr/bin/env python

# What is a sequence
# list
x = [0, 1, 2, 3]
# tuple
x = (0, 1, 2, 3)
# string
x = "0, 1, 2, 3" or '0, 1, 2, 3'

# in keyword
for each_item in x:
    print each_item

if("0" in x):
    print x

for each_item in x:
    if each_item == "0":
        print x
        break

# indexing
x[0] == "0" == x[-len(x)] == x[-10]


# slicing
x[0:2] == "0,"
x[-4:-2] == "2,"


# Length - number of elements
len(x) == 10
x[0] == "0" == x[-len(x)] == x[-10]

# min max
min(x)
max(x)

# index
min_index = x.index(min(x))
x[min_index]


# More commonly used sequence methods for strings
# upper lower and capitalize
x = "Not NOW"
x.lower() == "not now"
x.upper() == "NOT NOW"
x.capitalize() == "Not now"

# startswith and endswith
if (x.lower().startswith("n")):  # N____
    """stop"""
else:
    continue

if (x.lower().endswith("o")):  # _______o
    """stop"""
else:
    continue


"quit", "q", "Q", "no", "No", "NO"
condition = ("n", "q")
if (x.lower().startswith(condition)):  # n____ or q_____
    """stop"""
else:
    continue



# More commonly used sequence methods for lists
x = [0, 1, 2, 3]
x.append(4)
x == [0, 1, 2, 3, 4]

index = x.index(3)
value = x.pop(index)
x == [0, 1, 2, 4]

index4 = x.index(4)
x.insert(index4, value)
x == [0, 1, 2, 3, 4]


# sorting
x.reverse()
x == [4, 3, 2, 1, 0]

x.sort()
x == [0, 1, 2, 3, 4]


