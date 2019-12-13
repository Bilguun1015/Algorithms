#!/usr/bin/python

import sys

# 16

# 1 dime and 6 cents
# 1 dime and 1 nickel

# 3 nickels and 1 cent
# 2 nickels and 6 cents
# 1 nickel and 11 cents

# 16 cents

# 26
# a quarter and a cent

# 2 dimes and 1 nickel and 1 cent
# 2 dimes and 6 cents

# 1 dime and 1 nickel and 11 cents
# 1 dime and 2 nickels and 6 cent
# 1 dime and 3 nickels and 1 cent
# 1 dime and 16 cents


# 5 nickels and 1 cent
# 4 nickels and 6 cents
# 3 nickels and 11 cents
# 2 nickels and 16 cents
# 1 nickel and 21 cents

# 26 cents

# 25 
# 1 quarter

# 2 dimes and 1 nickel
# 2 dimes and 5 cents

# 1 dime and 3 nickels
# 1 dime and 2 nickels and 5 cents
# 1 dime and 1 nickel and 10 cents
# 1 dime and 15 cents


# 24

# 2 dimes and 4 cents

# 1 dime and 2 nickels and 4 cents
# 1 dime and 1 nickel and 9 cents
# 1 dime and 14 cents

# 31

# 1 quarter and 1 nickel and 1 cent
# 1 quarter and 6 cents

# 3 dimes and 1 cent

# 2 dimes and 2 nickels and 1 cent
# 2 dimes and 1 nickel and 6 cents
# 2 dimes and 11 cents

# 1 dime and 4 nickels and 1 cent
# 1 dime and 3 nickels and 6 cents
# 1 dime and 2 nickels and 11 cents
# 1 dime and 1 nickel and 16 cents
# 1 dime and 21 cents

# 6 nickels and 1 cent
# 5
# 4
# 3
# 2
# 1


# 31 cents
# #51
# 2 quarters and 1 cent
# 1 quarter and (
#     2 dimes and 1 nickel and 1 cent
#     2 dimes and 6 cents

#     1 dime and 1 nickel and 11 cents
#     1 dime and 2 nickels and 6 cent
#     1 dime and 3 nickels and 1 cent
#     1 dime and 16 cents


#     5 nickels and 1 cent
#     4 nickels and 6 cents
#     3 nickels and 11 cents
#     2 nickels and 16 cents
#     1 nickel and 21 cents
#     26 cents
# )

# N = 10
# D = 9 + 7 + 5 + 3 + 1
# Q1 = 1 + 2 + 4 + 5
# C = 1

# 101
# C = 1
# N = 20
# D = 19 + 17 + 15 + 13 + 11 + 9 + 7 + 5 + 3 + 1
# H = 50


cache = []
def making_change(amount, denominations):
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  cache = [0] * (amount + 1)
  cache[0] = 1
  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      previous_amount = higher_amount - coin
      new_amount = cache[previous_amount]
      if not previous_amount and (higher_amount+1) % 5 == 0 and coin is not 1:
        new_amount = new_amount + 1
      cache[higher_amount] += new_amount
    print(cache)
  return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    # denominations = [1, 5, 10, 25, 50]
    denominations = [1,5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")


