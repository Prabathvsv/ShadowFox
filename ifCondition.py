                                                                              # task 1
# Explanation: Calculates BMI (Body Mass Index) based on user input of height and weight, and provides an interpretation of the result.
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))


def BMI(height, weight):
    bmi = weight / (height * height)
    if bmi >= 30:
        answer = "Obesity"
    elif bmi >= 25:
        answer = "Overweight"
    elif bmi >= 18.5 and bmi < 25:
        answer = "Normal"
    else:
        answer = "Underweight"
    return answer, bmi


answer, calculated_bmi = BMI(height, weight)
print("Your BMI answer is:", answer)
print("Your calculated BMI value is:", calculated_bmi)

                                                                          # task 2
# Explanation: Determines the country of a given city based on predefined lists of cities for Australia, UAE, and India.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Please enter a city name: ")


def Country(city_name):
    if city_name in Australia:
        return f"{city_name} is in Australia"
    elif city_name in UAE:
        return f"{city_name} is in UAE"
    elif city_name in India:
        return f"{city_name} is in India"
    else:
        return "City not found in the lists."


# calling the function
print(Country(city_name))

                                                                    # task 3
# Explanation: Checks if two given cities belong to the same country based on predefined lists of cities for Australia, UAE, and India.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Please enter a city name: ")
city_name_two = input("Please enter the second city name: ")


def Country(city_name, city_name_two):
    if city_name in Australia and city_name_two in Australia:
        return "Both cities are in Australia"
    elif city_name in UAE and city_name_two in UAE:
        return "Both cities are in UAE"
    elif city_name in India and city_name_two in India:
        return "Both cities are in India"
    else:
        return "They do not belong in the same country"


# calling the function
print(Country(city_name, city_name_two))
