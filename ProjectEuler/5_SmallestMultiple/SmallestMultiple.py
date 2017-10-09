#!/usr/bin/env python
#MultiplesOf3And5.py

import sys
import argparse

FLAGS = None

def getListOfPrime(upper_bound):
	if upper_bound < 2:
		return
	primes = []
	for num in range(2,upper_bound+1):
		for prime in primes:
			if num % prime == 0:
				num = int(num / prime)
		if num != 1:
			primes.append(num)
	return primes 

def main(_):
	primes_list = getListOfPrime(FLAGS.numbers_to)
	product = 1
	for prime in primes_list:
		product *= prime

	print(product)
	

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--numbers_to', action='store', type=int, default=20)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)