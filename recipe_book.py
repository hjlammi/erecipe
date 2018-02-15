import json

class RecipeBook:
    def __init__(self, recipes):
        self.recipes = []
        for recipe in recipes:
            new_recipe = Recipe(recipe)
            self.recipes.append(new_recipe)

    def serialize(self):
        serialized_recipes = []
        for recipe in self.recipes:
            serialized_recipes.append(recipe.serialize())
        return serialized_recipes

    def recipes_with_ingredient(self, name):
        recipes_with_ingredient = []
        for recipe in self.recipes:
            if recipe.has_ingredient(name):
                recipes_with_ingredient.append(recipe.serialize())
            else:
                pass
        return recipes_with_ingredient

class Recipe:
    def __init__(self, recipe):
        self.name = recipe["name"]
        self.ingredients = []
        for ingredient in recipe["ingredients"]:
            ingred = { "name" : ingredient["name"],
                       "amount" : ingredient["amount"],
                       "unit" : ingredient["unit"]}
            self.ingredients.append(ingred)
        self.instructions = recipe["instructions"]

    # def __str__(self):
    #     return (self.name + "\n" + str(len(self.ingredients)) + "\n" + self.ingredients[0]["unit"] +
    #             "\n" + self.instructions)

    def __eq__(self, other):
        if (self.name == other.name and
            self.instructions == other.instructions and
            self.ingredients == other.ingredients):
            return True
        else:
            return False

    def serialize(self):
        return { "name": self.name, "ingredients": self.ingredients, "instructions": self.instructions }

    def has_ingredient(self, name):
        name = name.capitalize()
        found = False
        for i in self.ingredients:
            if i["name"] == name:
                found = True
                break
            else:
                found = False
        return found

# def get_recipes_from_file():
#     with open('eresepti/recipes.json', encoding='utf-8') as recipes_file:
#         recipes = json.load(recipes_file)
#         return recipes
#
# if __name__ == "__main__":
#     recipes = get_recipes_from_file()
#     book = RecipeBook(recipes)
