import sys
import argparse
import math

FLAGS = None


def readLineFromFile(file_name):
	with open(file_name, "r") as file_obj:
		num_matrix = []
		for line in file_obj:
			yield line

	# return num_matrix

def main(_):
	sum = 0
	for line in readLineFromFile(FLAGS.file_name):
		sum += int(line)

	print (sum)
	# print(type(sum))

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	parser.add_argument('-f','--file_name', action='store', type=str, default="in.txt")
	# parser.add_argument('-n','--over_num', action='store', type=int, default=500)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)