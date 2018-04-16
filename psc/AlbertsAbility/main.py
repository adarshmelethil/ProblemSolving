
# 2 sec - move
# 1 sec - press
# 5 sec - space

MOVE = 2
PRESS = 1
SPACE = 5

keyset = [
	"QWERTYUIOP",
	"ASDFGHJKL",
	"ZXCVBNM"]

def getTime(pos, msg):
	msg = msg.upper()
	time = 0
	for a in msg:
		if a == ' ':
			time += SPACE
			continue

		for i in range(3):
			if a in keyset[i]:
				break

		time += abs(pos[0] - i) * MOVE
		pos[0] = i 

		ind = keyset[pos[0]].index(a)
		time += abs(pos[1] - ind) * MOVE
		pos[1] = ind
		time += PRESS
	return time

t = int(input())
for _ in range(t):
	msg = input()
	cur_pos = [0,2]
	print(getTime(cur_pos, msg))
