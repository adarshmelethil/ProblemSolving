

def troubleSort(l):
  done = False 
  while not done:
    done = True 
    for i in range(len(l)-2):
      if l[i] > l[i+2]:
        done = False
        temp = l[i]
        l[i] = l[i+2]
        l[i+2] = temp 
  return l
def solve(l, n):
  new_l = troubleSort(l)
  for i in range(len(new_l)-1):
    if new_l[i] > new_l[i+1]:
      return i 
  return 'OK'


t = int(input())
for case in range(t):
  n = int(input())
  l = list(map(int, input().split(' ')))
  ans = solve(l, n)

  print('Case #{}: {}'.format(case+1, ans))

