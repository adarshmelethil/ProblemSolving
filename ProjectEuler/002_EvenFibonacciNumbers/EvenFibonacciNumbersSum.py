#!/usr/bin/env python
#EvenFibonacciNumbersSum.py

import sys
import argparse

FLAGS = None

def main(_):
	sum_total = 2
	if FLAGS.sum_below < 2:
		print(0)
		return
	elif FLAGS.sum_below < 3:
		print(2)
		return

	previous_digits = [1, 2]
	current_digit = -1
	while True:
		current_digit = sum(previous_digits)
		if current_digit >= FLAGS.sum_below:
			break
		if current_digit % 2 == 0:
			sum_total += current_digit
		previous_digits[0] = previous_digits[1]
		previous_digits[1] = current_digit


	print(sum_total)
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-b','--sum_below', action='store', type=int, default=4000000)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)