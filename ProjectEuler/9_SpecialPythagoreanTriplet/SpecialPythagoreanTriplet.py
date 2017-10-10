#!/usr/bin/env python
#MultiplesOf3And5.py

import sys
import argparse

FLAGS = None

def pythagoreanTriple(x,y):
	if y >= x: 
		return
	a = (x*x) - (y*y)
	b = 2*x*y
	c = (x*x) + (y*y)
	return (a,b,c)

def main(_):
	for y in range(1, 1001):
		for x in range(y+1, 1001):
			triple = pythagoreanTriple(x,y)
			if sum(triple) == 1000:
				print(triple[0]*triple[1]*triple[2])
				return

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')

	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)