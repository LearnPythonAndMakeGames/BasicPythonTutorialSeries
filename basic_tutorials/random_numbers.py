#!/usr/bin/env python
import random

# random.seed(0)

health = 100
print "Health starts at:", health


def hit(health):
    """Hits health for a random number between 1 and 10"""
    hit_value = random.randint(1, 10)
    print "hits for:", hit_value
    health = health - hit_value
    print "health now:", health
    return health

for every_number in xrange(10):
    health = hit(health)

print "Final Value:", health
