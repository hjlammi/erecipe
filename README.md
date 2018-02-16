# Installing dependencies

First make sure you have [Python3](https://www.python.org/downloads/) and [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) installed.

```shell
# Create a new virtualenv
virtualenv venv

# Activate the virtualenv (if you use Bash)
source venv/bin/activate

# Activate the virtualenv (if you use Fish)
source venv/bin/activate.fish

# Install the dependencies
pip install -r requirements.txt
```

# Starting the server

Start the server with the command `env FLASK_APP=recipes.py flask run`

# Making requests to the server

The server listens at http://127.0.0.1:5000.

You can view all the recipes with a GET request to http://127.0.0.1:5000/recipes.

Recipes can be searched with the name of an ingredient, eg. http://127.0.0.1:5000/recipes?ingredient=Nutella.
The case of the search parameter doesn't matter so "Nutella" and "nutella" give the same result.

If an ingredient name consists of several words, those words can be
used in searches. E.g., if the ingredient is "Bok Choy", both "Bok" and "Choy" can be used to search for a recipe.

The recipes are shown in JSON format.
