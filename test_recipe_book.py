from recipe_book import *

def test_serialize_pizza_recipe():
    recipe = { "name": "Pizza", "ingredients": [{"name": "Frozen pizza", "amount": 1, "unit": "units"}], "instructions": "Bake in the oven." }
    r = Recipe(recipe)
    result = { "name": "Pizza", "ingredients": [{"name": "Frozen pizza", "amount": 1, "unit": "units"}], "instructions": "Bake in the oven." }
    assert r.serialize() == result

def test_serialize_recipe_book():
    recipeJSON = [{
        "name": "Nutella Powder",
        "ingredients": [
          {
            "name": "Nutella",
            "amount": 60,
            "unit": "grams"
          },
          {
            "name": "Tapioca Maltodextrin Powder",
            "amount": 40,
            "unit": "grams"
          }
        ],
        "instructions": "Weigh the stuff. Mix it together. Blend it. Enjoy!"
        },
        {
        "name": "Bittman Chinese Chicken With Bok Choy",
        "ingredients": [
          {
            "name": "Chicken Breast",
            "amount": 2,
            "unit": "units"
          },
          {
            "name": "Bok Choy",
            "amount": 1,
            "unit": "units"
          },
          {
            "name": "Sauce",
            "amount": 1,
            "unit": "deciliters"
          }
        ],
        "instructions": "Make sauce. Steam bok choy and chicken. Carry on steaming. Pour sauce over."
    }]
    book = RecipeBook(recipeJSON)
    result = [{
        "name": "Nutella Powder",
        "ingredients": [
          {
            "name": "Nutella",
            "amount": 60,
            "unit": "grams"
          },
          {
            "name": "Tapioca Maltodextrin Powder",
            "amount": 40,
            "unit": "grams"
          }
        ],
        "instructions": "Weigh the stuff. Mix it together. Blend it. Enjoy!"
      },
        {
        "name": "Bittman Chinese Chicken With Bok Choy",
        "ingredients": [
          {
            "name": "Chicken Breast",
            "amount": 2,
            "unit": "units"
          },
          {
            "name": "Bok Choy",
            "amount": 1,
            "unit": "units"
          },
          {
            "name": "Sauce",
            "amount": 1,
            "unit": "deciliters"
          }
        ],
        "instructions": "Make sauce. Steam bok choy and chicken. Carry on steaming. Pour sauce over."
      }]
    assert book.serialize() == result

def test_recipe_has_ingredient():
    recipe = { "name": "Pizza", "ingredients": [{
      "name": "Bok Choy",
      "amount": 1,
      "unit": "units"
    },
    {"name": "pizza",
     "amount": 1, "unit":
      "units"}],
    "instructions": "Bake in the oven." }
    r = Recipe(recipe)
    assert r.has_ingredient("pizza") == True

def test__eq__recipes():
    r1 = {
        "name": "Nutella Powder",
        "ingredients": [
        {
        "name": "Nutella",
        "amount": 60,
        "unit": "grams"
        },
        {
        "name": "Tapioca Maltodextrin Powder",
        "amount": 40,
        "unit": "grams"
        }
        ],
        "instructions": "Weigh the stuff. Mix it together. Blend it. Enjoy!"
        }
    r2 = {
        "name": "Nutella Powder",
        "ingredients": [
        {
        "name": "Nutella",
        "amount": 60,
        "unit": "grams"
        },
        {
        "name": "Tapioca Maltodextrin Powder",
        "amount": 40,
        "unit": "grams"
        }
        ],
        "instructions": "Weigh the stuff. Mix it together. Blend it. Enjoy!"
        }
    assert r1.__eq__(r2) == True

def test_recipes_with_ingredients():
    r1 = {
    "name": "Nutella Powder",
    "ingredients": [
    {
    "name": "Nutella",
    "amount": 60,
    "unit": "grams"
    },
    {
    "name": "Tapioca Maltodextrin Powder",
    "amount": 40,
    "unit": "grams"
    }
    ],
    "instructions": "Weigh the stuff. Mix it together. Blend it. Enjoy!"
    }
    r2 = {
    "name": "Bittman Chinese Chicken With Bok Choy",
    "ingredients": [
    {
    "name": "Chicken Breast",
    "amount": 2,
    "unit": "units"
    },
    {
    "name": "Bok Choy",
    "amount": 1,
    "unit": "units"
    },
    {
    "name": "Nutella",
    "amount": 1,
    "unit": "deciliters"
    }
    ],
    "instructions": "Make sauce. Steam bok choy and chicken. Carry on steaming. Pour sauce over."
    }
    recipes = [r1, r2]
    result = [Recipe(r1), Recipe(r2)]
    book = RecipeBook(recipes)
    assert book.recipes_with_ingredient("Nutella") == result
