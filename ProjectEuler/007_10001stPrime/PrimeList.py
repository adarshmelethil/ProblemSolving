#!/usr/bin/env python
#PrimeList.py

import sys
import argparse

FLAGS = None

def getPrimes(number_of_primes):
	primes_list = [2]
	if number_of_primes == 1:
		return primes_list
	num = 3
	while(len(primes_list) < number_of_primes):
		is_prime = True
		for prime in primes_list:
			if num % prime == 0:
				is_prime = False
				break
		if is_prime:
			primes_list.append(num)
		num += 2

	return primes_list
def main(_):
	print(getPrimes(FLAGS.number_of_primes))
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--number_of_primes', action='store', type=int, default=10001)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)