#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = prices[0]
  profit = -prices[0]
  for price in prices:
    if price - current_min_price_so_far > profit and prices.index(price) != 0:
      profit = price - current_min_price_so_far
    if price < current_min_price_so_far:
      current_min_price_so_far = price

  return profit

print(find_max_profit([6,5,1,5,8,9,3,8,1]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))