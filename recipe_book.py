import json

# RecipeBook and Recipe classes

class RecipeBook:
    # Add all recipes in the book.
    def __init__(self, recipes):
        self.recipes = []
        for recipe in recipes:
            # Create new recipe that is appended to the recipes list.
            new_recipe = Recipe(recipe)
            self.recipes.append(new_recipe)

    # Returns recipes in a list that can be passed to JSON.dumps.
    def serialize(self):
        serialized_recipes = []
        for recipe in self.recipes:
            serialized_recipes.append(recipe.serialize())
        return serialized_recipes

    # Finds recipes that include the ingredient name which is given as a parameter.
    # Returns a list with the found recipes and if no recipe has the name as an ingredient
    # an empty list is returned.
    def recipes_with_ingredient(self, name):
        recipes_with_ingredient = []
        for recipe in self.recipes:
            if recipe.has_ingredient(name):
                recipes_with_ingredient.append(recipe.serialize())
            else:
                pass
        return recipes_with_ingredient

class Recipe:
    # Initializing a recipe.
    def __init__(self, recipe):
        self.name = recipe["name"]
        self.ingredients = []
        for i in recipe["ingredients"]:
            ingredients = {"name": i["name"],
                           "amount": i["amount"],
                           "unit": i["unit"]}
            self.ingredients.append(ingredients)
        self.instructions = recipe["instructions"]

    # Returns recipe in a dict form that can be turned into JSON format.
    def serialize(self):
        return {"name": self.name, "ingredients": self.ingredients, "instructions": self.instructions}

    # Checks if an ingredient is included in a recipe.
    # Gets the name or a partial name of an ingredient as a parameter.
    def has_ingredient(self, name):
        # The case of the parameter is ignored.
        name = name.lower()
        found = False
        for i in self.ingredients:
            # Checks if the ingredient name or part of it is in the ingredients list.
            # Capitalization of the ingredient name is removed to be able to compare to the name parameter.
            if name == i["name"].lower() or name in i["name"].lower():
                found = True
                break
            else:
                found = False
        return found
