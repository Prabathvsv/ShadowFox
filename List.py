# Task 1
# Explanation: Defines a list 'justice_league' containing the initial members of the Justice League.

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern",
]

# 1
# Explanation: Calculates the number of members in the Justice League and prints the result.
no_members = len(justice_league)
print("the number of members is", no_members, "members")

# 2
# Explanation: Adds new members to the Justice League using the 'extend' method without using 'append' and prints the updated list.
new_members = "Batgirl", "Nightwing"
justice_league.extend(new_members)
print("the new members have been added", justice_league)

# 3
# Explanation: Removes 'Wonder Woman' from the list, then inserts her back at the beginning and prints the updated list.
wonder_woman = justice_league.pop(2)
justice_league.insert(0, wonder_woman)
print("the new order is", justice_league)

# 4
# Explanation: Removes 'Superman' from the list, then inserts him back after 'Aquaman' and prints the updated list.
removed_hero = "Superman"
justice_league.remove(removed_hero)
justice_league.insert(justice_league.index("Aquaman"), removed_hero)
print("The new order after separating Aquaman and Flash is:", justice_league)

# 5
# Explanation: Updates the list with a new team assembled by Superman and prints the updated list.
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("The new team assembled by Superman:", justice_league)

# 6
# Explanation: Sorts the list alphabetically and prints the sorted list along with the new leader.
justice_league.sort()
print(
    "The sorted list of Justice League members is:",
    justice_league,
    "and the new leader is",
    justice_league[0],
)
