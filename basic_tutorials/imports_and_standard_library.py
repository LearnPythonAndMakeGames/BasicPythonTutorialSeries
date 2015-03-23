import random

attack_power = raw_input("What is the attack power? ")
percent_to_hit = raw_input("What is the percent to hit? ")

attack_power = int(attack_power)
percent_to_hit = float(percent_to_hit)

random.seed(0)

damage_value = random.randint(1, attack_power)
chance_to_hit = random.random()


print '-'*40
print "Attack Power:", attack_power
print "Percent to Hit:", percent_to_hit
print '-'*40
print 'Calculated'
print '-'*40
print "Damage Value:", damage_value
print "Chance to hit:", chance_to_hit
print '-'*40
