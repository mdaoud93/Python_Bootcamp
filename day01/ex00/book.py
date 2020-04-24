from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if (not isinstance(name, str)):
            raise TypeError("\033[93mName must be of type 'str'\033[0m")
        if (not name):
            raise ValueError("\033[93mName cannot be empty\033[0m")
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rec_list in self.recipe_list.values():
            for item in rec_list:
                if (item.name == name):
                    return(item)
    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type in self.recipe_list):
            for item in self.recipe_list[recipe_type]:
                print(item.name + " ", end='')
            print()

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now
    def print_all(self):
        for rec_list in self.recipe_list.values():
            for item in rec_list:
                print (item)
