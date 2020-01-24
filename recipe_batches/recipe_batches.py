#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ratio = 0
  first = True
  for ingredient, amount in recipe.items():
    new_ratio = ingredients.get(ingredient, 0) // amount
    if first:
      ratio = new_ratio
      first = False
    elif new_ratio < ratio:
      ratio = new_ratio
  return ratio

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))