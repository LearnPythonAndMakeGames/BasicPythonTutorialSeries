attack_power = 100

# Print keyword  only available python 2 and lower.
print "Attack Power:", attack_power
print "Attack Power: {} points".format(attack_power)
print "Attack Power: {attack_power} points".format(attack_power=100)

print "Attack Power: %s" % (attack_power)  # python 1 and 2... won't work on 3

# Print as a built-in function
print("Attack Power:", attack_power)
print("Attack Power: {} points".format(attack_power))
#                                       0th           1st             ...
print("Attack Power: {0} points".format(attack_power, percent_to_hit, ...))
print("Attack Power: {attack_power} points".format(attack_power=100))

print "Attack Power".lower()  # attack power
print "Attack Power".upper()  # ATTACK POWER
print "Attack Power".capitalize()  # Attack power


print ":".join("Attack Power", "{}".format(attack_power))  # Attack Power : 100
print "Attack " + "Power"  # Attack Power

for character in "Attack Power":
    print character  #  A t t a c k  P o w e r  <--- each on its own line
    # A
    # t
    # t

ap_string = "Attack Power"
if "attack power" == ap_string.lower():
    pass

