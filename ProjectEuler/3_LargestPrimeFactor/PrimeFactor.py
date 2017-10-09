#!/usr/bin/env python
#PrimeFactor.py

import sys
import argparse

FLAGS = None

def expandPrimeList(prime_list):
	if len(prime_list) == 0:
		prime_list.append(2)
		return
	elif len(prime_list) == 1:
		prime_list.append(3)
		return
	counter = prime_list[-1] + 2
	while True:
		is_prime = True
		for i in prime_list:
			if counter % i == 0:
				is_prime = False
				break
		if is_prime:
			prime_list.append(counter)
			return
		counter += 2

def decomposeNum(prime_list, num):
	new_num = num
	for prime in prime_list:
		while True:
			if(new_num % prime == 0):
				new_num = new_num / prime
			else:
				break
	return new_num

def main(_):
	num = FLAGS.num
	print(num)
	primes = []
	while True:
		expandPrimeList(primes)
		num = decomposeNum(primes, num)
		if num == 1:
			break
	print(primes)
			
if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--num', action='store', type=int, default=600851475143)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)