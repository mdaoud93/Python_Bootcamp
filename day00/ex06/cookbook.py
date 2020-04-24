import sys

def add_recipe(cookbook):
    ingr = []
    '''Add a recipe to the cookbook, if the recipe exists, it will be updated'''
    rec_name = input("Enter the name of the recipe\t")
    ingr_number = int(input("Enter the number of ingredients\t"))
    for i in range (ingr_number):
        ingr_name = input("Enter the ingredient number " + str(i + 1) + "\t")
        ingr.append(ingr_name)
    meal = input("Enter the meal description\t")
    prep_time = input("Enter the preperation time\t")
    new_recipe = {
        'ingredients': ingr,
        'meal': meal,
        'prep_time': prep_time
    }
    cookbook[rec_name] = new_recipe
    print("\033[32mRecipe added successfully!!\033[0m")


def print_recipe(cookbook):
    '''Print the details of a recipe in the cookbook'''
    rec_name = input("Enter the recipe name for more details ")
    # if (rec_name is None):
    #     print("\033[31mError, please provide a recipe name\033[0m")
    #     return
    if (rec_name not in cookbook):
        print("\033[31mError\033[0m, the entry \'" + rec_name + "\' not found")
        return
    print("Recipe for \033[34m" + str(rec_name) + "\033[0m:")
    print("\033[32mIngredients\033[0m:\t\t", end='')
    print(cookbook[rec_name]['ingredients'])
    print("\033[32mMeal type\033[0m:\t\t", end='')
    print(cookbook[rec_name]['meal'])
    print("\033[32mPreperation time\033[0m:\t", end='')
    print(cookbook[rec_name]['prep_time'])


def delete_recipe(cookbook):
    '''Remove a recipe from the cookbook'''
    rec_name = input("Enter the name of the recipe you would like to remove")
    if (rec_name not in cookbook):
        print("\033[31mError\033[0m, the entry \'" + rec_name + "\' not found")
        return
    del(cookbook[rec_name])

def print_cookbook(cookbook):
    '''Print all recipes in the cookbook'''
    print("Printing all recipes in the cookbook")
    for k in cookbook.keys():
        print("Recipe for \033[34m" + str(k) + "\033[0m:")
        print("\033[32mIngredients\033[0m:\t\t", end='')
        print(cookbook[k]['ingredients'])
        print("\033[32mMeal type\033[0m:\t\t", end='')
        print(cookbook[k]['meal'])
        print("\033[32mPreperation time\033[0m:\t", end='')
        print(cookbook[k]['prep_time'])


sandwich_rec = {
    'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
    'meal': 'lunch',
    'prep_time': '10 minutes'
}

salad_rec = {
    'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
    'meal': 'lunch',
    'prep_time': '15 minutes'
}

cake_rec = {
    'ingredients': ['flour', 'sugar', 'eggs'],
    'meal': 'to be eaten for dessert',
    'prep_time': '60 minutes'
}

cookbook = {
    'sandwich': sandwich_rec,
    'salad': salad_rec,
    'cake': cake_rec
}


option = 0
while (option != 5):
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        option = int(input())
    except ValueError:
        print("\033[31mError\033[0m, please choose a number from the list above, 5 to exit")
        continue
    if (not option in range(1, 6)):
        print("\033[31mError\033[0m, please choose a number from the list above, 5 to exit")
        continue
    if (option == 1):
        add_recipe(cookbook)
    if (option == 2):
        delete_recipe(cookbook)
    if (option == 3):
        print_recipe(cookbook)
    if (option == 4):
        print_cookbook(cookbook)
    if (option == 5):
        print("\033[34mClosing the cookbook\033[0m")
        sys.exit(0)
