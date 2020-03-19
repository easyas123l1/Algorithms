#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}
def eating_cookies(n, cache=None):
  if cache is None:
    cache = {}
  # edge case if n = 0 we return 1 cookie
  if n == 0:
    return 1
  # base cases
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  if cache and cache[n]:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')