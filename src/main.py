from flask import Flask, render_template
from cocktails import Cocktails
import json

app = Flask(__name__)

with open("app/config.json", "r") as cf:
    config = json.load(cf)


@app.route("/")
def root():
    """
        Default response
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    # print(json.dumps(data, indent=2))
    return render_template("showcocktail.html", data=drinks.getRandom(), heading=heading)


@app.route("/cocktail/<name>")
def cocktail_name(name):
    """
        Search for a cocktail
    :param name:
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    drink = drinks.search(name)
    if drink is not None:
        return render_template("showcocktail.html", data=drink, heading=heading)
    else:
        return render_template("showcocktail.html", data=drinks.search('none'), heading=heading)


@app.route("/cocktails")
def cocktails():
    """
        Show cocktail list
    :return:
    """
    heading = config['heading']
    drinks = Cocktails()
    data = drinks.getAll()
    return render_template("listcocktails.html", data=data, heading=heading)


@app.route("/ingredients")
def ingredients():
    """
        A list of ingredients and quantities
    :return:
    """
    drinks = Cocktails()
    data = drinks.getIngredients()
    # sorted_dict = {k: disordered[k] for k in sorted(disordered)}
    # sorted_data = {k: data for k in sorted(data)}
    return render_template("listingredients.html", data=data, heading=config['heading'])

@app.route("/base")
def base():
    """
        A list of ingredients and quantities
    :return:
    """
    drinks = Cocktails()
    data = drinks.getByBase()
    # sorted_dict = {k: disordered[k] for k in sorted(disordered)}
    # sorted_data = {k: data for k in sorted(data)}
    return render_template("showbybase.html", data=data, heading=config['heading'])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
