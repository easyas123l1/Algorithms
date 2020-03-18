#!/usr/bin/python

import argparse


def find_max_profit(prices):
  #money made set to 0
  money = 0
  #iterate thru prices
  buys = 0
  for i in range(0, len(prices) - 1):
    #iterate thru prices again with j
    for j in range(1, len(prices) - 1):
      #make sure j is after i
      if j > i:
        #make sure j - i is > current possible money
        #if money = -100000000000 is cheating change if statement below to have or buys == 0
        if prices[j] - prices[i] > money or buys == 0:
          # j - i = money made!
          money = prices[j] - prices[i] 
          buys += 1

  return money


print(find_max_profit([10, 7, 5, 8, 11, 9]))





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))