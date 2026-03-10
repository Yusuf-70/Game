from random import randint, random

def roll_dice():
    return randint(1, 6)

for _ in range(10):
    print(roll_dice())

input("Press enter to continue to roll the dice")

def generate_target_number(lower_limit=17, upper_limit=29, roll=None):
    print ("You rolled:", roll)
    total = lower_limit + (upper_limit - lower_limit) * roll


    

