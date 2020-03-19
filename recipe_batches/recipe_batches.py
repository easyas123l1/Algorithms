#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # set batches made to 0
  batches = None
  for key in recipe:
    if key in ingredients.keys():
      possible = ingredients[key] // recipe[key]
      if batches == None:
        batches = possible
      if possible < batches:
        batches = possible
    else:
      return 0

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))