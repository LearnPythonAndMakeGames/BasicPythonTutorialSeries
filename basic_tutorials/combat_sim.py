"""
Combat Sim
----------
Inspired by Ben Arnold's:  Making Games with Ben Series

Cowboys vs Aliens

Requirements:
* Cowboys and aliens attack each other to the death
* Cowboys and aliens attack each other simultaneously
* Each cowboy and alien have a chance to hit < 100%
* Human or player can input the number of cowboys and number of aliens
* Rerun with same numbers


Design:

    Data:
        Cowboys:
            health: 100
            attack power: 35
            percent to hit: 0.5 or 50%
        Aliens:
            health: 200
            attack power: 20
            percent to hit: 0.2 or 20%
        Set random seed

    Functions:
        Attack:
            health
            attack power
            percent to hit
        Simulation:
            how many cowboys?  default is 40
            how many aliens?  default is 500
        Capture Input:
            numbers
            rerun


Implementation:

    Hint 1:  There should be at least 8 variables.
    Hint 2:  attack(health, attack_power, percent_to_hit) and return new health
    Hint 3:  consider using 'while loops' in simulation and cowboys and aliens
             attack each other simultaneously

    Hint 4:  Commented function definitions

        def attack(health, power, percent_to_hit):
            # Calculates health from percent to hit and power of hit
            # if our random number falls between 0 and percent to hit
                # then a hit occurred so we reduce health by power
            # return the new health value

        def simulate_army(number_of_cowboys=45, number_of_aliens=500):
            # Simulates combat between cowboys and aliens
            # setup cowboy data
            # setup alien data

            # while we still have cowboys and aliens
                # have cowboys and aliens attack until one dies
                # update cowboy or alien count

            # display remaining cowboys and aliens


        # Capture the number of cowboys and aliens

        # While we should rerun
            # run the simulation
            # ask if we should rerun and set the value

Test:

Passed:
* Cowboys and aliens attack each other to the death
* Cowboys and aliens attack each other simultaneously
* Human or player can input the number of cowboys and number of aliens
* Each cowboy and alien have a chance to hit < 100%
* Rerun with same numbers
"""
import random


def attack(health, power, percent_to_hit):
    """Calculates health from percent to hit and power of hit

    Parameters:
        health - integer defining health of attackee
        power - integer defining damage of attacker
        percent to hit - float defining percent chance to hit of attacker

    Returns: new health
    """
    random_number = random.random()  # number between 0.0 and 1.0
    # if our random number falls between 0 and percent to hit
    if random_number <= percent_to_hit:
        # then a hit occurred so we reduce health by power
        health = health - power
    # return the new health value
    return health


def simulate_army(number_of_cowboys=45, number_of_aliens=500):
    """Simulates combat between cowboys and aliens

    Parameters:
        number of cowboys - integer representing number of cowboys
        number of aliens - integer representing number of aliens

    Returns: nothing
    """
    # setup cowboy data
    cowboy_starting_health = 100
    cowboy_attack_power = 35
    cowboy_percent_to_hit = 0.5

    # setup alien data
    alien_starting_health = 200
    alien_attack_power = 20
    alien_percent_to_hit = 0.2

    # Initialize cowboys and aliens
    cowboy = cowboy_starting_health
    alien = alien_starting_health
    rounds = 0
    # while we still have cowboys and aliens
    while(number_of_cowboys > 0 and number_of_aliens > 0):
        # have cowboys and aliens attack until one dies
        while(cowboy > 0 and alien > 0):
            rounds = rounds + 1
            cowboy = attack(cowboy, alien_attack_power, alien_percent_to_hit)
            alien = attack(alien, cowboy_attack_power, cowboy_percent_to_hit)
            print rounds, cowboy, alien
        # update cowboy or alien count
        if cowboy > 0:
            number_of_aliens = number_of_aliens - 1
            alien = alien_starting_health
        elif alien > 0:
            number_of_cowboys = number_of_cowboys - 1
            cowboy = cowboy_starting_health
        else:
            number_of_aliens = number_of_aliens - 1
            alien = alien_starting_health
            number_of_cowboys = number_of_cowboys - 1
            cowboy = cowboy_starting_health

    # display remaining cowboys and aliens
    print "Cowboys remaining:", number_of_cowboys
    print "Aliens remaining:", number_of_aliens
    print "Number of rounds:", rounds


# Capture the number of cowboys and aliens
number_of_cowboys = raw_input("How many cowboys? ")
number_of_aliens = raw_input("How many aliens? ")

number_of_cowboys = int(number_of_cowboys)
number_of_aliens = int(number_of_aliens)

rerun = True
# While we should rerun
while(rerun):
    # run the simulation
    simulate_army(number_of_cowboys, number_of_aliens)
    # ask if we should rerun and set the value
    rerun = raw_input("Rerun ([Y]/n)? ")
    if rerun.lower().startswith(("n", "q")):  # n, N, No, NO, no, nO, ...
        rerun = False
    else:
        rerun = True
