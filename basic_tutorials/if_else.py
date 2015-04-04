import random

# Ask player what the attack power and percent to hit are
attack_power = raw_input("What is the attack power? ")
percent_to_hit = raw_input("What is the percent to hit? ")

# Fix attack power and percent to hit so they are not strings
attack_power = int(attack_power)
percent_to_hit = float(percent_to_hit)

# Sets the random pattern
# random.seed(0)

# Check if the creature was hit
chance_to_hit = random.random()
if chance_to_hit <= percent_to_hit:
    creature_was_hit = True
else:
    creature_was_hit = False

# if the creature was hit, then calculate the damage
if (creature_was_hit):
    # we hit the creature
    damage_value = random.randint(1, attack_power)
else:
    # we didn't hit the creature
    damage_value = 0


print '-' * 40
print "Attack Power:", attack_power
print "Percent to Hit:", percent_to_hit
print '-' * 40
print 'Calculated'
print '-' * 40
print 'Creature was hit:', creature_was_hit
print "Damage Value:", damage_value
print "Chance to hit:", chance_to_hit
print '-' * 40
