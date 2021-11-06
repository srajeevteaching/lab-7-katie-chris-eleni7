#Chris, Katie, Eleni
#Lab7
#CS-151
#11/4/21

import random

def get_number_of_rolls():
    while True:
        r = input("Enter the # of rolls: ")
        if r.isdigit():
            break
    return int(r)

def get_roll_dice(roll1, roll2):
    return roll1 + roll2

def get_print_histogram(index_list):
    for i in range(len(index_list)):
        print(i, "\t","*" * index_list[i])

def main():
    index_list = [0,0,0,0,0,0,0,0,0,0,0]
    count = 0
    rolls = get_number_of_rolls()
    while count < rolls:
        roll1 = (random.randint(1, 6))
        roll2 = (random.randint(1, 6))
        count += 1
        dice_sum = get_roll_dice(roll1, roll2)
        index_list[dice_sum - 2] += 1
    print(index_list)
    get_print_histogram(index_list)

main()

