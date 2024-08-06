import ipdb
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Define a function `get_names()` that takes a list of `spicy_foods` and
# **returns a list of strings** with the names of each spicy food.

def get_names(spicy_foods):
    return[food['name'] for food in spicy_foods]

# Define a function `get_spiciest_foods()` that takes a list of `spicy_foods` and
# **returns a list of dictionaries** where the heat level of the food is greater
# than 5.

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food['heat_level'] > 5]

# Define a function `print_spicy_foods()` that takes a list of `spicy_foods` and
# **output to the terminal** each spicy food in the following format using
# `print()`: `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.

# HINT: you can use [times (\*) with a string][string times] to produce the
# correct number of "🌶" emojis.
    
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")        
    
    # for food in spicy_foods: 
    #     name = food.get('name')
    #     cuisine = food.get('cuisine')
    #     heat_level = food.get('heat_level')
    #     heat_emoji = '🌶️' * heat_level
    #     print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
    # pass
    # print(f"{food['name']} ({food['cuisine']}))

    

# Define a function `get_spicy_food_by_cuisine()` that takes a list of
# `spicy_foods` and a string representing a `cuisine`, and **returns a single
# dictionary** for the spicy food whose cuisine matches the cuisine being passed
# to the method.

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    
# Define a function `print_spiciest_foods()` that takes a list of `spicy_foods`
# and **outputs to the terminal** ONLY the spicy foods that have a heat level
# greater than 5, in the following format:

# `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.

# Try to use functions you've already written to solve this!

# ```py
# print_spiciest_foods(spicy_foods)
# # => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# # => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
# ```    
def print_spiciest_foods(spicy_foods):
    # spiciest_foods = get_spiciest_foods(spicy_foods)
    # print_spicy_foods(spiciest_foods)

    # def print_spiciest_foods(spicy_foods):
    # Filter spicy foods with heat level greater than 5
    # spiciest_foods = [food for food in spicy_foods if food.get('heat_level') > 5]
    # Iterate over each food and print the formatted string
    # for food in spiciest_foods:
    #     name = food.get('name')
    #     cuisine = food.get('cuisine')
    #     heat_level = food.get('heat_level')
    #     # Format the output string
    #     heat_emoji = '🌶️' * heat_level
    #     print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
    spiciest_foods = get_spiciest_foods(spicy_foods) 
    print_spicy_foods(spiciest_foods) 
    
    # print_spiciest_foods(spicy_foods)
# Define a function `average_heat_level()` that takes a list of `spicy_foods` and
# **returns an integer** representing the average heat level of all the spicy
# foods in the array. Recall that to derive the average of a collection, you need
# to calculate the total and divide number of elements in the collection.

# 1) Python Average: Len() and Sum()
# The Sum() and Len() functions are built-in in Python and are used to find the averages. 
# This method of finding the average helps avoid looping through the list and hence is time and effort-saving. This also reduces redundancy and helps maintain DRY code since it helps in finding the average of a list using a single line.
# average = sum(numbers)/len(numbers)
# def get_average_heat_level(spicy_foods):
# #     total_heat = sum(food['heat_level'] for food in spicy_foods) 
# #     return total_heat // len(spicy_foods) 

# #print(get_average_heat_level(spicy_foods)) 
def get_average_heat_level(spicy_foods):
    return sum(food['heat_level'] for food in spicy_foods) / len(spicy_foods)

# Define a function `create_spicy_food()` that takes a list of `spicy_foods` and a
# new `spicy_food` and returns the original list with the new `spicy_food` added.

# Example:

# ```py
# create_spicy_food(
#     spicy_foods,
#     {
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
#     }
# )


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food) 
    return spicy_foods
 
new_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
spicy_foods = create_spicy_food(spicy_foods, new_food)

# ipdb.set_trace()



