#!/usr/bin/env python
#SummationOfPrimes.py

import sys
import argparse

FLAGS = None

def primesBelow(number):
	primes_list = [2]
	num = 3
	num_of_primes = 1
	while(primes_list[-1] < number):
		is_prime = True
		for primes in primes_list:
			if num%primes == 0:
				is_prime = False
				break
		if is_prime:
			primes_list.append(num)
			num_of_primes += 1
		num += 2
		print(num, num_of_primes, end="\r")
	return primes_list[:-1:]

def main(_):
	primes_list = primesBelow(FLAGS.sum_primes_below)
	print(sum(primes_list))
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-b','--sum_primes_below', action='store', type=int, default=2000000)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)