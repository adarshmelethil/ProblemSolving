
import sys
import math 


offset = 2

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

def getInput(l,w, i,j):
  x = i 
  y = j 
  if i == 0:
    x += 1
  elif i == l-1:
    x -= 1
  if j == 0:
    y += 1
  elif j == w-1:
    y -= 1
  return [x,y] 


def checkArr(arr, l, w):
  for i in range(offset, l+offset):
    for j in range(offset, w+offset):
      if not arr[i][j]:
        vals = getInput(l,w, i-offset, j-offset)

        return vals[0]+offset, vals[1]+offset

def getFactors(A):
  fac = []
  for i in range(1,int(math.sqrt(A))+1):
    if A % i == 0:
      fac.append(i)
  return fac 

def printOut(arr, l, w):
  for i in range(0, l+offset+2):
    for j in range(0, w+offset+2):
      eprint('{}, '.format(arr[i][j]), end='')
    eprint('')

t = int(input())
for case in range(t):
  A = int(input())
  arr = [[False]*1000 for _ in range(1000)]
  
  facs = getFactors(A)
  l = facs[-1]
  w = A // l 
  while True:
    vals = checkArr(arr, l, w)
    if vals is None:
      printOut(arr, l, w)
      exit(1)
    output = '{x} {y}'.format(x=vals[0], y=vals[1])

    print(output)
    sys.stdout.flush()
    input_val = list(map(int, input().split(" ")))

    if input_val[0] == 0:
      break
    if input_val[0] < 0:
      exit()

    arr[input_val[0]][input_val[1]] = True
