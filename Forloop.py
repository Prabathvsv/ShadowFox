                                                                                              # task 1
# Explanation: Defines a function 'roll_dice' to simulate rolling a die multiple times and tracks occurrences of specific outcomes such as rolling a 6, rolling a 1, and rolling double 6s.
import random


def roll_dice(num_rolls):
    COUNT_6 = 0
    COUNT_1 = 0
    COUNT_DOUBLE_6 = 0
    prev_roll = None
    DIE_RANGE = (1, 6)

    for _ in range(num_rolls):
        roll = random.randint(*DIE_RANGE)

        # Check for occurrences
        if roll == 6:
            COUNT_6 += 1
        elif roll == 1:
            COUNT_1 += 1
        if roll == prev_roll == 6:
            COUNT_DOUBLE_6 += 1

        prev_roll = roll

    # Print statistics
    print(f"Occurrences of Dice 6: {COUNT_6} times")
    print(f"Occurrences of Dice 1: {COUNT_1} times")
    print(f"Occurrences of double 6s: {COUNT_DOUBLE_6} times")


roll_dice(20)
                                                               #task-2
# Explanation: Simulates a jumping jack workout session with user interaction. It performs jumping jacks in sets of 10 until completed or until the user indicates tiredness or completion.
total_jumping_jacks = 100

while total_jumping_jacks > 0:
    set_size = min(10, total_jumping_jacks)
    print(f"Performing {set_size} jumping jacks...")
    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip_remaining = input(
            "Do you want to skip the remaining sets? (yes/no): "
        ).lower()
        if skip_remaining == "yes" or skip_remaining == "y":
            print(
                f"You completed a total of {100 - total_jumping_jacks} jumping jacks."
            )
            break
        else:
            print("Continuing with the next set...")
    else:
        total_jumping_jacks -= set_size
        if total_jumping_jacks == 0:
            print("Congratulations! You completed the workout.")
        else:
            print(f"{total_jumping_jacks} jumping jacks remaining.")
