title = "Combat information"
print title
print "-" * 40

attack_power = raw_input("What is the attack power? ")
percent_to_hit = raw_input("What is the percent to hit? ")  # this is a string
percent_to_hit = float(percent_to_hit)

print "-" * 40
print "Attack Power:", attack_power, "points"
print "Percent to Hit:", percent_to_hit * 100, "%"
print "-" * 40
