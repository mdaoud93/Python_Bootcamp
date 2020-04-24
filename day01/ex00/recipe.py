


class Recipe:
    def __init__(
        self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type
    ):
        if (not isinstance(name, str)):
            raise TypeError("\033[93mName must be of type 'str'\033[0m")
        if (not name):
            raise ValueError("\033[93mName cannot be empty\033[0m")
        self.name = name
        if (not isinstance(cooking_lvl, int)):
            raise TypeError("\033[93mCooking level must be of type 'int'\033[0m")
        if (cooking_lvl not in range(1, 6)):
            raise ValueError("\033[93mCooking level must be between 1 and 5\033[0m")
        self.cooking_lvl = cooking_lvl
        if (not isinstance(cooking_time, int)):
            raise TypeError("\033[93mCooking time must be of type 'int'\033[0m")
        if (cooking_time < 0):
            raise ValueError("\033[93mCooking time cannot be negative\033[0m")
        self.cooking_time = cooking_time
        if (not isinstance(ingredients, list)):
            raise TypeError("\033[93mIngredients must be of type 'list'\033[0m")
        if (not ingredients):
            raise ValueError("\033[93mIngredients cannot be empty\033[0m")
        self.ingredients = ingredients
        if (not isinstance(description, str)):
            raise TypeError("\033[93mDesciption must be of type 'str'\033[0m")
        self.description = description
        if (recipe_type not in ("starter", "lunch", "dessert")):
            raise ValueError("\033[93mType must be 'starter', 'lunch' or 'dessert'\033[0m")
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe for "
        txt += "\033[32m" + self.name + "\033[0m :\n"
        if (self.description):
            txt += "\033[34mDesciption:\t\t\033[0m" + self.description + "\n"
        txt += "\033[34mMeal type:\t\t\033[0m" + self.recipe_type + "\n"
        txt += "\033[34mCooking level:\t\t\033[0m" + str(self.cooking_lvl) + "\n"
        txt += "\033[34mCooking time:\t\t\033[0m" + str(self.cooking_time) + " minutes\n"
        txt += "\033[34mIngredients:\t\t\033[0m" + str(self.ingredients) + "\n"
        return txt
