# Task 1
# Explanation: Defines a function 'representation' that takes two arguments, num and char. It checks if num is an integer, if not, it returns an error message. Then, it constructs and returns a string containing the number and the character.
def representation(num, char):
    # Check if num is a valid integer
    if not isinstance(num, int):
        return "Invalid input for num: '{}' is not an integer".format(num)
    string = "Number: {:d}, letter: '{}'".format(num, char)
    return string


answers = representation(45, "o")
print(answers)


# Task 2
# Explanation: Defines a function 'area' that calculates the area of a circle given the radius and pi value. It then calculates the area of a pond using the 'area' function and computes the total water in the pond based on the given square meter value.
def area(radius, pi):
    calculation = pi * (radius**2)
    return calculation


pi = 3.14
result = area(10, pi)
print("Area of the pond is ", int(result), "meters")

square_meter = 1.4
total_water = result * square_meter
print("Total water of the pond is ", int(total_water), "meters")


# Task 3
# Explanation: Defines a function 'my_speed' that calculates speed given distance and time. It calculates the speed and prints the result.
def my_speed(distance, time):
    speed = distance / time
    return speed


answer = my_speed(490, 7)
print("My speed is ", int(answer), "meters per second")
