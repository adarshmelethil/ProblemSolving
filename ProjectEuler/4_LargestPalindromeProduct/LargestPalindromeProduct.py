#!/usr/bin/env python
#MultiplesOf3And5.py

import sys
import argparse

import numpy as np


FLAGS = None

def isPalindrome(num):
	num_str = str(num)
	for i in range(int(len(num_str)/2)):
		if num_str[i] != num_str[-i-1]:
			return 0
	return num

def main(_):
	if(FLAGS.number_of_digits < 1):
		return
	upper_bound = int("9"*FLAGS.number_of_digits)
	if(FLAGS.number_of_digits == 1):
		lower_bound = 0
	else:
		lower_bound = int("9"*(FLAGS.number_of_digits-1))
	
	nums = np.arange(lower_bound+1, upper_bound+1)
	nums = nums.reshape(-1, 1)
	all_products = np.matmul(nums, np.transpose(nums))
	vfunc = np.vectorize(isPalindrome)
	palindromes = vfunc(all_products)
	print(palindromes.max())

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--number_of_digits', action='store', type=int, default=3)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)