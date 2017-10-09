#!/usr/bin/env python
#LargestProductInASeries.py

import sys
import argparse

FLAGS = None


def main(_):
	file_of_numbers = open(FLAGS.file_name, "r")
	read = file_of_numbers.read()
	number_of_digits = FLAGS.number_of_digits
	digits = []
	best_digits = []
	best_product = 0
	for c in read:
		if c.isdigit():
			if len(digits) >= number_of_digits:
				product = 1
				for d in digits:
					product *= d
				if product > best_product:
					best_product = product
					best_digits = digits
				digits.remove(digits[0])
			digits.append(int(c))
	print(best_product)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--number_of_digits', action='store', type=int, default=13)
	parser.add_argument('-f','--file_name', action='store', type=str, default="num.txt")



	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)