import json
import random
import re

class Cocktails():
    """
        Class to control cocktail objects
    """
    def __init__(self):
        with open("/app/cocktails.json", "r") as jd:
            self.cocktails = {}
            self.cocktails = json.load(jd)
        self._previous = ""

    def getRandom(self):
        """
            Returns a random cocktail
        :return:
        """
        cocktail = random.choice(self.cocktails)
        print("Getting cocktail")
        for c in cocktail:
            if c != "none":
                if cocktail[c]['meta']['title'] != self._previous:
                    self._previous = cocktail[c]['meta']['title']
                    return cocktail[c]
                else:
                    return self.getRandom()
            else:
                return self.getRandom()

    def getAll(self):
        """
            Simply return all cocktails as a dict
        :return:
        """
        return self.cocktails

    def getByBase(self):
        """
            Get all cocktails by base drink
        :param base: str
        :return:
        """
        cocktails = {}
        for eachCocktail in self.cocktails:
            # print(eachCocktail)
            for c in eachCocktail:
                # print(eachCocktail)
                if eachCocktail[c]['meta']['base'] not in cocktails:
                    cocktails[eachCocktail[c]['meta']['base']] = []
                cocktails[eachCocktail[c]['meta']['base']].append(eachCocktail[c]['meta']['title'])
        return cocktails

    def getIngredients(self):
        """
            Return a list of ingredients
        :return: list
        """
        ingredients = {}
        for eachCocktail in self.cocktails:
            for c in eachCocktail:
                # print(c)
                for eachIngredient in eachCocktail[c]['ingredients']:
                    # print(json.dumps(eachIngredient, indent=2))
                    if eachIngredient[0] in ingredients:
                        ingredients[eachIngredient[0]]['qty'] += int(eachIngredient[1])
                    else:
                        ingredients[eachIngredient[0]] = {}
                        ingredients[eachIngredient[0]]['qty'] = int(eachIngredient[1])
                        ingredients[eachIngredient[0]]['unit'] = eachIngredient[2]
        return ingredients

    def search(self, name: str):
        """
            Search for a cocktail name
        :return:
        """
        for eachCocktail in self.cocktails:
            for c in eachCocktail:
                if re.search(name.lower(), eachCocktail[c]['meta']['title'].lower()):
                    return eachCocktail[c]
        return None
