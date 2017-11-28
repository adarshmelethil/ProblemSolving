#!/usr/bin/env python
#SumSquareDifference.py

import sys
import argparse

FLAGS = None

def main(_):
	total = 0
	for i in range(1, FLAGS.numbers+1):
		for j in range(1, FLAGS.numbers+1):
			if i == j:
				continue
			product = i * j
			total += product
	print(total)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-n','--numbers', action='store', type=int, default=100)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)