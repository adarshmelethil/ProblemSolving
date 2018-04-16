
def switch(s, switch_at, cur_dmg):
  ind = switch_at[-1][0]
  dmg = switch_at[-1][1]

  if ind < len(s)-1:
    end = s[ind+1:]
  else:
    end = ''
  
  new_s = s[:ind-1] + s[ind] + s[ind-1] + end 
  cur_dmg -= (dmg/2)

  del switch_at[-1]
  if ind-2 > 0:
    if new_s[ind-2] == 'C':
      switch_at.append((ind-1, dmg//2))
  if ind + 1 < len(new_s):
    if new_s[ind+1] == 'S':
      switch_at.append((ind+1, dmg))


  return new_s, switch_at, cur_dmg

def solve(D,s):
  s_count = 0
  c_count = 0
  shoot_dmg = 1
  cur_dmg = 0

  switch_at = []
  for i in range(len(s)):
    if s[i] == "S":
      s_count += 1
      cur_dmg += shoot_dmg

      if i > 0:
        if s[i-1] == "C":
          switch_at.append((i, shoot_dmg))
    else:
      c_count += 1
      shoot_dmg *= 2

  switch_count = 0
  if D < s_count:
    return 'IMPOSSIBLE'

  while cur_dmg > D:
    if len(switch_at) < 1:
      return 'IMPOSSIBLE'
    
    s, switch_at, cur_dmg = switch(s, switch_at, cur_dmg)
    switch_count += 1

  return switch_count

t = int(input())
for case in range(t):
  D, s = input().split(' ')
  D = int(D)
  ans = solve(D, s)

  print('Case #{}: {}'.format(case+1, ans))

