

def simulate(alex, sonny):
	


safe_output = "Sonny and Alex are safe"
t = int(input())
for _ in range(t):
	a, b, c, d, e, f = map(int, input().split(' '))
	print([a, b, c], [d, e, f])
