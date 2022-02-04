import math


def picky_piggy(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2

    seven_starter = 7.14285
    position_of_n_in_seven_starter = score%6
    ones_place = seven_starter*(10**position_of_n_in_seven_starter)
    no_decimals = math.floor(ones_place)
    none_to_left = no_decimals%10

    return none_to_left

print(picky_piggy(0))
print(picky_piggy(1))
print(picky_piggy(2))
print(picky_piggy(3))
print(picky_piggy(4))
print(picky_piggy(16))