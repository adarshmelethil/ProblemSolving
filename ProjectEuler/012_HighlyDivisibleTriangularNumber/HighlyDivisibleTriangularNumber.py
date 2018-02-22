import sys
import argparse
import math

FLAGS = None

def numOfDivisor(num):
	if num == 1:
		return 1
	if num < 4:
		return 2

	devisors = 2
	for i in range(2, math.ceil(math.sqrt(num))):
		# print("-",i)
		if num % i == 0:
			devisors += 2

	return devisors



def main(_):
	cur_num = 1
	index = 1
	cur_divisor = numOfDivisor(cur_num)

	while cur_divisor < FLAGS.over_num:
		index += 1
		cur_num += index
		cur_divisor = numOfDivisor(cur_num)
		# print(cur_num, cur_divisor)

	print(cur_num)


if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	# parser.add_argument('-f','--file_name', action='store', type=str, default="in.txt")
	parser.add_argument('-n','--over_num', action='store', type=int, default=500)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)