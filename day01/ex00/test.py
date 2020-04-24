from recipe import Recipe
from book import Book

def recipe_test():
    # Name check
    rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], "Meal", "lunch")   # No errors
    del rec
    rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec
    rec = Recipe(22, 1, 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec
    rec = Recipe("", 1, 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec

    # Cooking level check
    rec = Recipe("Sanwich", -9, 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec
    rec = Recipe("Sanwich", 6, 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec
    rec = Recipe("Sanwich", "Nine", 10, ["Ham", "Bread"], "Meal", "lunch")
    del rec

    # Cooking time check
    rec = Recipe("Sanwich", 1, "30 minutes", ["Ham", "Bread"], "Meal", "lunch")
    del rec
    rec = Recipe("Sanwich", 1, -90, ["Ham", "Bread"], "Meal", "lunch")
    del rec

    # Ingredients check
    rec = Recipe("Sanwich", 1, 10, [], "Meal", "lunch")
    del rec
    rec = Recipe("Sanwich", 1, 10, "Ham", "Meal", "lunch")
    del rec

    # Description check
    rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], 22, "lunch")
    del rec

    # Recipe type check
    rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], "Meal", "Bla")
    del rec
    rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], "Meal", ["lunch", "dessert"])
    del rec


# def book_test_invalid():
#     book = Book("")
#     del book
#     book = Book()
#     del book

def book_test():
    book = Book("cookbook")
    print("Cookbook creation date: " + book.creation_date.strftime("%d/%m/%y"))
    rec = Recipe("Sandwich", 1, 10, ["Ham", "Bread"], "Meal", "lunch")
    book.add_recipe(rec)
    rec = Recipe("Cereals", 1, 2, ["Cereals", "Milk"], "To be eaten in the morning", "starter")
    book.add_recipe(rec)
    rec = Recipe("Cake", 3, 20, ["Flour", "Butter", "Eggs"], "After meal", "dessert")
    book.add_recipe(rec)
    # book.print_all()
    book.get_recipes_by_type("lunch")
    rec = book.get_recipe_by_name("Cereals")
    print(rec)

book_test()
# recipe_test()
# book_test()
# rec = Recipe("Sanwich", 1, 10, ["Ham", "Bread"], "Meal", "lunch")
# print(rec)

