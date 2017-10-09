#!/usr/bin/env python
#MultiplesOf3And5.py

import sys
import argparse

FLAGS = None

def multipleOf3or5(num):
	if num % 3 == 0:
		return True
	elif num % 5 == 0:
		return True
	else:
		return False

def main(_):
	sum_total = 0
	for num in range(FLAGS.sum_below):
		if(multipleOf3or5(num)):
			sum_total += num
	print(sum_total)
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-b','--sum_below', action='store', type=int, default=1000)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)