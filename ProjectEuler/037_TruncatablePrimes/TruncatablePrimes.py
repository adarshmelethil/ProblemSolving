#!/usr/bin/env python 
#TruncatablePrimes.py

import sys
import argparse 
from math import sqrt

FLAGS = None 

primes = [2,3,5,7]

def addToPrimesTill(n):
  cur_num = primes[-1]

  while cur_num <= sqrt(n):
    cur_num += 2
    is_prime = True 
    for prime in primes:
      if cur_num % prime == 0:
        is_prime = False 
        break 
    if is_prime:
      primes.append(cur_num)
      if n == cur_num:
        return True 

      if n % cur_num == 0:
        return False

  return True 
def isPrime(n):
  if n == 1:
    return False
  for prime in primes:
    if n == prime:
      return True

    if n % prime == 0:
      return False 

  return addToPrimesTill(n)

def isTruncatable(n):
  if n / 10 == 0 or not isPrime(n):
    return False

  num_of_digits = len(str(n))
  for i in range(1, num_of_digits):
    num1 = n // (10**i)
    num2 = n % 10**(num_of_digits-i)
    if not isPrime(num1) or not isPrime(num2):
      return False

  return True 

def main(_):
  starting_set = ('2','3','5','7')
  ending_set = ('3','7')

  count = 0
  total = 0
  middle = 0
  while count < 11:
    for start in starting_set:
      for end in ending_set:
        if middle == 0:
          num = int(start + end)
        else:
          num = int(start + str(middle) + end)
        if isTruncatable(num):
          count += 1 
          total += num 
    middle += 1

  print(total)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Project euler problem 37, truncated primes")
  
  FLAGS, unparsed = parser.parse_known_args()
  main(unparsed)


