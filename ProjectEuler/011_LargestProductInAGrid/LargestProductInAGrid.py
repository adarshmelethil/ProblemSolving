#!/usr/bin/env python
#MultiplesOf3And5.py

import sys
import argparse

FLAGS = None

def readFile(file_name):
	file_of_numbers = open(file_name, "r")
	num_matrix = []
	for i in range(20):
		read_line = file_of_numbers.readline()
		nums_row = list(map(int, read_line.split(" ")))
		num_matrix.append(nums_row)

	return num_matrix

def largestSum(matrix):

	set_of_num = []
	best_sum = 0
	for i in range(len(matrix)):
		row = matrix[i]
		for j in range(len(row)-4):
			if len(set_of_num) >= 4:
				sum_of_num = sum(set_of_num)
				if sum_of_num > best_sum:
					best_sum = sum_of_num
				set_of_num.remove(set_of_num[0])
			set_of_num.append(row[j])

def main(_):
	matrix_of_num = readFile(FLAGS.file_name)
	# for row in matrix_of_num:
	# 	for cell in row:
	# 		print(type(cell))
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-f','--file_name', action='store', type=str, default="in.txt")
	parser.add_argument('-n','--num_of_sum', action='store', type=int, default=4)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)