import random


def attack(attack_power, percent_to_hit, percent_to_critical=0.01):
    """Calculates the damage done based on attack power and percent to
    hit.  Also calculates critical strike.

    Parameters:
        attack_power - attack power
        percent_to_hit - percent to hit

    Optional:
        percent_to_critical - percent to critical strike [default: 0.01]

    Returns:
       Returns damage
    """
    damage_value = 0

    # Calculate if creature was hit
    chance_to_hit = random.random()
    if chance_to_hit <= percent_to_hit:
        creature_was_hit = True
    else:
        creature_was_hit = False

    # Calculate final damage value
    if creature_was_hit:
        damage_value = random.randint(1, attack_power)
        if chance_to_hit <= percent_to_critical:
            damage_value = attack_power + damage_value

    return damage_value

attack_power = raw_input("What is the attack power? ")
percent_to_hit = raw_input("What is the percent to hit? ")
percent_to_critical = raw_input("What is the percent to critical? ")

attack_power = int(attack_power)
percent_to_hit = float(percent_to_hit)
percent_to_critical = float(percent_to_critical)

player_wants_to_continue = True
while(player_wants_to_continue):
    print attack(attack_power, percent_to_hit, percent_to_critical)
    answer = raw_input("Continue ([Y]/n)? ")
    if answer == "n":
        player_wants_to_continue = False

