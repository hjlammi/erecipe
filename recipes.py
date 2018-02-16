import json
from flask import Flask, request, Response, redirect
from recipe_book import RecipeBook
app = Flask(__name__)

def get_recipes_from_JSONfile(file_name):
    with open(file_name, encoding='utf-8') as recipes_file:
        return json.load(recipes_file)

recipes = get_recipes_from_JSONfile('eresepti/recipes.json')
book = RecipeBook(recipes)

@app.route("/")
def recipes():
    return redirect('/recipes')

@app.route("/recipes")
def get():
    ingredient = request.args.get('ingredient')
    if ingredient:
        result = book.recipes_with_ingredient(ingredient)
    else:
        result = book.serialize()
    return Response(json.dumps(result), mimetype="application/json")
