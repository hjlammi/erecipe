import json
from flask import Flask, request, Response
from recipe_book import RecipeBook
app = Flask(__name__)

def get_recipes_from_JSONfile(file_name):
    with open(file_name, encoding='utf-8') as recipes_file:
        return json.load(recipes_file)

recipes = get_recipes_from_file('eresepti/recipes.json')
book = RecipeBook(recipes)

@app.route("/")
def recipes():
    return json.dumps(book.serialize())

@app.route("/recipes")
def get():
    ingredient = request.args.get('ingredient')
    recipes_with_ingr = book.recipes_with_ingredient(ingredient)
    return Response(json.dumps(recipes_with_ingr), mimetype="application/json")
