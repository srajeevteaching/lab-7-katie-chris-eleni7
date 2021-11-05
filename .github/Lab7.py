#Chris, Katie, Eleni
#Lab7
#CS-151
#11/4/21

import random

def get_number_of_rolls():
    return (int(input("Enter the # of rolls: ")))

def get_roll_dice(roll1, roll2):
    return roll1 + roll2

def get_print_histogram(index_list):
    for i in range(11):
        print("\n")
        for j in range(i + 1):
            print ("*", end = " ")
    print()

def main():
    rolls = get_number_of_rolls()
    if rolls < 0:
        print("Invalid input")
        get_number_of_rolls()

    index_list = [0,0,0,0,0,0,0,0,0,0,0]

    count = 0
    while count < rolls:
        roll1 = (random.randint(1, 6))
        roll2 = (random.randint(1, 6))
        count += 1
        dice_sum = get_roll_dice(roll1, roll2)
        index_list[dice_sum - 2] += 1
    print(index_list)
    get_print_histogram(index_list)

main()

