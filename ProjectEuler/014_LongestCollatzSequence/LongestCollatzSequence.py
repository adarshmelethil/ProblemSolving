import sys
import argparse
import math

FLAGS = None

def NextCollatz(n):
	if n%2 ==0 :
		return n//2
	else:
		return 3*n +1

CollatzDict = {}
def getChainLength(num):
	global CollatzDict
	if num in CollatzDict:
		print("here")
		return CollatzDict[n]

	chain_length = 1
	n = num
	while n != 1:
		n = NextCollatz(n)
		if n in CollatzDict:
			chain_length += CollatzDict[n]
			break

		chain_length += 1

	CollatzDict[num] = chain_length
	return chain_length

def main(_):
	max_chain = 0
	max_num = 0
	for i in range(1, FLAGS.max_num):
		cur_chain = getChainLength(i)
		if cur_chain > max_chain:
			max_num = i
			max_chain = cur_chain


	print(max_num, max_chain)
	

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Mapper to calculate n-gram')
	# parser.add_argument('-f','--file_name', action='store', type=str, default="in.txt")
	parser.add_argument('-n','--max_num', action='store', type=int, default=1000000)


	FLAGS, unparsed = parser.parse_known_args()
	main(unparsed)