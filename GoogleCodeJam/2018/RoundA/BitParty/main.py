


def solve(R, B, C, M, S, P):
  print(R, B, C, M, S, P)
  itter = {}
  b = B 
  for i in range(C):
    items = M[i]
    left = B - M[i]
    if b < M[i]:
      items = b 
      left = 0

    itter[i] = {
      'time': b*S[i] + P[i],
      'b_left': left 
    }

  for i in itter:
    
  return 1

t = int(input())
for case in range(t):
  R, B, C= map(int, input().split())
  
  M, S, P = [], [], []
  for i in range(C):
    m,s,p, = map(int, input().split())
    M.append(m)
    S.append(s)
    P.append(p)

  ans = solve(R, B, C, M, S, P)
  
  print('Case #{case}: {ans}'.format(case=case+1, ans=ans))

