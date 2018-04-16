
import math

max_for_z_tilt = math.sqrt(2)

def solve(A):
  ans = [[0.5, 0, 0],
       [0, 0.5, 0],
       [0, 0, 0.5]]

  if A >= max_for_z_tilt:
    return ans 

  x = math.asin(A/max_for_z_tilt)-(math.pi/4)
  if abs(x) < 1e-6:
    return ans 
  # offset = math.sin(x) - 0.5

  ans[0][0] = math.sin(x) * 0.5
  ans[0][1] = math.cos(x)* 0.5

  ans[1][0] = math.cos(x)* 0.5
  ans[1][1] = -math.sin(x)* 0.5
  # print(x * 180/math.pi)
  return ans

t = int(input())
for case in range(t):
  A = float(input())
  ans = solve(A)

  print('Case #{case}'.format(case=case))
  for row in ans:
    print(' '.join(map(str, row)))
